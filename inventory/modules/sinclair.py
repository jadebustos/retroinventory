import copy

from data import data

sinclair = copy.deepcopy(data)

# default data is loaded

# sinclair data
sinclair['description']['manufacturer'] = 'Sinclair'

# ZX80
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80'
sinclair['specs']['cpuspeed'] = '3.25 MHz'
sinclair['specs']['ram'] = '1 KB'
sinclair['specs']['rom'] = '4 KB'
sinclair['description']['model'] = 'ZX80'
zx80_data = copy.deepcopy(sinclair)

# ZX81
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80'
sinclair['specs']['cpuspeed'] = '3.25 MHz'
sinclair['specs']['ram'] = '1 KB'
sinclair['specs']['rom'] = '8 KB'
sinclair['description']['model'] = 'ZX80'
zx81_data = copy.deepcopy(sinclair)

# ZX Spectrum
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80A'
sinclair['specs']['cpuspeed'] = '3.25 MHz'
sinclair['specs']['ram'] = '48 KB'
sinclair['specs']['rom'] = '16 KB'
sinclair['description']['model'] = 'ZX Spectrum'
zxspectrum_data = copy.deepcopy(sinclair)

# Sinclair QL
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Motorola'
sinclair['specs']['cpumodel'] = '68008'
sinclair['specs']['cpuspeed'] = '7.5 MHz'
sinclair['specs']['ram'] = '128 KB'
sinclair['specs']['rom'] = '32 KB'
sinclair['description']['model'] = 'Sinclair QL'
ql_data = copy.deepcopy(sinclair)

# ZX Spectrum +128
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80'
sinclair['specs']['cpuspeed'] = '3.5 MHz'
sinclair['specs']['ram'] = '128 KB'
sinclair['specs']['rom'] = '64 KB'
sinclair['description']['model'] = 'ZX Spectrum +128'
zx128_data = copy.deepcopy(sinclair)

# ZX Spectrum 128 +2
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80'
sinclair['specs']['cpuspeed'] = '3.5 MHz'
sinclair['specs']['ram'] = '128 KB'
sinclair['specs']['rom'] = '32 KB'
sinclair['description']['model'] = 'ZX Spectrum 128 +2'
zx128_2_data = copy.deepcopy(sinclair)

# ZX Spectrum 128 +3
sinclair['specs']['cpubits'] = '8'
sinclair['specs']['cpuvendor'] = 'Zilog'
sinclair['specs']['cpumodel'] = 'Z80'
sinclair['specs']['cpuspeed'] = '3.5 MHz'
sinclair['specs']['ram'] = '128 KB'
sinclair['specs']['rom'] = '64 KB'
sinclair['description']['model'] = 'ZX Spectrum 128 +3'
zx128_3_data = copy.deepcopy(sinclair)