from http import HTTPStatus
from importlib.resources import Resource

from __init__ import blogPosts, blog_posts

class BlogResource(Resource):

    def get(self, article_id):
        article = next((article for article in blog_posts if article.id == article_id), None)
        
        if article is None:
            return{'message': 'article not found'}, HTTPStatus.NOT_FOUND

        return article.data, HTTPStatus.OK