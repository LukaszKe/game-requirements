let game = 'dawadw'

var found_game = false;
eel.get_game_by_title()(x => {
    if (x !== null) {
        game = JSON.parse(x)
        document.getElementById('gameImage').src = game.header_image;
        document.getElementById('gameTitle').innerHTML = game.name;
        document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0]['description'] : '';
        document.getElementById('gameYear').innerHTML = game.release_date;
        document.getElementById('spinner').style = 'display:none';
        document.getElementById('gameTile').style = 'display:block';
        found_game = true;
    } else {
        document.getElementById('gameTitle').innerHTML = "Niestety nie znaleziono takiej gry";
        found_game = false;
    }


})

const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    eel.get_game_by_title(gameTitle)(game => {
        updatePage(JSON.parse(game));
    });
};

const updatePage = (game) => {
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0]['description'] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;
}

const showGameDetails = () => {
    if (found_game) {
        window.location.href = 'final_page.html';
    }
};