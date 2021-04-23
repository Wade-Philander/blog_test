from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test','Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test','Test Author')
        b2 = Blog ('My Day', 'Jackie')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Jackie (0 posts)')

    def test_repr_multiple(self):
         b = Blog('Test','Test Author')
         b.posts = ['test']

         b2 = Blog('My Day', 'Jackie')
         b2.posts = ('another', 'test')

         self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
         self.assertEqual(b2.__repr__(), 'My Day by Jackie (2 posts)')

    def test_create_post_in_blog(self):
        b = Blog('Test','Test Author')
        b.create_post('Test Post','Test Content')

        self.assertEqual(len(b.posts),1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json_no_post(self):
        b = Blog('Test','Test Author')
        expected = {'title':'Test','author': 'Test Author', 'posts': []}
        
        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test','Test Author')
        b.create_post('Test Post','Test Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts':[
                {
                    'title': 'Test Post',
                    'content':'Test Content'
                }
            ]
        }
        self.assertDictEqual(expected, b.json())

        

