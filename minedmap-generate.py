import subprocess
import sys

# •••••••••••••••••••••••••••••••••••••••
print('\n--------------------')
print('1• Entrer le lien vers le dossier contenant MinedMap:')
# MinedMap = input()
MinedMap = '/mnt/d/Developpement/GitHub/Website/mbu-amethyst/carte/MinedMap/custom-1.19'

print('\n--------------------')
print('2• Entrer le lien vers le dossier de la map minecraft:')
# pathMap = input()
pathMap = '/mnt/d/Downloads/MBU Tetrago 2024-03-15/acacb4d8-660d-46a2-b63a-9b95931e3f0d/MBU S2 Tetrago'

print('\n--------------------')
print('3• Entrer le lien vers le dossier ou sera généré la cartographie:')
# pathExport = input()
pathExport = '/mnt/d/Developpement/GitHub/Website/mbu-amethyst/carte/data_new'


# •••••••••••••••••••••••••••••••••••••••
# ./MinedMap "/path/to/save/game" "/path/to/viewer/data"
def generate(exe, src, export):
	subprocess.call([f'{exe}', src, export])


# •••••••••••••••••••••••••••••••••••••••
# Nether
print('\n--------------------')
print('Nether\n')
generate(f'{MinedMap}/MinedMap-Nether', f'{pathMap}/DIM-1', f'{pathExport}/nether')

# Toit du Nether
print('\n--------------------')
print('Nether Toit\n')
generate(f'{MinedMap}/MinedMap', f'{pathMap}/DIM-1', f'{pathExport}/nether_toit')

# The End
print('\n--------------------')
print('Endrya\n')
generate(f'{MinedMap}/MinedMap', f'{pathMap}/DIM1', f'{pathExport}/endrya')

# Aegol
print('\n--------------------')
print('Aegol\n')
generate(f'{MinedMap}/MinedMap', f'{pathMap}/dimensions/mbu/aegol', f'{pathExport}/aegol')

# Skyslands
print('\n--------------------')
print('Skyslands\n')
generate(f'{MinedMap}/MinedMap', f'{pathMap}/dimensions/minecraft/islands_overworld', f'{pathExport}/skyslands')

# Tetrago
print('\n--------------------')
print('Tetrago\n')
generate(f'{MinedMap}/MinedMap', pathMap, f'{pathExport}/tetrago')