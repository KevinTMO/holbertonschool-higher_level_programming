$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $.map(data, function (value, key) {
    if (key === 'hello') { $('#hello').html(value); }
  });
});
