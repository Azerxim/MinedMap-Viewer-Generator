import os, sys, subprocess
import datetime as dt, time
from core import utils, file, mef

# •••••••••••••••••••••••••••••••••••••••
# ./MinedMap "/path/to/save/game" "/path/to/viewer/data"
def generate(exe, src, export):
    subprocess.call([f'{exe}', src, export])


# •••••••••••••••••••••••••••••••••••••••
MinedMap = 'MinedMap'
pathMap = None
pathExport = utils.export_folder
maps = export_maps = {
    'vanilla': {
        'overworld': "",
        'nether:surface': "",
        'nether:roof': "",
        'end': ""
    },
    'dimensions': {},
    'date': ''
}


# •••••••••••••••••••••••••••••••••••••••
if __name__ == "__main__":

    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      {utils.NAME}{utils.bcolors.RESET}')
    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      Author: {utils.bcolors.purple}{utils.AUTHOR}{utils.bcolors.RESET}')
    print(f'{utils.bcolors.green}INFO{utils.bcolors.RESET}      Version: {utils.bcolors.purple}{utils.VERSION}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}CONFIG{utils.bcolors.RESET}{utils.bcolors.RESET}')
    print('Enter the link to the minecraft map folder:')
    pathMap = mef.WSL(pathMap)
    print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathMap}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    # print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    # print(f'{utils.bcolors.purple}CONFIG{utils.bcolors.RESET}{utils.bcolors.RESET}')
    # print('Enter the link to the folder where the mapping will be generated:')
    pathExport=mef.WSL(pathExport, utils.export_folder)
    # print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathExport}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}INFO{utils.bcolors.RESET}      Converting the save{utils.bcolors.RESET}')
    print(f'{pathMap}/level.dat')
    if file.exist(f'{pathMap}/level.dat'):
        pathLevel = f'{pathMap}/level.dat'
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        level.dat{utils.bcolors.RESET}')
    else:
        print(f'{utils.bcolors.red}ERROR{utils.bcolors.RESET}     The level.dat file is missing{utils.bcolors.RESET}')
        exit()
    
    # Overworld
    maps['vanilla']['overworld'] = pathMap
    print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Overworld{utils.bcolors.RESET}')

    # Nether
    if file.exist(f'{pathMap}/DIM-1/'):
        maps['vanilla']['nether:roof'] = maps['vanilla']['nether:surface'] = f'{pathMap}/DIM-1'
        file.copy(f'"{pathLevel}"', f'"{maps["vanilla"]["nether:surface"]}/level.dat"')
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Nether{utils.bcolors.RESET}')
    else:
        maps['vanilla']['nether:roof'] = maps['vanilla']['nether:surface'] = ''
        print(f'{utils.bcolors.green}NOK{utils.bcolors.RESET}       Nether{utils.bcolors.RESET}')

    # The End
    if file.exist(f'{pathMap}/DIM1/'):
        maps['vanilla']['end'] = f'{pathMap}/DIM1'
        file.copy(f'"{pathLevel}"', f'"{maps["vanilla"]["end"]}/level.dat"')
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        End{utils.bcolors.RESET}')
    else:
        maps['vanilla']['end'] = ''
        print(f'{utils.bcolors.green}NOK{utils.bcolors.RESET}       End{utils.bcolors.RESET}')

    # Dimensions custom
    print(f'{utils.bcolors.purple}INFO{utils.bcolors.RESET}      Custom Dimensions{utils.bcolors.RESET}')
    pathDC = f'{pathMap}/dimensions'
    pathDCs = {}
    for rootdir, dirs, files in os.walk(pathDC):
        parent = mef.MEF(rootdir, f'{pathDC}/', "")
        parentd = parent.split("/")
        lparentd = len(parentd)
        try:
            for subdir in dirs:
                if subdir == 'region':
                    if (lparentd == 2):
                        maps['dimensions'][f'{parentd[0]}:{parentd[1]}'] = os.path.join(rootdir)
                        try:
                            pathDCs[parentd[0]].append(parentd[1])
                        except:
                            pathDCs[parentd[0]] = []
                            pathDCs[parentd[0]].append(parentd[1])
        except:
            pass
    if pathDCs == {}:
        print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        No custom dimension{utils.bcolors.RESET}')
    for one in pathDCs:
        for two in pathDCs[one]:
            file.copy(f'"{pathLevel}"', f'"{pathDC}/{one}/{two}/level.dat"')
            print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        {one}:{two}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}VIEWER{utils.bcolors.RESET}    Viewer creation{utils.bcolors.RESET}')
    file.copy_dir('viewer_template/*', f'viewer/')
    time.sleep(6)

    # •••••••••••••••••••••••••••
    for one in maps:
        if one != "date":
            for map in maps[one]:
                if map != '':
                    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
                    print(f'{utils.bcolors.purple}GENERATE{utils.bcolors.RESET}  {map}{utils.bcolors.RESET}')
                    exe = 'MinedMap-2.2.0'
                    if ':surface' in map:
                        exe = '1.19/Nether'
                    name = mef.MEF(map, 'nether:roof', 'nether_roof')
                    name = mef.MEF(name, 'nether:surface', 'nether')
                    name = mef.MEF(name, ':', '_')
                    if maps[one][map] != '':
                        if (not file.exist(f'{pathExport}/{name}')):
                            file.createdir(f'{pathExport}/{name}')
                        generate(f'{MinedMap}/{exe}', f'{maps[one][map]}', f'{pathExport}/{name}')
                        export_maps[one][map] = name
    export_maps['date'] = dt.date.today().strftime("%d/%m/%Y")
    file.create(f'{pathExport}/maps.json')
    file.json_write(f'{pathExport}/maps.json', export_maps)

    # •••••••••••••••••••••••••••
    # Viewer builder
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}GENERATE{utils.bcolors.RESET}  {pathExport}/maps.json{utils.bcolors.RESET}')
    export_maps = file.json_read(f'{pathExport}/maps.json')

