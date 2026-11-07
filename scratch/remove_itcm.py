import os

files_to_fix = [
    ('source/Chunk.h', [
        ('ITCM_CODE void rebuildColumnOccupancy(', 'void rebuildColumnOccupancy('),
        ('ITCM_CODE void computeColumnFacesBitwise(', 'void computeColumnFacesBitwise(')
    ]),
    ('source/Chunk.cpp', [
        ('ITCM_CODE void Chunk::rebuildColumnOccupancy(', 'void Chunk::rebuildColumnOccupancy('),
        ('ITCM_CODE void Chunk::computeColumnFacesBitwise(', 'void Chunk::computeColumnFacesBitwise(')
    ]),
    ('source/Player.h', [
        ('ITCM_CODE void physicsTick(', 'void physicsTick('),
        ('ITCM_CODE bool collidesAt(', 'bool collidesAt(')
    ]),
    ('source/Player.cpp', [
        ('ITCM_CODE bool Player::collidesAt(', 'bool Player::collidesAt('),
        ('ITCM_CODE void Player::physicsTick(', 'void Player::physicsTick(')
    ]),
    ('source/VoxelRLE.h', [
        ('ITCM_CODE void unpack(', 'void unpack(')
    ]),
    ('source/Hardware.h', [
        ('ITCM_CODE static void applyClockSafeTWL()', 'static void applyClockSafeTWL()')
    ])
]

for filepath, replacements in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    initial_content = content
    for old_str, new_str in replacements:
        assert old_str in content, f"Target '{old_str}' not found in {filepath}!"
        content = content.replace(old_str, new_str)
        print(f"Replaced '{old_str}' in {filepath}")
        
    assert content != initial_content, f"No changes made in {filepath}!"
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

print("\nSUCCESS: All ITCM_CODE references removed completely!")

