#!/usr/bin/node

// import the module
const request = require('request');

// The first argument is the movie ID
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiurl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Make an HTTP GET request to the API
request(apiurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
