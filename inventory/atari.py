import copy

from data import data

atari = copy.deepcopy(data)

# default data is loaded

# atari data
atari['description']['manufacturer'] = 'Atari'

# Atari 800
atari['specs']['cpubits'] = '8'
atari['specs']['cpuvendor'] = 'Rockwell'
atari['specs']['cpumodel'] = '6502'
atari['specs']['cpuspeed'] = '1.79 MHz'
atari['specs']['ram'] = '64 KB'
atari['specs']['rom'] = '24 KB'
atari_800_data = copy.deepcopy(atari)

# Atari 1040
atari['specs']['cpubits'] = '16'
atari['specs']['cpuvendor'] = 'Motorola'
atari['specs']['cpumodel'] = '68000'
atari['specs']['cpuspeed'] = '9 MHz'
atari['specs']['ram'] = '512 KB'
atari['specs']['rom'] = '196 KB'
atari_1040_data = copy.deepcopy(atari)