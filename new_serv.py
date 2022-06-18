
import os
import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

from decorators import validator_decorator
from b_d import orm
myDB = orm.ORM_my(host='',user='oscura',password='Ujhs!!Gj04Rjktyj!((#',db='my_blog')


def bPost():
  user_post = myDB.select("select id, title, text from Post")
  for id in user_post:
    id.update(myDB.select(f"SELECT photo FROM User_Photo INNER JOIN Photo_Post ON User_Photo.id=Photo_Post.photo_id WHERE photo_id={id['id']}")[0])
  return user_post
  
 



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
      file_loader = FileSystemLoader('')
      env = Environment(loader=file_loader)
      templ = env.get_template('our_blog.html')
      file_to_open = templ.render(blog_posts=bPost()).encode()
    self.send_response(200)
    self.end_headers()
    self.wfile.write(file_to_open)
    print("Path (GET): ", self.path)
  
  def my404(self):
    file_to_open = "File not found"
    self.send_response(404)
    self.end_headers()
    self.wfile.write(file_to_open.encode('utf-8'))
  
  @validator_decorator
  def do_POST(self, post_data):
    email, password = post_data['email'][0], post_data['password'][0]
    if(email == 'posttest@gmail.com' and password == 'Qwerty+!'):
      # print("Path (POST): ", self.path)
      return self.do_GET()
    # print("Path (my404): ", self.path)
    return self.my404()
    

httpd = HTTPServer(('127.0.0.1', 9000), web_server)
httpd.serve_forever()
    
    

    
