import random

from Adaptors.async_adaptors import AsyncRequestsAdapter as asyncRequests
from Adaptors.sync_adaptors import SyncRequestsAdapter as syncRequests
from Data.auth_data import getApiKey
from Data.test_data import violations
from Data.test_objects import TextAsyncAPi
from Utils.base_test_case import BaseTestCase


class TextApiAsyncTest(BaseTestCase):

    def setUp(self):
        self._api_key = getApiKey()
        self.endpoint_url = TextAsyncAPi.get_textAsyncApi().endpoint
        self.webhook_url = 'https://webhook.site/d284e774-acf8-41d9-865f-0e0a9a321afc'

    def test_case_01__correct_creds_and_required_fields__code_200_(self):

        data = {'text': 'This is {}, and  {}'.format(violations(), violations()),
                'title': violations(),
                'description': violations(),
                'content_id': str(random.randint(1, 100)),
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 200
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 200, got {} instead'.format(resp.status_code))

    def test_case_02__missing_one_required_field__code_400_(self):

        data = {'text': 'This is {}, and  {}'.format(violations(), violations()),
                'content_id': None,
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 400, got {} instead '.format(resp.status_code))

    def test_case_03__missing_both_required_fields_code_400_(self):

        data = {'text': '',
                'content_id': '',
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 400, got {} instead'.format(resp.status_code))

    def test_case_04__incorrect_data_type__code_400_(self):

        data = {'text': None,
                'content_id': 707,
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Expected 400, got {} instead. Check ASAP'.format(resp.status_code))

    def test_case_05__incorrect_credentials__code_401_(self):

        data = {'text': 'This is {}, and  {}'.format(violations(), violations()),
                'content_id': str(random.randint(1, 100)),
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key='18721')

        try:
            assert resp.status_code == 401
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 401, got {} instead'.format(resp.status_code))

    def test_case_06__multiple_async_post_requests__code_429_(self):

        data = {'text': 'This is {}, and  {}'.format(violations(), violations()),
                'content_id': str(random.randint(1, 100)),
                'callback_url': self.webhook_url}

        resp = asyncRequests.post_multiple_requests(self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert any(resp[i].status_code == 429 for i in range(len(resp)))
        except AssertionError:
            self.fail('Looks like no 429 error code. Got this {}'.format(resp))
