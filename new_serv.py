"""
  Server
"""
import os

from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

from decorators import validator_decorator

from databases.connection import Connection
from databases.models.base import Post
from config.db import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

connection = Connection(
        DB_HOST,
        DB_USER,
        DB_PASSWORD,
        DB_NAME
        )
BaseManager.database_connection = connection

our_blog = Post().objects\
          .select('Post.id', 'Post.title','Post.text', 'User_Photo.photo')\
          .FROM('Photo_Post')\
          .JOIN('Post',id='Photo_Post.post_id')\
          .JOIN('User_Photo',id='Photo_Post.photo_id')\
          .fetch(connection)


def post_list(start,size):
    """
      List of all post articles
    """
    start = start*size
    return Post(connection).getPost(f'{start}, {size}','Post.creation_date')


def corecting_curent_post(curent):
    """
      Adds a class into html
    """
    size_post = Post(connection).lenPost()
    if curent <= 0 or curent > size_post // 6:
        return [1,'class="this_list"']
    ## Do not use else
    return [curent,'class="this_list"']

def number_list(curent):
    """
        Example
    """
    curent = corecting_curent_post(curent)[0]
    start, end = 0, 5
    while True:
        if start <= curent <= end:
            return list(range(start+1,end+1))
        else:
            start, end = start+5, end+5


class WebServer(BaseHTTPRequestHandler):
    """
      Application webserver
    """

    # pylint: disable=C0103,attribute-defined-outside-init
    def do_GET(self):
        """
          GET request handlers
        """
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
            file_to_open = templ.render(
                blog_posts=post_list(list_curent, 6),
                number_list=number_list(list_curent),
                tmp_carent=list_curent,
                curent=list_curent,this_list=corecting_curent_post(list_curent)[1])\
                .encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(file_to_open)

    def my404(self):
        """
          404
        """
        file_to_open = "File not found"
        self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open.encode('utf-8'))

    # pylint: disable=C0103
    @validator_decorator
    def do_POST(self, post_data):
        """
          Post handler
        """
        email, password = post_data['email'][0], post_data['password'][0]
        if(email == 'posttest@gmail.com' and password == 'Qwerty+!'):
            return self.do_GET()
        return self.my404()

httpd = HTTPServer(('127.0.0.1', 9000), WebServer)
httpd.serve_forever()
