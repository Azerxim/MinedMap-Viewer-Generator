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
    const response0 = await fetch("options.json", {cache: 'no-store'});
	const options_data = await response0.json();
    const option_div = document.getElementById("Options");

    for (var key in options_data) {
        if (!options_data[key].hidden) {
            var a = document.createElement('a');
            var i = document.createElement('i');
            var span = document.createElement('span');
            var txt = document.createTextNode(options_data[key].title);
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

            // <a> style
            a.style = 'justify-content: start'

            // build button
            if (options_data[key].icon) {
                i.className = options_data[key].icon
                a.appendChild(i)
            }
            a.appendChild(span)
            option_div.appendChild(a)
        }
    }
}