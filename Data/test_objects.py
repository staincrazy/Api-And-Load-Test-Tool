class TestEndpoint:
    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint


class CatFactsAsyncAPi(TestEndpoint):
    @staticmethod
    def get_randomCatFact():
        instance = TestEndpoint('Cat Facts Endpoint', 'https://catfact.ninja/fact')
        return instance



