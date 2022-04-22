from flask import request
from flask_restful import Resource
from http import HTTPStatus

from __init__ import blogPosts, blog_posts

class BlogListResource(Resource):

    def get(self):
        data = []
        for article in blog_posts:
            data.append(article.data)
        
        return {'data': data}, HTTPStatus.OK