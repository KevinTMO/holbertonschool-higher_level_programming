$('#toggle_header').click(function(){
  $('header').hasClass( 'red', function() {
    $('header').addClass('red');
    });
    $('header').hasClass('green', function(){
      $('header').addClass('green');
    });
});

/*

Trying first method if not then use this one:

$(document).ready(function(){
  $("div#toggle_header").click(function() {
    $("header").toggleClass("red");
    $("header").toggleClass("green");
  });
});
*/
