$('body').on('click','img',function() {
    $('#image-modal').modal();
    $('#js-image-modal').src = this.src;
})