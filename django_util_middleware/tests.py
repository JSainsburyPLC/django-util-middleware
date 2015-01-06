import json
from datetime import datetime

from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.test import TestCase

from . import views


class ExceptionTests(TestCase):

    # override urls with local versions
    urls = [
        url(r'^exception/$',
            views.exception_view,
            name="exception"),
    ]

    def test_exceptions_are_json(self):
        response = self.client.get(reverse('exception'),
                                   format='json',
                                   content_type='application/json')

        parsed = json.loads(response.content)

        self.assertEqual(500, response.status_code)
        self.assertTrue("ERROR" in parsed)
        self.assertTrue("TRACEBACK" in parsed)


class TimestampTests(TestCase):

    # override urls with local versions
    urls = [
        url(r'^empty/$',
            views.empty_view,
            name="empty"),
    ]

    def test_timestamp_header_is_set(self):
        now = datetime.now().replace(microsecond=0)
        response = self.client.get(reverse('empty'),
                                   format='json',
                                   content_type='application/json')

        # grab the timestamp, set microseconds to 0
        timestamp = datetime.fromtimestamp(
            float(response._headers['timestamp'][1])
        ).replace(microsecond=0)

        self.assertEqual(200, response.status_code)
        self.assertEqual(now, timestamp)
