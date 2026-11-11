import math
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MODES = {'general': 180, 'technical': 130, 'math': 50}


def get_read_time(text, mode='general'):
    words = text.split()
    return math.ceil(len(words) / MODES.get(mode, 180)) if words else 0


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        mins = get_read_time('sample text for heroku check', 'general')
        self.wfile.write(f'Reading time: {mins} min'.encode())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()
