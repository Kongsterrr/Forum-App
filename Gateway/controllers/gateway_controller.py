import requests
from flask.views import MethodView
from flask import request, Response, g

from utils.utils import text_type

import config


class GatewayView(MethodView):

    def get(self, path):
        url = g.route['url'] + path[path.find('/')+1:]
        headers = self._clean_request_headers()
        raw_response = requests.get(url, stream=True, params=request.args, headers=headers)
        return self._get_response(raw_response)

    def post(self, path):
        url = g.route['url'] + path[path.find('/')+1:]
        headers = self._clean_request_headers()
        raw_response = requests.post(url, stream=True, data=request.get_data(), headers=headers)
        return self._get_response(raw_response)

    def put(self, path):
        url = g.route['url'] + path[path.find('/')+1:]
        headers = self._clean_request_headers()
        raw_response = requests.put(url, stream=True, data=request.get_data(), headers=headers)
        return self._get_response(raw_response)

    # Used to get the response from the raw response
    def _get_response(self, raw_response):
        def generate():
            for chunk in raw_response.iter_content(config.CHUNK_SIZE):
                yield chunk
        response = Response(generate())
        self._set_response_headers(response, raw_response.headers)
        return response

    # Used to clean the request headers
    def _clean_request_headers(self):
        headers = request.headers
        new_headers = {}

        # if the header has a str, and a unicode, it will cause a 422 error
        for name, value in headers.items():
            l_name = name.lower()
            required_headers = ['x-api-user-json', 'x-api-access-key']
            if l_name.startswith('x-api-') and l_name not in required_headers:
                pass
            elif l_name == 'content-length':
                pass
            else:
                new_headers[text_type(name)] = text_type(value)

        new_headers['Host'] = g.route['netloc']
        return new_headers

    def _set_response_headers(self, response, raw_headers):
        for (k, v) in raw_headers.items():
            if k == 'Server' or k == 'X-Powered-By':
                pass
            elif k == 'Transfer-Encoding' and v.lower() == 'chunked':
                pass
            elif k == 'Location':
                pass
            elif k == 'Content-Length':
                pass
            # elif k == 'Content-Encoding':
            #     pass
            elif k == 'Set-Cookie':
                response.headers.add(k, v)
            else:
                response.headers.set(k, v)

