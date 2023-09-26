#!/usr/bin/node

// import the module
const request = require('request');

// The first argument is the API URL
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Make an HTTP GET request to the API
let movies = 0;
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
