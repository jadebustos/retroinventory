import modules.amstrad
import modules.atari
import modules.commodore
import modules.msx
import modules.sinclair

# Families
families = {}

# MSX
families['MSX'] = {}
families['MSX']['MSX'] = modules.msx.msx_data.copy()
families['MSX']['MSX2'] = modules.msx.msx2_data.copy()
families['MSX']['MSX2+'] = modules.msx.msx2plus_data.copy()
families['MSX']['TurboR'] = modules.msx.msxtr_data.copy()
families['MSX']['MSXVR'] = modules.msx.msxvr_data.copy()

# Sinclair
families['Sinclair'] = {}
families['Sinclair']['ZX80'] = modules.sinclair.zx80_data.copy()
families['Sinclair']['ZX81'] = modules.sinclair.zx81_data.copy()
families['Sinclair']['ZX-Spectrum'] = modules.sinclair.zxspectrum_data.copy()
families['Sinclair']['Sinclair-QL'] = modules.sinclair.ql_data.copy()
families['Sinclair']['ZX-Spectrum-+128'] =  modules.sinclair.zx128_data.copy()
families['Sinclair']['ZX-Spectrum-128+2'] =  modules.sinclair.zx128_2_data.copy()
families['Sinclair']['ZX-Spectrum-128+3'] =  modules.sinclair.zx128_3_data.copy()
families['Sinclair']['ZX-Spectrum-+128'] =  modules.sinclair.zx128_data.copy()

# Commodore
families['Commodore'] = {}
families['Commodore']['VIC-20'] = modules.commodore.vic20_data.copy()
families['Commodore']['16'] = modules.commodore.c16_data.copy()
families['Commodore']['C64'] =  modules.commodore.c64_data.copy()
families['Commodore']['C128'] = modules.commodore.c128_data.copy()
families['Commodore']['Amiga'] = modules.commodore.amiga_data.copy()

# Amstrad
families['Amstrad'] = {}
families['Amstrad']['CPC464'] = modules.amstrad.cpc464_data.copy()
families['Amstrad']['CPC664'] = modules.amstrad.cpc664_data.copy()
families['Amstrad']['CPC6128'] = modules.amstrad.cpc6128_data.copy()

# Atari
families['Atari'] = {}
families['Atari']['Atari-800'] = modules.atari.atari_800_data.copy()
families['Atari']['Atari-1040'] = modules.atari.atari_1040_data.copy()