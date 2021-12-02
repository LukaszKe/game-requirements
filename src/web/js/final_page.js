var update_view = function (components, game) {
    if (game.runs === true) {
        document.getElementById('doesGameWork').innerHTML = "This game will run!";
        document.getElementById('doesGameWork').style = "color:#0c7e0c"
    } else if (game.runs === false) {
        document.getElementById('doesGameWork').innerHTML = "This game won't run";
        document.getElementById('doesGameWork').style = "color:#ff0000"
    }
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0]['description'] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;

    document.getElementById('userProcessor').innerHTML = 'CPU: ' + components.cpu;
    document.getElementById('userGraphics').innerHTML = 'GPU: ' + components.gpu;
    document.getElementById('userMemory').innerHTML = 'Ram: ' + components.ram + ' GB';
    document.getElementById('userSpace').innerHTML = 'Disk space: ' + components.free_space + ' GB';

    if (game.hasOwnProperty('pc_requirements_minimum')) {
        min_req = game.pc_requirements_minimum
        if (min_req.gpu_ok === true) {
            document.getElementById('minimalProcessor').style = "color:#0c7e0c"
        } else if (min_req.gpu_ok === false) {
            document.getElementById('minimalProcessor').style = "color:#ff0000"
        }
        if (min_req.cpu_ok === true) {
            document.getElementById('minimalGraphics').style = "color:#0c7e0c"
        } else if (min_req.cpu_ok === false) {
            document.getElementById('minimalGraphics').style = "color:#ff0000"
        }
        if (min_req.ram_ok === true) {
            document.getElementById('minimalMemory').style = "color:#0c7e0c"
        } else if (min_req.ram_ok === false) {
            document.getElementById('minimalMemory').style = "color:#ff0000"
        }
        if (min_req.free_space_ok === true) {
            document.getElementById('minimalSpace').style = "color:#0c7e0c"
        } else if (min_req.free_space_ok === false) {
            document.getElementById('minimalSpace').style = "color:#ff0000"
        }
        document.getElementById('minimalProcessor').innerHTML = 'CPU: ' + game.pc_requirements_minimum.cpu;
        document.getElementById('minimalGraphics').innerHTML = 'GPU: ' + game.pc_requirements_minimum.gpu;
        document.getElementById('minimalMemory').innerHTML = 'Ram: ' + game.pc_requirements_minimum.ram + ' GB';
        document.getElementById('minimalSpace').innerHTML = 'Disk space: ' + game.pc_requirements_minimum.free_space + ' GB';
    }

    if (game.hasOwnProperty('pc_requirements_recommended')) {
        rec_req = game.pc_requirements_recommended
        if (rec_req.gpu_ok === true) {
            document.getElementById('recommendedProcessor').style = "color:#0c7e0c"
        } else if (rec_req.gpu_ok === false) {
            document.getElementById('recommendedProcessor').style = "color:#ff0000"
        }
        if (rec_req.cpu_ok === true) {
            document.getElementById('recommendedGraphics').style = "color:#0c7e0c"
        } else if (rec_req.cpu_ok === false) {
            document.getElementById('recommendedGraphics').style = "color:#ff0000"
        }
        if (rec_req.ram_ok === true) {
            document.getElementById('recommendedMemory').style = "color:#0c7e0c"
        } else if (rec_req.ram_ok === false) {
            document.getElementById('recommendedMemory').style = "color:#ff0000"
        }
        if (rec_req.free_space_ok === true) {
            document.getElementById('recommendedSpace').style = "color:#0c7e0c"
        } else if (rec_req.free_space_ok === false) {
            document.getElementById('recommendedSpace').style = "color:#ff0000"
        }
        document.getElementById('recommendedProcessor').innerHTML = 'CPU: ' + game.pc_requirements_recommended.cpu;
        document.getElementById('recommendedGraphics').innerHTML = 'GPU: ' + game.pc_requirements_recommended.gpu;
        document.getElementById('recommendedMemory').innerHTML = 'Ram: ' + game.pc_requirements_recommended.ram + ' GB';
        document.getElementById('recommendedSpace').innerHTML = 'Disk space: ' + game.pc_requirements_recommended.free_space + ' GB';
    } else {
        document.getElementById('recommendedProcessor').innerHTML = 'Not found'
    }
}

var get_user_components = async function () {
    const user_components = await eel.get_user_components()();
    await eel.get_game_by_title()(x => {
        const game = JSON.parse(x)
        update_view(JSON.parse(user_components), game);
    });
}

get_user_components();