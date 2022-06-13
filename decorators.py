
import urllib

def validator_decorator(func):
    def validator(self):
        post_data = urllib.parse.parse_qs(self.rfile.read(int(self.headers['Content-Length'])).decode())
        if 'email' not in post_data or 'password' not in post_data:
            file_to_open = open('400.html', 'rb').read()
            self.send_response(400)
            self.end_headers()
            self.wfile.write(file_to_open)
        func(self, post_data)
    return validator