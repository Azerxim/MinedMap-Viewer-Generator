import os, sys, subprocess
import datetime as dt, time
from core import utils, file, mef

# •••••••••••••••••••••••••••••••••••••••
# ./MinedMap "/path/to/save/game" "/path/to/viewer/data"
def generate(exe, src, export):
    subprocess.call([f'{exe}', src, export])

# •••••••••••••••••••••••••••••••••••••••
def builder_menu(name, maps):
    export = ""
    for one in maps:
        if one != "date":
            for map in maps[one]:
                mapname = mef.MEF(map, 'nether:surface', 'nether')
                color = 'smoothwhite'
                if map == name:
                    color = 'ultradarkblue'
                export += f'<a href="{maps[one][map]}" class="menu-button button is-TD-{color}">{mapname}</a>\n'
    return export


# •••••••••••••••••••••••••••••••••••••••
MinedMap = 'MinedMap'
pathMap = None
pathExport = utils.export_folder
maps = export_maps = {
    'vanilla': {
        'overworld': "",
        'nether:surface': "",
        'nether:toit': "",
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
    print('Entrer le lien vers le dossier de la map minecraft:')
    pathMap = mef.WSL(pathMap)
    print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathMap}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    # print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    # print(f'{utils.bcolors.purple}CONFIG{utils.bcolors.RESET}{utils.bcolors.RESET}')
    # print('Entrer le lien vers le dossier ou sera généré la cartographie:')
    pathExport=mef.WSL(pathExport, utils.export_folder)
    # print(f'{utils.bcolors.blue}RESULT{utils.bcolors.RESET}    {pathExport}{utils.bcolors.RESET}')

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
    maps['vanilla']['nether:toit'] = maps['vanilla']['nether:surface'] = f'{pathMap}/DIM-1'
    file.copy(f'"{pathLevel}"', f'"{maps["vanilla"]["nether:surface"]}/level.dat"')
    print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        Nether{utils.bcolors.RESET}')

    # The End
    maps['vanilla']['end'] = f'{pathMap}/DIM1'
    file.copy(f'"{pathLevel}"', f'"{maps["vanilla"]["end"]}/level.dat"')
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
            file.copy(f'"{pathLevel}"', f'"{pathDC}/{one}/{two}/level.dat"')
            print(f'{utils.bcolors.green}OK{utils.bcolors.RESET}        {one}:{two}{utils.bcolors.RESET}')

    # •••••••••••••••••••••••••••
    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    print(f'{utils.bcolors.purple}VIEWER{utils.bcolors.RESET}    Creation du viewer{utils.bcolors.RESET}')
    file.copy_dir('viewer_template/*', f'viewer/')
    time.sleep(6)

    # •••••••••••••••••••••••••••
    for one in maps:
        if one != "date":
            for map in maps[one]:
                print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
                print(f'{utils.bcolors.purple}GENERATE{utils.bcolors.RESET}  {map}{utils.bcolors.RESET}')
                exe = 'MinedMap-2.2.0'
                if ':surface' in map:
                    exe = '1.19/Nether'
                name = mef.MEF(map, 'nether:toit', 'nether_toit')
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
    export_maps = file.json_read(f'{pathExport}/maps.json')

    print(f'{utils.bcolors.white}------------------------------{utils.bcolors.RESET}')
    for one in export_maps:
        if one != "date":
            for map in export_maps[one]:
                name = mef.MEF(map, 'nether:toit', 'nether_toit')
                name = mef.MEF(name, 'nether:surface', 'nether')
                name = mef.MEF(name, ':', '_')
                print(f'{utils.bcolors.purple}VIEWER{utils.bcolors.RESET}    Creation de viewer/{name}.html{utils.bcolors.RESET}')
                file.copy('viewer/index.html', f'viewer/{name}.html')
                time.sleep(2)
                f = file.open_read(f'viewer/{name}.html')
                datas = f.readlines()
                f.close()
                data = ''
                for line in datas:
                    modif_line = line
                    if '<date></date>' in line:
                        modif_line = mef.MEF(modif_line, '<date></date>', f'<span class="menu-date">{export_maps["date"]}</span>')
                    
                    if '<menu></menu>' in line:
                        modif_line = mef.MEF(modif_line, '<menu></menu>', builder_menu(map, export_maps))
                    data += modif_line
                if data != '':
                    file.write(f'viewer/{name}.html', data)
    file.copy('viewer/overworld.html', 'viewer/index.html')

