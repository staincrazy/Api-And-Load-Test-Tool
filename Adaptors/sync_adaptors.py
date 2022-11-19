import requests


class SyncRequestsAdapter:
    @staticmethod
    def post_request(endpoint_url, data, api_key):
        headers = {'af-api-key': api_key}
        response = requests.post(url=endpoint_url, data=data, headers=headers)

        return response

    @staticmethod
    def get_request(endpoint_url, data=None):
        if data is None:
            data = data
        response = requests.get(url=endpoint_url, data=data)

        return response
