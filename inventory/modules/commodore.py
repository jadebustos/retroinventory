import copy

from data import data

commodore = copy.deepcopy(data)

# default data is loaded

# commodore data
commodore['description']['manufacturer'] = 'Commodore'

# VIC-20
commodore['specs']['cpubits'] = '8'
commodore['specs']['cpuvendor'] = 'MOS Technology'
commodore['specs']['cpumodel'] = '6502'
commodore['specs']['cpuspeed'] = '1.1 MHz'
commodore['specs']['ram'] = '5 KB'
commodore['specs']['rom'] = '20 KB'
commodore['description']['model'] = 'VIC-20'
vic20_data = copy.deepcopy(commodore)

# Commodore 16
commodore['specs']['cpubits'] = '8'
commodore['specs']['cpuvendor'] = 'MOS Technology'
commodore['specs']['cpumodel'] = '8501'
commodore['specs']['cpuspeed'] = '1.76 MHz'
commodore['specs']['ram'] = '16 KB'
commodore['specs']['rom'] = '20 KB'
commodore['description']['model'] = 'Commodore 16'
c16_data = copy.deepcopy(commodore)

# Commodore 64
commodore['specs']['cpubits'] = '8'
commodore['specs']['cpuvendor'] = 'MOS Technology'
commodore['specs']['cpumodel'] = '6510/8500'
commodore['specs']['cpuspeed'] = '0.985 MHz'
commodore['specs']['ram'] = '64 KB'
commodore['specs']['rom'] = '20 KB'
c64_data = copy.deepcopy(commodore)

# Commodore 128
commodore['specs']['cpubits'] = '8'
commodore['specs']['cpuvendor'] = 'MOS Technology'
commodore['specs']['cpumodel'] = '8502'
commodore['specs']['cpuspeed'] = '2 MHz'
commodore['specs']['ram'] = '128 KB'
commodore['specs']['vram'] = '16 KB'
commodore['specs']['rom'] = '72 KB'
c128_data = copy.deepcopy(commodore)

# Amiga
commodore['specs']['cpubits'] = '16'
commodore['specs']['cpuvendor'] = 'Motorola'
commodore['specs']['cpumodel'] = '68000'
commodore['specs']['cpuspeed'] = '7.14 MHz'
commodore['specs']['ram'] = '512 KB'
commodore['specs']['rom'] = '512 KB'
amiga_data = copy.deepcopy(commodore)