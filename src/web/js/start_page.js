const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    eel.post_game_title(gameTitle);
    window.location.href = 'result_page.html';
};