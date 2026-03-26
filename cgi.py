"""Compatibility shim for Python 3.13+ where stdlib cgi was removed."""

import re
from email.message import Message


def parse_header(line):
    if isinstance(line, bytes):
        line = line.decode('ascii')
    message = Message()
    message['content-type'] = line
    key = message.get_content_type()
    params = dict(message.get_params()[1:])
    return key, params


def valid_boundary(s):
    if isinstance(s, bytes):
        s = s.decode('ascii')
    return re.match(r"^[ -~]{0,200}[!-~]$", s) is not None
