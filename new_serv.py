
import os

from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

from decorators import validator_decorator

from config.db import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from databases.connection import Connection

from databases.models.post import Post #<---------------------------------
print('-'*15, DB_HOST, 
  DB_USER, 
  DB_PASSWORD, 
  DB_NAME)
connection = Connection(
  DB_HOST, 
  DB_USER, 
  DB_PASSWORD, 
  DB_NAME
  )


def list_Post(start,size):
  start = start*size
  return Post(connection).getPost(f'{start}, {size}','Post.creation_date') #<---------------------------------

def corecting_curent_post(curent):
  size_post = Post(connection).lenPost() #<---------------------------------
  if curent <= 0 or curent > size_post // 6:
    return [1,'class="this_list"']
  ## Do not use else
  return [curent,'class="this_list"']

def number_list(curent):
    curent = corecting_curent_post(curent)[0]
    st, en = 0, 5
    while True:
        if st <= curent <= en:
            return list(range(st+1,en+1))
        else:
            st, en = st+5, en+5


class web_server(BaseHTTPRequestHandler):
  
  def do_GET(self):
    list_curent = 1
    if self.path == '/':
        self.path = '/index.html'
    if '/list_blog' in self.path: 
        list_curent = corecting_curent_post(int(self.path[10:]))[0]  
        self.path = '/our_blog'
    html_file_exist = f'{self.path[1:]}.html'
    if os.path.exists(html_file_exist):
      file_to_open = open(html_file_exist, 'rb').read()
    else:
      file_to_open = open(self.path[1:], 'rb').read()
    if self.path == '/our_blog':
      file_loader = FileSystemLoader('')
      env = Environment(loader=file_loader)
      templ = env.get_template('our_blog.html')
      file_to_open = templ.render(blog_posts=list_Post(list_curent,6),number_list=number_list(list_curent),tmp_carent=list_curent,curent=list_curent,this_list=corecting_curent_post(list_curent)[1]).encode()
    self.send_response(200)
    self.end_headers()
    self.wfile.write(file_to_open)
    # print("Path (GET): ", self.path)
  
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
    
    

    
