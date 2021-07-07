# Moodle REST Client

This is a basic Moodle REST client for Python.

## Setup

Everything is included in the file `moodle_client.py`. Therefore, just clone the repository and use the file as you want.

The only required package , that is not core to Python, is: `requests`.

Use PIP to install it, if needed.


## Usage

This is a basic example of accessing a WS-function, passing parameters and then downloading a file from
a returned URL.

The primary method is `send`: it calls the given WS-function with the provided parameter dictionary.

Additionally a download method is provided, as downloading files from URLs returned from Moodle-WS can be a bit involved.

```python
from moodle_client import MoodleClient

client = MoodleClient('YOUR_WS_TOKEN', 'YOUR_MOODLE_DOMAIN')

resp = client.send('mod_wiki_get_subwiki_files', {'wikiid':1})

client.download_file(resp.files[0].fileurl, 'FILE_NAME', download_dir='.')
```

Finally, you can also instantiate your client using the redirect url of the form:

```html
moodlemobile://token=<BASE64_ENCODED_TOKEN>
```
as received from

```html
<YOUR_MOODLE_DOMAIN>/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=PASSPORT
```

instead of your WS-token.