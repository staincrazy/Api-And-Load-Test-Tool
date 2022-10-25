import grequests


class AsyncRequestsAdapter:
    @staticmethod
    def post_multiple_requests(url, api_key, data):

        headers = {'af-api-key': api_key}
        urls_list = [url, url, url, url, url, url, url, url, url, url]
        response = (grequests.post(url, data=data, headers=headers) for url in urls_list)

        return grequests.map(response)
