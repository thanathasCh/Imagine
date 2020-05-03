$(document).ready(function() {
    let isAdmin = $('#is-admin').val()
    if (isAdmin === 'False') {
        $('.restricted-content').each(function() {
            $(this).addClass('d-none');
        })   
    }
})