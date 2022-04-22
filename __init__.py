blog_posts = []

def get_last_id():
    if blog_posts:
        last_post = blog_posts[-1]
    else:
        return 1
    return last_post + 1

class blogPosts:
    def __init__(self, id, author, authorId, likes, popularity, reads, tags):
        self.id = id
        self.author = author
        self.authorId = authorId
        self.likes = likes
        self.popularity = popularity
        self.reads = reads
        self.tags = tags
    
    @property
    def data(self):
        return {
            'id': self.id,
            'author': self.author,
            'authorId': self.authorId,
            'likes': self.likes,
            'popularity': self.popularity,
            'reads': self.reads,
            'tags': self.tags
        }