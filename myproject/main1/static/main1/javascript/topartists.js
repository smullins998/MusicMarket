const searchInput = document.getElementById('search-input');
const autocompleteSuggestions = document.getElementById('autocomplete-suggestions');
const searchResultsContainer = document.getElementById('search-results');

searchInput.addEventListener('input', debounce(searchArtists, 300));

async function searchArtists() {
    const query = searchInput.value.trim();
    searchResultsContainer.innerHTML = '';

    if (query.length < 0) {
        // Clear previous results if the query is too short
        searchResultsContainer.innerHTML = '';
        searchResultsContainer.style.display = 'none';

        return;
    }

    try {
        const response = await fetch(`/api/top_artists/?query=${query}`);
        const data = await response.json();
        searchResultsContainer
        if (response.ok) {
            const resultsList = document.createElement('ul');

            data.forEach(artist => {
                const listItem = document.createElement('li');
                listItem.textContent = artist;
                resultsList.appendChild(listItem);
            });

            // Clear previous results and append the new results to the container
            searchResultsContainer.innerHTML = '';
            searchResultsContainer.appendChild(resultsList);
            searchResultsContainer.style.display = 'block';

        } else {
            console.error('API request failed');
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

// Debounce function remains the same
function debounce(func, delay) {
    let timeoutId;
    return function () {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            func.apply(this, arguments);
        }, delay);
    };
}


// To go to each artists page upon a click
const searchResults = document.getElementById('search-results');

searchResults.addEventListener('click', (event) => {
    const clickedItem = event.target;
    if (clickedItem.tagName === 'LI') {
        // Get the artist's name from the clicked item
        const artistName = clickedItem.textContent;

        // Construct the artist's page URL
        const artistPageUrl = `/artist/${artistName}/`;

        // Navigate to the artist's page
        window.location.href = artistPageUrl;1
    }
});