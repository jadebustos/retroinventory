import copy

from data import *

amstrad = copy.deepcopy(data)

# default data is loaded

# amstrad data
amstrad['description']['manufacturer'] = 'Amstrad'

# cpc464
amstrad['specs'] = hw_data.copy()
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['rom'] = '32 KB'
amstrad['description']['model'] = 'CPC464'
cpc464_data = copy.deepcopy(amstrad)

# cpc664
amstrad['specs'] = hw_data.copy()
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['rom'] = '48 KB'
amstrad['description']['model'] = 'CPC664'
cpc664_data = copy.deepcopy(amstrad)

# cpc6128
amstrad['specs'] = hw_data.copy()
amstrad['specs']['cpuspeed'] = '4 MHz'
amstrad['specs']['ram'] = '128 KB'
amstrad['specs']['rom'] = '48 KB'
amstrad['description']['model'] = 'CPC6128'
cpc6128_data = copy.deepcopy(amstrad)