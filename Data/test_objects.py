class TestEndpoint:
    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint


class CatFactsAsyncAPi(TestEndpoint):
    @staticmethod
    def get_randomCatFact():
        instance = TestEndpoint('Cat Facts Endpoint', 'https://catfact.ninja/fact')
        return instance


class ImageApi(TestEndpoint):
    @staticmethod
    def get_imageApi():
        instance = TestEndpoint('Image API', 'https://apis.activefence.com/v2/content/image')
        return instance


class TextSyncApi(TestEndpoint):
    @staticmethod
    def get_textSyncAPi():
        instance = TestEndpoint('Text API - Synchronous', 'https://apis.activefence.com/sync/v2/content/text')
        return instance
