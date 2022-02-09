$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, movies) {
    $('#list_movies').append('<li>' + movies.title + '</li>');
  });
});
