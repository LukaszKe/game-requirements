var update_view = async function (components, game) {
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;

    document.getElementById('userProcessor').innerHTML = components.cpu;
    document.getElementById('userGraphics').innerHTML = components.gpu;
    document.getElementById('userMemory').innerHTML = components.ram;
    document.getElementById('userSpace').innerHTML = components.space;

    if (game.hasOwnProperty('minimal_requirements')) {
        document.getElementById('minimalProcessor').innerHTML = game.minimal_requirements.cpu;
        document.getElementById('minimalGraphics').innerHTML = game.minimal_requirements.gpu;
        document.getElementById('minimalMemory').innerHTML = game.minimal_requirements.ram;
        document.getElementById('minimalSpace').innerHTML = game.minimal_requirements.space;
    }

    if (game.hasOwnProperty('recommended_requirements')) {
        document.getElementById('recommendedProcessor').innerHTML = game.recommended_requirements.cpu;
        document.getElementById('recommendedGraphics').innerHTML = game.recommended_requirements.gpu;
        document.getElementById('recommendedMemory').innerHTML = game.recommended_requirements.ram;
        document.getElementById('recommendedSpace').innerHTML = game.recommended_requirements.space;
    }
}

var get_user_components = function () {
    const user_components = eel.get_user_components();
    const game = eel.get_game_by_title();

    update_view(user_components, game);
}

get_user_components();