import json
from types import SimpleNamespace

import requests
import base64
import urllib.request
import shutil
import os
import urllib.parse as urlparse
from urllib.parse import urlencode

class MoodleClient:

    def __init__(self, token, host="https://tuwel.tuwien.ac.at"):
        if (token.startswith("moodlemobile")):
            self.token = self.parse_token_from_url(token)
        else:
            self.token = token

        self.host = host + "/webservice/rest/server.php"

    def send(self, function, params={}):
        ws_params = {
            'wstoken': self.token,
            'wsfunction': function,
            'moodlewsrestformat': "json"
        }
        ws_params.update(params)

        response = requests.post(self.host, data=ws_params)

        return json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

    def download_file(self, file_url, file_name, download_dir="downloads"):
        params = {"token": self.token}

        # Keep existing params and append token param
        url_parts = list(urlparse.urlparse(file_url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)
        url_parts[4] = urlencode(query)

        url = urlparse.urlunparse(url_parts)

        print("Downloading: " + url)
        with urllib.request.urlopen(url) as response, open(os.path.join(download_dir, file_name), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    def parse_token_from_url(self, url):
        parts = url.split("=", 1)
        base64_message = parts[1]
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        token = message.split(":::")[1]
        print("parsed token " + token + " from url: " + message)
        return token