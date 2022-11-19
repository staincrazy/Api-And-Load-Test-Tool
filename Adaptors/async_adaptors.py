import grequests


class AsyncRequestsAdapter:
    @staticmethod
    def post_multiple_requests(url, api_key, data):

        headers = {'af-api-key': api_key}
        urls_list = [url, url, url, url, url, url, url, url, url, url]
        response = (grequests.post(url, data=data, headers=headers) for url in urls_list)

        return grequests.map(response)

    @staticmethod
    def get_multiple_requests(url, data=None):
        if data is None:
            data = data
        urls_list = [url,url,url,url,url,url,url,url,url,url,url]
        response = (grequests.get(url, data=data) for url in urls_list)

        return grequests.map(response)
