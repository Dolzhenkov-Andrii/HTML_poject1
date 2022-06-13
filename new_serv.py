
import os
import urllib

from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

from decorators import validator_decorator



blog_posts = [
  {
    'img_link': "/blog_img/bimg_1.png",
    'title': "Pellentesque felis nibh",
    'article': "Phasellus sit amet neque molestie nunc tincidunt ultrices. Donec laoreet mi sit amet gravida bibendum. Aliquam erat volutpat. Aliquam arcu est, malesuada a nisi in.", 
  },
  {
    'img_link': "/blog_img/bimg_2.png",
    'title': "Mauris nisi magna, congue quis faucibus ac",
    'article': "Nulla in tincidunt neque, a luctus mi. Donec sollicitudin est vehicula mauris condimentum mattis. Suspendisse in augue ut lorem viverra dignissim. Fusce ultrices, mauris vitae fringilla.",
  },
  {
    'img_link': "/blog_img/bimg_3.png",
    'title': "Adipiscing auctor turpis",
    'article': "Aenean auctor leo et libero convallis, eget tempor urna rutrum. Aliquam erat volutpat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.",
  },
  {
    'img_link': "/blog_img/bimg_4.png",
    'title': "Duis sed lectus placerat, facilisis lacus id",
    'article': "Pellentesque aliquam eros non augue cursus, ut porta leo ornare. Suspendisse odio lectus, commodo ac mauris in, bibendum pretium nisi.",
  },
  {
    'img_link': "/blog_img/bimg_5.png",
    'title': "Fermentum pellentesque dolor at",
    'article': "Duis eros nisl, tincidunt sed elit ut, feugiat elementum justo. Vivamus ornare id eros vel imperdiet. Sed venenatis dapibus consequat. Curabitur viverra erat id vehicula consectetur.",
  },
  {
    'img_link': "/blog_img/bimg_6.png",
    'title': "Nunc sodales nec ante eget sollicitudin",
    'article': "Pellentesque imperdiet sem nec pellentesque luctus. Sed nisl elit, tempus sed ultricies vel, laoreet ut magna. In a condimentum nulla. Maecenas sem tellus, blandit a felis at, luctus lobortis erat.",
  },
  {
    'img_link': "/blog_img/bimg_6.png",
    'title': "Nunc sodales nec ante eget sollicitudin",
    'article': "Pellentesque imperdiet sem nec pellentesque luctus. Sed nisl elit, tempus sed ultricies vel, laoreet ut magna. In a condimentum nulla. Maecenas sem tellus, blandit a felis at, luctus lobortis erat.",
  }
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
      file_loader = FileSystemLoader('')
      env = Environment(loader=file_loader)
      templ = env.get_template('our_blog.html')
      
      file_to_open = templ.render(blog_posts=blog_posts[:-1]).encode()
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
    
    

    
