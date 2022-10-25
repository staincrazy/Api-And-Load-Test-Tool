class ActiveFenceApi:
    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint


class TextAsyncAPi(ActiveFenceApi):
    @staticmethod
    def get_textAsyncApi():
        instance = ActiveFenceApi('Text API - Asynchronous', 'https://apis.activefence.com/v2/content/text')
        return instance


class ImageApi(ActiveFenceApi):
    @staticmethod
    def get_imageApi():
        instance = ActiveFenceApi('Image API', 'https://apis.activefence.com/v2/content/image')
        return instance


class TextSyncApi(ActiveFenceApi):
    @staticmethod
    def get_textSyncAPi():
        instance = ActiveFenceApi('Text API - Synchronous', 'https://apis.activefence.com/sync/v2/content/text')
        return instance
