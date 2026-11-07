import math

def simulate_hw_divf(a, b):
    if b == 0.0:
        return 0.0
    fa = int(a * 4096.0)
    fb = int(b * 4096.0)
    if fb == 0:
        return 0.0
    # REG_DIVCNT = DIV_64_32
    # REG_DIV_NUMER = ((int64_t)fa) << 12
    # REG_DIV_DENOM_L = fb
    numer64 = fa << 12
    # Integer division as performed by DS hardware divider
    res = int(numer64 / fb)
    return res / 4096.0

def simulate_hw_sqrtf(val):
    if val <= 0.0:
        return 0.0
    fixed_val = int(val * 4096.0)
    # REG_SQRTCNT = SQRT_64
    # REG_SQRT_PARAM = ((int64_t)fixed_val) << 12
    param64 = fixed_val << 12
    res = int(math.isqrt(param64))
    return res / 4096.0

def test_math_accuracy():
    print("=== TEST SUITE 2: Math Coprocessor Emulation & Accuracy Test ===")

    # Test 1: Vector normalization sqrt and div
    for vx, vz in [(0.5, 0.5), (0.1, 0.9), (1.2, 0.3), (0.05, 0.05), (10.0, 0.0)]:
        expected_len = math.sqrt(vx * vx + vz * vz)
        hw_len = simulate_hw_sqrtf(vx * vx + vz * vz)
        err_len = abs(expected_len - hw_len)
        print(f" Sqrt test ({vx}, {vz}): expected={expected_len:.4f}, hw={hw_len:.4f}, err={err_len:.5f}")
        assert err_len < 0.01, f"Sqrt error too large: {err_len}"

        expected_norm_x = vx / expected_len
        hw_norm_x = simulate_hw_divf(vx, hw_len)
        err_norm = abs(expected_norm_x - hw_norm_x)
        print(f" Div test ({vx} / len): expected={expected_norm_x:.4f}, hw={hw_norm_x:.4f}, err={err_norm:.5f}")
        assert err_norm < 0.01, f"Div error too large: {err_norm}"

    # Test 2: Raycaster DDA plane step
    for bound, p, remain in [(5.0, 2.3, 0.8), (10.0, 8.5, -0.4), (1.0, 0.1, 0.9)]:
        expected_t = (bound - p) / remain
        hw_t = simulate_hw_divf(bound - p, remain)
        err_t = abs(expected_t - hw_t)
        print(f" DDA step test: expected={expected_t:.4f}, hw={hw_t:.4f}, err={err_t:.5f}")
        assert err_t < 0.01, f"DDA step error too large: {err_t}"

    print(" [PASS] Hardware math routines achieve high precision across all physics & raycasting cases.")

if __name__ == "__main__":
    test_math_accuracy()

