const search = () => {
    let gameTitle = document.getElementById('gameInput').value;
    eel.postGameTitle(gameTitle);
    window.location.href = '/result_page.html';
};