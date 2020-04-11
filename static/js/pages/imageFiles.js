let fileImages = $('#add-images');
let posterImage = $('#poster-image');

$(document).ready(function() {
    fileImages.change(function() {
        let files = this.files;
        
        for (var i = 0; i < files.length; i++) {
            var fileReader = new FileReader();
            fileReader.onloadend = function(e) {
                var image = document.createElement('img');
                image.height = "100";
                image.align = "middle";
                image.src = e.target.result;
                document.getElementById('image-gallery').appendChild(image);
            }
            fileReader.readAsDataURL(files[i]);
        }
    })

    // posterImage.change(function() {
    //     let files = this.files;

    //     for (var i = 0; i < files.length; i++) {
    //         var fileReader = new FileReader();
    //         fileReader.onloadend = function(e) {
    //             var image = document.createElement('img');
    //             image.height = "100";
    //             image.align = "middle";
    //             image.src = e.target.result;
    //             document.getElementById('poster-gallery').appendChild(image);
    //         }
    //         fileReader.readAsDataURL(files[i]);
    //     }
    // })
})