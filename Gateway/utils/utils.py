from flask import request, g
from config import routes
from future.utils import iteritems

unicode_type = str
basestring_type = str
text_type = str

_UTF8_TYPES = (bytes, type(None))


def utf8(value):
    if isinstance(value, _UTF8_TYPES):
        return value
    if not isinstance(value, unicode_type):
        raise TypeError(
            "Expected bytes, unicode, or None; got %r" % type(value)
        )
    return value.encode("utf-8")


_TO_UNICODE_TYPES = (unicode_type, type(None))


def unicode_encoded_dict(in_dict):
    out_dict = {}
    for k, v in in_dict.items():
        out_dict[to_unicode(k)] = to_unicode(v)
    return out_dict


_TO_UNICODE_TYPES = (unicode_type, type(None))


def to_unicode(value):
    if isinstance(value, _TO_UNICODE_TYPES):
        return value
    if not isinstance(value, bytes):
        raise TypeError(
            "Expected bytes, unicode, or None; got %r" % type(value)
        )
    return value.decode("utf-8")


def utf8_encoded_dict(in_dict):
    out_dict = {}
    for k, v in iteritems(in_dict):
        out_dict[utf8(k)] = utf8(v)
    return out_dict


def get_route():
    service_name = request.path.split('/')[1]
    g.route = list(filter(lambda x: x['service_name'] == service_name, routes))[0]


