$('body').on('click', 'img', function() {
    $('#image-modal').modal();  
    $('#js-image-modal').attr('src', $('#'+this.id).attr('src'))
})