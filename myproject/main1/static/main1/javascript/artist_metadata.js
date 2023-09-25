
console.log('Hi');

async function fetchDataAndDisplay() {
    try {

        const searchInput = document.getElementById('search-input');
        console.log('got input')
        const query = searchInput.value.trim();
        console.log('Query:', query);

        const response = await fetch(`/api/artist_metadata/?query=Drake`);
        console.log('Response status:', response.status);

        const data = await response.json();
        console.log('Data received:', data);

        const artistFollowers = data.artists_data.followers;
        const artistPictures= data.artists_data.pictures;
        const artistUrl= data.artists_data.url;
        const artistGenres= data.artists_data.genres;

        console.log('url', artistUrl);

        // Let's make all of this dynamic content and append to innerhtml
        const url = document.getElementById('appendurl');
        url.href = artistUrl;

        const followers = document.getElementById('artist-followers');
        followers.innerHTML += artistFollowers;

        const genres = document.getElementById('artist-genre');

        for (let i = 0; i < artistGenres.length; i++) {
          const listItem = document.createElement('li');
          listItem.textContent = artistGenres[i];
          genres.appendChild(listItem);
        }
        console.log(artistPictures)
        const images = document.getElementById('artist-image-scr');
        images.src = artistPictures



    } catch (error) {
        console.error('An error occurred:', error);
    }
}

fetchDataAndDisplay()
