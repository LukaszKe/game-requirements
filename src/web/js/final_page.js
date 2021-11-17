var update_view = function (components, game) {
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0]['description'] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;

    document.getElementById('userProcessor').innerHTML = components.cpu;
    document.getElementById('userGraphics').innerHTML = components.gpu;
    document.getElementById('userMemory').innerHTML = 'Ram: ' + components.ram;
    document.getElementById('userSpace').innerHTML = 'Disk space: ' + components.free_space;

    if (game.hasOwnProperty('pc_requirements_minimum')) {
        document.getElementById('minimalProcessor').innerHTML = game.pc_requirements_minimum.cpu;
        document.getElementById('minimalGraphics').innerHTML = game.pc_requirements_minimum.gpu;
        document.getElementById('minimalMemory').innerHTML = game.pc_requirements_minimum.ram;
        document.getElementById('minimalSpace').innerHTML = game.pc_requirements_minimum.free_space;
    }

    if (game.hasOwnProperty('pc_requirements_recommended')) {
        document.getElementById('recommendedProcessor').innerHTML = game.pc_requirements_recommended.cpu;
        document.getElementById('recommendedGraphics').innerHTML = game.pc_requirements_recommended.gpu;
        document.getElementById('recommendedMemory').innerHTML = game.pc_requirements_recommended.ram;
        document.getElementById('recommendedSpace').innerHTML = game.pc_requirements_recommended.free_space;
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