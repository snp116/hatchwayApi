from flask import Flask
from flask_restful import Api

from resources.blog import BlogResource, BlogListResource

app = Flask(__name__)
api = Api(app)

api.add_resource(BlogListResource, 'https://api.hatchways.io/assessment/blog/posts')
api.add_resource(BlogResource, 'https://api.hatchways.io/assessment/blog/posts')

if __name__ == '__main__':
    app.run(port=5000, debug=True)