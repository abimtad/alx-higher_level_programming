// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// Using the JQuery API

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json;'
$.get(url, function (data) {
    let films = data.results;
    for (let film of films){
        let element = '<li>${film.title}</li>';
        $('ul#list_movies').append(element);
    }
})