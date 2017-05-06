import requests
import json

import re


def pretty_print_request(r):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}\n{}'.format(
        '-----------START-----------',
        r.request.method + ' ' + r.request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in r.request.headers.items()),
        r.request.body,
        '-----------END-----------',
    ))
    print('\n{}\n{}\n{}\n{}'.format(
        '------START-RESPONSE-----',
        'Status Code: ' + str(r.status_code),
        r.text,
        '-------END-RESPONSE------',
    ))


def anki_connect(method, params={}, debug=False):
    r = requests.post('http://localhost:8765', data=json.dumps({'action': method, 'params': params}))

    if debug:
        pretty_print_request(r)

    r.raise_for_status()

    if r.json() is None:
        raise Exception('Anki connect responded with null, this is normally an error')

    return r.json()


def parse(string):
    sections = re.split('^\s*@', string, flags=re.MULTILINE)
    nonempty_sections = (sec for sec in sections  if sec.strip() != '')

    out = {}
    for sec in nonempty_sections:
        lines = sec.split('\n')
        key = lines[0].strip().lstrip('@')
        value = '\n'.join(lines[1:])
        out[key] = value

    return out
