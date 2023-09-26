#!/usr/bin/node

// import the module
const request = require('request');

// The first argument is the API URL
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Make an HTTP GET request to the API
request(apiUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
