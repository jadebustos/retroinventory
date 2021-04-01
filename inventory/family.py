import atari
import msx

# Families
families = {}

# MSX
families['MSX'] = {}
families['MSX']['MSX'] = msx.msx_data.copy()
families['MSX']['MSX2'] = msx.msx2_data.copy()
families['MSX']['MSX2+'] = msx.msx2plus_data.copy()
families['MSX']['TurboR'] = msx.msxtr_data.copy()
families['MSX']['MSXVR'] = msx.msxvr_data.copy()

# Sinclair
#families['Sinclair'] = {}
#families['Sinclair']['ZX80'] = data
#families['Sinclair']['ZX81'] = data
#families['Sinclair']['ZX-Spectrum'] = data
#families['Sinclair']['Sinclair-QL'] = data
#families['Sinclair']['ZX-Spectrum'] = data
#families['Sinclair']['ZX-Spectrum-128'] = data

# Commodore
#families['Commodore'] = {}
#families['Commodore']['PET'] = data
#families['Commodore']['VIC-20'] = data
#families['Commodore']['16'] = data
#families['Commodore']['C64'] = data
#families['Commodore']['C64C'] = data
#families['Commodore']['C128'] = data
#families['Commodore']['C128D'] = data
#families['Commodore']['Amiga-500'] = data
#families['Commodore']['Amiga-600'] = data
#families['Commodore']['Amiga-1000'] = data
#families['Commodore']['Amiga-1200'] = data

# Amstrad
#families['Amstrad'] = {}
#families['Amstrad']['CPC464'] = data
#families['Amstrad']['CPC472'] = data
#families['Amstrad']['CPC664'] = data
#families['Amstrad']['CPC6128'] = data
#families['Amstrad']['CPC464-Plus'] = data
#families['Amstrad']['CPC6128-Plus'] = data

# Atari
families['Atari'] = {}
families['Atari']['Atari-800'] = atari.atari_800_data.copy()
families['Atari']['Atari-1040'] = atari.atari_1040_data.copy()

# NES
#families['NES'] = {}

# SNES
#families['SNES'] = {}

# Megadrive
#families['Megadrive'] = {}

# Neogeo
#families['Neogeo'] = {}