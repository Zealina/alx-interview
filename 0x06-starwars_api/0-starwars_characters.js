#!/usr/bin/node
const request = require('request');

function fetchMovie (movieId) {
  return new Promise((resolve, reject) => {
    request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

function fetchCharacters (urls) {
  return Promise.all(urls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  }));
}

async function printMovieCharacters (movieId) {
  try {
    const movie = await fetchMovie(movieId);

    const characters = await fetchCharacters(movie.characters);

    console.log(`Characters in ${movie.title}:`);
    characters.forEach(character => {
      console.log(character);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide the Movie ID as a command line argument.');
} else {
  printMovieCharacters(movieId);
}
