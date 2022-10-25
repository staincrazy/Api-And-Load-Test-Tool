import requests


class SyncRequestsAdapter:
    @staticmethod
    def post_request(endpoint_url, data, api_key):

        headers = {'af-api-key': api_key}
        response = requests.post(url=endpoint_url, data=data, headers=headers)

        return response


