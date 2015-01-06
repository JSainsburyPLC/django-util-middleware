import json
import time
import traceback

from datetime import datetime
from django.http import HttpResponse


HOURS_IN_DAY = 24
SECONDS_IN_HOUR = 3600


class JSONExceptionMiddleware(object):
    """Return all exceptions as JSON, replacing
    the default Django error page"""

    def process_exception(self, request, exception):
        return HttpResponse(json.dumps({'ERROR': unicode(exception),
                                        'TRACEBACK': traceback.format_exc(
                                            exception)}, sort_keys=True),
                            content_type='application/json',
                            status=500)


def local_time_offset(t=None):
    """Return offset in seconds of local zone
    from UTC, either at present or at time t."""
    if t is None:
        t = time.time()

    if time.localtime(t).tm_isdst and time.daylight:
        return time.altzone
    else:
        return time.timezone


def to_utc_timestamp(dt):
    """Convert datetime to a UTC timestamp"""
    td = dt - datetime.utcfromtimestamp(0)

    tz_offset_in_seconds = local_time_offset()

    total_days_in_seconds = (
        td.days *
        HOURS_IN_DAY *
        SECONDS_IN_HOUR
    )

    total_seconds_in_ms = (
        td.seconds +
        total_days_in_seconds +
        tz_offset_in_seconds
    ) * 10**6

    return ((td.microseconds + total_seconds_in_ms) / 1e6)


class TimestampMiddleware(object):
    """
    Adds a `Timestamp` header containing the
    unix timestamp for the response
    """
    def process_response(self, request, response):
        response['Timestamp'] = to_utc_timestamp(datetime.now())
        return response
