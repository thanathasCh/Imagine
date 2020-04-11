from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    # i = 0
    # for image in images:
    #     destination = f'''destination_blob_name{i}'''
    #     blob = bucket.blob(destination)
    #     blob.upload_from_filename(image)
    #     blob.make_public()
    #     print(
    #         "File {} uploaded to {}.".format(
    #             image, destination_blob_name
    #         )
    #     )
    #     i += 1
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

    return blob.public_url

images = ['image.png','images2.jpg']
upload_blob('eventimagefilter',images,'Event/EventA/Images/aaa')