import copy

from data import data

amstrad = copy.deepcopy(data)

# default data is loaded

# amstrad data
amstrad['description']['manufacturer'] = 'Amstrad'

# cpc464
amstrad['specs']['cpubits'] = '8'
amstrad['specs']['cpuvendor'] = 'Zilog'
amstrad['specs']['cpumodel'] = 'Z80A'
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['ram'] = '64 KB'
amstrad['specs']['rom'] = '32 KB'
amstrad['description']['model'] = 'CPC464'
cpc464_data = copy.deepcopy(amstrad)

# cpc664
amstrad['specs']['cpubits'] = '8'
amstrad['specs']['cpuvendor'] = 'Zilog'
amstrad['specs']['cpumodel'] = 'Z80A'
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['ram'] = '64 KB'
amstrad['specs']['rom'] = '48 KB'
amstrad['description']['model'] = 'CPC664'
cpc664_data = copy.deepcopy(amstrad)

# cpc6128
amstrad['specs']['cpubits'] = '8'
amstrad['specs']['cpuvendor'] = 'Zilog'
amstrad['specs']['cpumodel'] = 'Z80A'
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['ram'] = '128 KB'
amstrad['specs']['rom'] = '48 KB'
amstrad['description']['model'] = 'CPC6128'
cpc6128_data = copy.deepcopy(amstrad)