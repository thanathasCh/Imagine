class Event:
    def __init__(self, eventName, description, date, coverImageUrl=None, eventId=0):
        self.eventId = eventId
        self.eventName = eventName
        self.coverImageUrl = coverImageUrl
        self.description = description
        self.date = date

class EventImage:
    def __init__(self, eventName, coverImageUrl, description, date, imageUrls, eventId=0):
        self.eventId = eventId
        self.eventName = eventName
        self.coverImageUrl = coverImageUrl
        self.description = description
        self.date = date
        self.imageUrls = imageUrls

class PreprocessedImage:
    def __init__(self, preprocessedImageUrl, imageId, preprocessedImageId = 0):
        self.imageId = imageId
        self.preprocessedImageUrl = preprocessedImageUrl
        self.preprocessedImageId = preprocessedImageId


