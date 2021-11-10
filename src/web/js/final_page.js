let game = 'dawadw'
eel.get_game_by_title()(x => {
    game = JSON.parse(x)
    console.log(game)
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;

    document.getElementById('minimalProcessor').innerHTML = game.minimal_requirements.cpu;
    document.getElementById('minimalGraphics').innerHTML = game.minimal_requirements.gpu;
    document.getElementById('minimalMemory').innerHTML = game.minimal_requirements.ram;
    document.getElementById('minimalSpace').innerHTML = game.minimal_requirements.space;

    if (game.hasOwnProperty('recommended_requirements')) {
        document.getElementById('recommendedProcessor').innerHTML = game.recommended_requirements.cpu;
        document.getElementById('recommendedGraphics').innerHTML = game.recommended_requirements.gpu;
        document.getElementById('recommendedMemory').innerHTML = game.recommended_requirements.ram;
        document.getElementById('recommendedSpace').innerHTML = game.recommended_requirements.space;
    }
})

