$(document).ready(function() {
    let preview = document.getElementById('user-gallery');
    let video = document.getElementById("vid-show"),
        take = document.getElementById("vid-take"),
        imageList = [];

    navigator.mediaDevices.getUserMedia({
            video: true
        })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();

            take.addEventListener("click", function () {
                var canvas = document.createElement("canvas");
                canvas.width = 480;
                canvas.height = 360;
                var context2D = canvas.getContext("2d");
                context2D.drawImage(video, 0, 0, 480, 360);
                var image = new Image();
                image.height = 150;
                image.src = canvas.toDataURL();
                preview.appendChild(image);
                // imageList add image url (base64)
                imageList.push(image.src);
            });
        })
        .catch(function (err) {
            document.getElementById('vid-controls').innerHTML =
                "Please enable access and attach a camera";
        });

    $('#confirm-button').on('click', function () {
        if (imageList.length > 0) {
            $.post("/processImage", {
                'userImages[]': imageList,
                'eventId': $('#eventId').val()
            });
        } else {
            alert("Images or files are missing.");
        }
    })

    $('#user-image').change(function() {
        var files = document.getElementById('user-image').files;

        function readAndPreview(file) {
            var reader = new FileReader();
            reader.addEventListener("load", function () {
                var image = new Image();
                image.height = 150;
                image.title = file.name;
                image.src = this.result;
                preview.appendChild(image);
                // imageList add image url (base64)
                imageList.push(this.result);
            }, false);
            reader.readAsDataURL(file);
        }
        if (files) {
            [].forEach.call(files, readAndPreview);
        }
    })
})