window.onload = function() {
    $('#loader-spin').fadeOut(400, function() {
        $('#content-loader').fadeIn();
    });   
}

$('eventForm').submit(function() {
    $('#content-loader').fadeOut(400, function() {
        $('#loader-spin').fadeIn();
    })
})