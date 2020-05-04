let fileImages = '#add-images';
let secondImage = '#second-image-files';
let gallery = document.getElementById('image-gallery');

$(document).ready(function() {
    $(fileImages).change(function() {
        let files = this.files;

        $(secondImage).remove();
        while (gallery.hasChildNodes()) {
            gallery.removeChild(gallery.firstChild);
        }
        
        $(fileImages).clone()
                    .prop('id', 'second-image-files')
                    .prop('name', 'secondEventImages')
                    .addClass('d-none')
                    .appendTo("#eventForm");

        for (var i = 0; i < files.length; i++) {
            var fileReader = new FileReader();
            fileReader.onloadend = function(e) {
                var image = document.createElement('img');
                image.height = "100";
                image.align = "middle";
                image.src = e.target.result;
                gallery.appendChild(image);
            }
            fileReader.readAsDataURL(files[i]);
        }
    })
})