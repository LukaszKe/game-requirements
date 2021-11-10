const game = JSON.parse(eel.getGameByTitle())

document.getElementById('gameImage').src = game.header_image;
document.getElementById('gameTitle').innerHTML = game.name;
document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0] : '';
document.getElementById('gameYear').innerHTML = game.release_date;

const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    const game = eel.getGameByTitle(gameTitle);
    updatePage(game);
};

const updatePage = (game) => {
    document.getElementById('gameImage').src = game.header_image;
    document.getElementById('gameTitle').innerHTML = game.name;
    document.getElementById('gameGenre').innerHTML = game.categories.length > 0 ? game.categories[0] : '';
    document.getElementById('gameYear').innerHTML = game.release_date;
}

const showGameDetails = () => {
    window.location.href = '/final_page.html';
};