import os, sys, subprocess
from core import utils, file, mef

# •••••••••••••••••••••••••••••••••••••••
def copy(source, destination):
    os.popen(f'cp {source} {destination}')

# •••••••••••••••••••••••••••••••••••••••
# ./MinedMap "/path/to/save/game" "/path/to/viewer/data"
def generate(exe, src, export):
	subprocess.call([f'{exe}', src, export])


# •••••••••••••••••••••••••••••••••••••••
MinedMap = 'MinedMap-Legacy/1.19'
pathMap = pathExport = None
maps = {
    'vanilla': {
        'overworld': "",
        'nether': "",
        'end': ""
    },
    'dimensions': {}
}


# •••••••••••••••••••••••••••••••••••••••
if __name__ == "__main__":

    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      {utils.NAME}{utils.bcolors.RESET}')
    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      Author: {utils.bcolors.purple}{utils.AUTHOR}{utils.bcolors.RESET}')
    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      Version: {utils.bcolors.purple}{utils.VERSION}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}CONFIG{utils.bcolors.RESET}{utils.bcolors.RESET}')
    print('Entrer le lien vers le dossier de la map minecraft:')
    pathMap = mef.WSL(pathMap)
    print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathMap}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}CONFIG{utils.bcolors.RESET}{utils.bcolors.RESET}')
    print('Entrer le lien vers le dossier ou sera généré la cartographie:')
    pathExport=mef.WSL(pathExport, utils.export_folder)
    print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathExport}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}INFO{utils.bcolors.RESET}      Conversion de la sauvegarde{utils.bcolors.RESET}')
    if file.exist(f'{pathMap}/level.dat'):
        pathLevel = f'{pathMap}/level.dat'
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        level.dat récupéré{utils.bcolors.RESET}')
    else:
        print(f'{utils.bcolors.red}ERROR{utils.bcolors.RESET}     Le fichier level.dat est manquant{utils.bcolors.RESET}')
        exit()
    
    # Overworld
    maps['vanilla']['overworld'] = pathMap
    print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Overworld{utils.bcolors.RESET}')

    # Nether
    maps['vanilla']['nether:*'] = maps['vanilla']['nether'] = f'{pathMap}/DIM-1'
    copy(f'"{pathLevel}"', f'"{maps["vanilla"]["nether"]}/level.dat"')
    print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Nether{utils.bcolors.RESET}')

    # The End
    maps['vanilla']['end'] = f'{pathMap}/DIM1'
    copy(f'"{pathLevel}"', f'"{maps["vanilla"]["end"]}/level.dat"')
    print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        End{utils.bcolors.RESET}')

    # Dimensions custom
    print(f'{utils.bcolors.purple}INFO{utils.bcolors.RESET}      Dimension custom{utils.bcolors.RESET}')
    pathDC = f'{pathMap}/dimensions'
    pathDCs = {}
    for rootdir, dirs, files in os.walk(pathDC):
        parent = mef.MEF(rootdir, f'{pathDC}/', "")
        parentd = parent.split("/")
        for subdir in dirs:
            if subdir == 'region':
                match len(parentd):
                    case 2:
                        maps['dimensions'][f'{parentd[0]}:{parentd[1]}'] = os.path.join(rootdir)
                        try:
                            pathDCs[parentd[0]].append(parentd[1])
                        except:
                            pathDCs[parentd[0]] = []
                            pathDCs[parentd[0]].append(parentd[1])
    if pathDCs is {}:
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Aucune dimension custom{utils.bcolors.RESET}')
    for one in pathDCs:
        for two in pathDCs[one]:
            copy(f'"{pathLevel}"', f'"{pathDC}/{one}/{two}/level.dat"')
            print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        {one}:{two}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    for one in maps:
        for map in maps[one]:
            print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
            print(f'{utils.bcolors.purple}GENERATE{utils.bcolors.RESET}  {map}{utils.bcolors.RESET}')
            exe = 'MinedMap'
            if ':*' in map:
                exe = 'Nether'
            name = mef.MEF(map, ':*', '_toit')
            name = mef.MEF(name, ':', '/')
            if maps[one][map] != '':
                if (not file.exist(f'{pathExport}/{name}')):
                    file.createdir(f'{pathExport}/{name}')
                generate(f'{MinedMap}/{exe}', f'{maps[one][map]}', f'{pathExport}/{name}')