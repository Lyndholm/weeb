function toggleFavorite(artworkId) {
    var button = document.getElementById('favoriteButton' + artworkId);
    var isFavored = button.classList.contains('remove');

    if (isFavored) {
        removeFromFavorites(artworkId);
    } else {
        addToFavorites(artworkId);
    }
}

function addToFavorites(artworkId) {
    fetch(`/artwork/${artworkId}/favorite/`, { method: "GET" })
        .then(response => {
            if (response.ok) {
            } else {
            }
        })
        .catch(error => {
        });

    var button = document.getElementById('favoriteButton' + artworkId);
    button.classList.remove('add');
    button.classList.add('remove');
    button.innerText = '💔';
}

function removeFromFavorites(artworkId) {
    fetch(`/artwork/${artworkId}/unfavorite/`, { method: "GET" })
        .then(response => {
            if (response.ok) {
            } else {
            }
        })
        .catch(error => {
        });

    var button = document.getElementById('favoriteButton' + artworkId);
    button.classList.remove('remove');
    button.classList.add('add');
    button.innerText = '❤';
}