import copy

from data import data

vtech = copy.deepcopy(data)

# default data is loaded

# vtech data

vtech['description']['manufacturer'] = 'vtech'

# Laser 200
vtech['specs']['cpubits'] = '8'
vtech['specs']['cpuvendor'] = 'Zilog'
vtech['specs']['cpumodel'] = 'Z80A'
vtech['specs']['cpuspeed'] = '3.58 MHz'
vtech['specs']['ram'] = '4 KB'
vtech['specs']['rom'] = '16 KB'
vtech['specs']['vram'] = '16 KB'
vtech['description']['model'] = 'Laser 200'
laser200_data = copy.deepcopy(vtech)
