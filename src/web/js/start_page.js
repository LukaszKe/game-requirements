const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    document.getElementById('spinner').style = 'display:block';
    eel.post_game_title(gameTitle);
    window.location.href = 'result_page.html';
};