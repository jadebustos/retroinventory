import copy

from data import *

vtech = copy.deepcopy(data)

# default data is loaded

# vtech data

vtech['description']['manufacturer'] = 'vtech'

# Laser 200
vtech['specs'] = hw_data.copy()
vtech['specs']['ram'] = '4 KB'
vtech['specs']['rom'] = '16 KB'
vtech['specs']['vram'] = '16 KB'
vtech['description']['model'] = 'Laser 200'
laser200_data = copy.deepcopy(vtech)
