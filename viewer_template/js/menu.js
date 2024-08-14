async function BuildDate() {
    const response = await fetch("data/maps.json", {cache: 'no-store'});
	const maps_data = await response.json();
    // console.log(maps_data);
    const maps_date = document.getElementById("maps_date");
    const txt = document.createTextNode(maps_data.date);
    maps_date.appendChild(txt);
}

async function BuildMenu() {
    const pathname = parsePathName();
    const hash = parseHash();
    const maps = await fetch("data/maps.json", {cache: 'no-store'});
	const maps_data = await maps.json();
    const maps_menu = document.getElementById("Menu");

    for (var key in maps_data.vanilla) {
        var a = document.createElement('a');
        var txt = document.createTextNode(key);
        a.appendChild(txt);
        a.href = maps_data.vanilla[key];
        if (pathname.file) {
            a.href += '-' + pathname.file
        }
        if (pathname.option) {
            a.href += '-' + pathname.option
        }
        if (maps_data.vanilla[key] == pathname.data) {
            a.className = 'menu-button button is-TD-ultradarkblue';
        }
        else {
            a.className = 'menu-button button is-TD-smoothwhite';
        }
        maps_menu.appendChild(a);
    }

    for (var key in maps_data.dimensions) {
        var a = document.createElement('a');
        var txt = document.createTextNode(key);
        a.appendChild(txt);
        a.href = maps_data.dimensions[key];
        if (pathname.file) {
            a.href += '-' + pathname.file
        }
        if (pathname.option) {
            a.href += '-' + pathname.option
        }
        if (maps_data.dimensions[key] == pathname.data) {
            a.className = 'menu-button button is-TD-ultradarkblue';
        }
        else {
            a.className = 'menu-button button is-TD-smoothwhite';
        }
        maps_menu.appendChild(a);
    }
}

async function BuildOptions() {
    const pathname = parsePathName();
    const hash = parseHash();
    const response = await fetch("options.json", {cache: 'no-store'});
	const options_data = await response.json();
    const option_div = document.getElementById("Options");

    if (isNaN(hash.zoom))
        hash.zoom = 0;
    if (isNaN(hash.x))
        hash.x = spawn.x;
    if (isNaN(hash.z))
        hash.z = spawn.z;

    for (var key in options_data['options']) {
        if (!options_data['options'][key].hidden) {
            var a = document.createElement('a');
            var i = document.createElement('i');
            var span = document.createElement('span');
            var txt = document.createTextNode(options_data['options'][key].title);
            span.appendChild(txt)

            // <a> classname
            a.className = 'menu-button-option button gap-5'
            if (key == pathname.option || key == pathname.file) {
                a.className += ' is-TD-ultradarkblue';
            }
            else {
                a.className += ' is-TD-smoothwhite';
            }

            // <a> href
            a.href = pathname.data
            if ((key == 'embed' || key == 'editor')) {
                if (pathname.file != key) {
                    a.href += '-' + key;
                }
                if (pathname.option != '') {
                    a.href += '-' + pathname.option;
                }
            }
            if ((key != 'embed' && key != 'editor')) {
                if (pathname.file != '') {
                    a.href += '-' + pathname.file;
                }
                
                if (pathname.option != key) {
                    a.href += '-' + key;
                }
            }
            a.href += '#x='+hash.x+'&z='+hash.z;

            if (hash.zoom != 0) {
                a.href += '&zoom='+hash.zoom;
            }

            // <a> style
            a.style = 'justify-content: start';

            a.id = 'Option_'+key;

            // build button
            if (options_data['options'][key].icon) {
                i.className = options_data['options'][key].icon;
                a.appendChild(i);
            }
            a.appendChild(span);
            option_div.appendChild(a);
        }
    }
}

async function updateOptions() {
    const pathname = parsePathName();
    const hash = parseHash();
    const response = await fetch("options.json", {cache: 'no-store'});
	const options_data = await response.json();
    let a;

    if (isNaN(hash.zoom))
        hash.zoom = 0;
    if (isNaN(hash.x))
        hash.x = spawn.x;
    if (isNaN(hash.z))
        hash.z = spawn.z;
    
    for (var key in options_data['options']) {
        if (!options_data['options'][key].hidden) {
            a = document.getElementById('Option_'+key);
            // <a> href
            a.href = pathname.data
            if ((key == 'embed' || key == 'editor')) {
                if (pathname.file != key) {
                    a.href += '-' + key;
                }
                if (pathname.option != '') {
                    a.href += '-' + pathname.option;
                }
            }
            if ((key != 'embed' && key != 'editor')) {
                if (pathname.file != '') {
                    a.href += '-' + pathname.file;
                }
                
                if (pathname.option != key) {
                    a.href += '-' + key;
                }
            }
            a.href += '#x='+hash.x+'&z='+hash.z;

            if (hash.zoom != 0) {
                a.href += '&zoom='+hash.zoom;
            }
        }
    }
}



async function BuildButtons() {
    const response = await fetch("options.json", {cache: 'no-store'});
	const options_data = await response.json();
    const option_div = document.getElementById("OptionsButtons");

    for (var key in options_data['buttons']) {
        if (!options_data['buttons'][key].hidden) {
            var a = document.createElement('a');
            var i = document.createElement('i');
            var span = document.createElement('span');
            var txt = document.createTextNode(options_data['buttons'][key].title);
            span.appendChild(txt)

            // <a> classname
            a.className = 'menu-button-option button gap-5 is-TD-smoothwhite';

            // <a> href
            a.href = options_data['buttons'][key].href;
            if (options_data['buttons'][key].target != '') {
                a.target = options_data['buttons'][key].target;
            }

            // <a> style
            a.style = 'justify-content: start'

            // build button
            if (options_data['buttons'][key].icon) {
                i.className = options_data['buttons'][key].icon
                a.appendChild(i)
            }
            a.appendChild(span)
            option_div.appendChild(a)
        }
    }
}