import copy

from data import data

msx = copy.deepcopy(data)

# MSX
msx['specs']['cpubits'] = '8'
msx['specs']['cpuvendor'] = 'Zilog'
msx['specs']['cpumodel'] = 'Z80A'
msx['specs']['cpuspeed'] = '3.58 MHz'
msx['specs']['ram'] = '64 KB'
msx['specs']['vram'] = '16 KB'
msx['specs']['rom'] = '32 KB'
msx_data = copy.deepcopy(msx)

# MSX2
msx['specs']['cpubits'] = '8'
msx['specs']['cpuvendor'] = 'Zilog'
msx['specs']['cpumodel'] = 'Z80A'
msx['specs']['cpuspeed'] = '3.58 MHz'
msx['specs']['ram'] = '64 KB'
msx['specs']['vram'] = '64 KB'
msx['specs']['rom'] = '48 KB'
msx2_data = copy.deepcopy(msx)

# MSX2 PLUS
msx['specs']['cpubits'] = '8'
msx['specs']['cpuvendor'] = 'Zilog'
msx['specs']['cpumodel'] = 'Z80A'
msx['specs']['cpuspeed'] = '3.58 MHz'
msx['specs']['ram'] = '64 KB'
msx['specs']['vram'] = '128 KB'
msx['specs']['rom'] = '32 KB'
msx2plus_data = copy.deepcopy(msx)

# MSX Turbo R
msx['specs']['cpubits'] = '8'
msx['specs']['cpuvendor'] = 'ASCII Corporation'
msx['specs']['cpumodel'] = 'R800'
msx['specs']['cpuspeed'] = '14.32 MHz'
msx['specs']['ram'] = '256 KB'
msx['specs']['vram'] = '128 KB'
msx['specs']['rom'] = '96 KB'
msxtr_data = copy.deepcopy(msx)

# MSX VR
msx['specs']['cpubits'] = '64'
msx['specs']['cpuvendor'] = 'ARM'
msx['specs']['cpumodel'] = 'ARMv8'
msx['specs']['cpuspeed'] = '1.4 GHz'
msx['specs']['ram'] = '1 GB'
msxvr_data = copy.deepcopy(msx)