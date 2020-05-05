import pyrebase

class Storage:
    def __init__(self):
        print('[INFO] Initializing Storage')
        
        self.FIREBASE_CONFIG = {
            "apiKey": "AIzaSyBWm3BStpa73uv9d45sLnYCyxQ6iOrlT5U",
            "authDomain": "imagine-cab17.firebaseapp.com",
            "databaseURL": "https://imagine-cab17.firebaseio.com",
            "storageBucket": "imagine-cab17.appspot.com"
        }
        
        self.CoverImagePath = 'Event/{}/CoverImages'
        self.ImagePath = 'Event/{}/Images'
        self.STORAGE_CLIENT = pyrebase.initialize_app(self.FIREBASE_CONFIG).storage()

        print('[INFO] Initialed Storage')
        super().__init__()

    def upload_cover_blob(self, source_file_name, eventId, seq_number):
        destination_blob_path = self.CoverImagePath.format(eventId)
        destination_blob_name = f'{destination_blob_path}/img{seq_number}.jpg'
        uploaded_file_json = self.STORAGE_CLIENT.child(destination_blob_name).put(source_file_name)
        print(f'File {source_file_name.filename} uploaded to {destination_blob_name}.')

        return self.STORAGE_CLIENT.child(destination_blob_name).get_url(uploaded_file_json['downloadTokens'])

    def upload_images_blob(self, source_file_names, eventId, seq_number):
        urls = []
        destination_blob_path = self.ImagePath.format(eventId)

        for image in source_file_names:
            seq_number += 1
            destination_blob_name = f'{destination_blob_path}/img{seq_number}.jpg'
            uploaded_file_json = self.STORAGE_CLIENT.child(destination_blob_name).put(image)
            print(f'File {image.filename} uploaded to {destination_blob_name}.')
            urls.append(self.STORAGE_CLIENT.child(destination_blob_name).get_url(uploaded_file_json['downloadTokens']))
    
        return urls