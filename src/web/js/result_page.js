
var found_game = false;

function showInfo(game) {
    if (game !== null) {
        document.getElementById('gameImage').src = game.header_image;
        document.getElementById('gameTitle').innerHTML = game.name;
        document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0]['description'] : '';
        document.getElementById('gameYear').innerHTML = game.release_date;
        found_game = true;
    } else {
        document.getElementById('gameTitle').innerHTML = "Niestety nie znaleziono takiej gry";
        found_game = false;
    }
    document.getElementById('spinner').style = 'display:none';
    document.getElementById('gameTile').style = 'display:block';
}

eel.get_game_by_title()(x => {
    let game = JSON.parse(x)
    showInfo(game);
})

const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    document.getElementById('spinner').style = 'display:block';
    document.getElementById('gameTile').style = 'display:none';
    eel.get_game_by_title(gameTitle)(game => {
        updatePage(JSON.parse(game));
    });
};

const updatePage = (game) => {
    showInfo(game);
}

const showGameDetails = () => {
    if (found_game) {
        window.location.href = 'final_page.html';
    }
};