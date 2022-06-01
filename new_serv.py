import http.server
import socketserver
import os
import jinja

from http.server import HTTPServer, BaseHTTPRequestHandler
# def do_GET(self):  
#     rootdir = 'c:/xampp/htdocs/' #file location  
#     try:  
#       if self.path.endswith('.html'):  
#         f = open(rootdir + self.path) #open requested file  
  
#         #send code 200 response  
#         self.send_response(200)  
  
#         #send header first  
#         self.send_header('Content-type','text-html')  
#         self.end_headers()  
  
#         #send file content to client  
#         self.wfile.write(f.read())  
#         f.close()  
#         return  

#     except IOError:  
#       self.send_error(404, 'file not found')


blog_posts = [
  {
    'title': 'fasdfsd'
  },
  {},
  {}
]


class web_server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        html_file_exist = f'{self.path[1:]}.html'
        if os.path.exists(html_file_exist):
          file_to_open = open(html_file_exist, 'rb').read()
        else:
          file_to_open = open(self.path[1:], 'rb').read()

        if self.path == '/our_blog':
          template = env.get_template("our_blog.html", blog_posts=blog_posts)
          file_to_open = bytes(template.render(the="variables", go="here"))

        self.send_response(200)
        # except:
        #     file_to_open = "File not found"
        #     self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open)


httpd = HTTPServer(('127.0.0.1', 8099), web_server)
httpd.serve_forever()
    
    
    
    
