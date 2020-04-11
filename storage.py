from google.cloud import storage
from db import Db

def upload_cover_blob(bucket_name, source_file_name, destination_blob_path): 
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = f'''{destination_blob_path}/coverimg'''
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name.filename)
    blob.make_public()

    print(
        "File {} uploaded to {}.".format(
            source_file_name.filename, destination_blob_name
        )
    )

    return blob.public_url


def upload_images_blob(bucket_name, source_file_names, destination_blob_path, eventId):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    urls = []
    seq_number = Db().getSeqNumber(eventId)
    for image in source_file_names:
        seq_number += 1

        destination_blob_name = f'''{destination_blob_path}/img{seq_number}'''
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(image.filename)
        blob.make_public()
        urls.append(blob.public_url)

        print(
            "File {} uploaded to {}.".format(
                image.filename, destination_blob_name
            )
        )
    
    return urls
