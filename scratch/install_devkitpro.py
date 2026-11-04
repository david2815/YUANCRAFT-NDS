import os, urllib.request, tarfile

packages = [
    ("devkitARM", "https://wii.leseratte10.de/devkitPro/devkitARM/r55%20%282020-07-25%29/devkitARM-r55-1-windows_x86_64.pkg.tar.xz"),
    ("devkitarm-rules", "https://wii.leseratte10.de/devkitPro/devkitARM/devkitarm-rules/devkitarm-rules-1.2.3-1-any.pkg.tar.xz"),
    ("libnds", "https://wii.leseratte10.de/devkitPro/libnds/libnds_1.8.2%20%282022%29/libnds-1.8.2-1-any.pkg.tar.xz"),
    ("libfat", "https://wii.leseratte10.de/devkitPro/libfat/libfat_1.1.5%20%282020-04-18%29/libfat-nds-1.1.5-1-any.pkg.tar.xz"),
    ("libfilesystem", "https://wii.leseratte10.de/devkitPro/libfilesystem/libfilesystem_0.9.14%20%282018%29/libfilesystem-0.9.14-2-any.pkg.tar.xz"),
    ("default_arm7", "https://wii.leseratte10.de/devkitPro/default_arm7/default-arm7-0.7.4-7-any.pkg.tar.xz"),
    ("ndstool", "https://wii.leseratte10.de/devkitPro/other-stuff/ndstool/ndstool-2.1.2-2-windows_x86_64.pkg.tar.xz"),
    ("grit", "https://wii.leseratte10.de/devkitPro/other-stuff/grit/grit-0.8.17-1-windows_x86_64.pkg.tar.xz"),
    ("general-tools", "https://wii.leseratte10.de/devkitPro/other-stuff/general-tools/general-tools-1.2.0-3-windows_x86_64.pkg.tar.xz"),
]

dest_dir = r"C:\Users\Lendy\msys64"
temp_dir = os.environ.get("TEMP", r"C:\Users\Lendy\AppData\Local\Temp")

for name, url in packages:
    print(f"Downloading {name} from {url}...")
    filename = url.split("/")[-1].replace("%20", " ")
    tar_path = os.path.join(temp_dir, filename)
    
    if not os.path.exists(tar_path):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(tar_path, "wb") as out:
            out.write(resp.read())
        print(f"Saved {tar_path}")
    else:
        print(f"Already cached: {tar_path}")
        
    print(f"Extracting {name} into {dest_dir}...")
    with tarfile.open(tar_path, "r:xz") as tar:
        tar.extractall(dest_dir)
    print(f"{name} extracted successfully!")

print("\nAll devkitPro components installed successfully!")

