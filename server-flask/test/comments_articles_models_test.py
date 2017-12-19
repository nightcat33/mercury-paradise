import unittest
import requests
from random import randint


class TestIntegratedCase(unittest.TestCase):

    def test_comments_integration(self):

        # test create one
        payloads = {
            'comment_id': 50,
            'body': 'test comments creating',
            'user_id': 50
        }

        create_result = requests.post(
            'http://0.0.0.0:5000/comments/createone', json=payloads)
        create_result.raise_for_status()
        # test create multiple
        payloads = []
        upper = randint(30, 40)
        for i in range(0, upper):
            p = {
                'comment_id': i,
                'body': str(i),
                'user_id': i
            }
            payloads.append(p)

        create_result = requests.post(
            'http://0.0.0.0:5000/comments/createmultiple', json=payloads)
        create_result.raise_for_status()

        #test delete one
        payloads = {
            'comment_id': 50
        }

        delete_result = requests.post(
            'http://0.0.0.0:5000/comments/deleteone', json=payloads)
        delete_result.raise_for_status()

        #test delete multiple
        payloads = {'comment_id': 0, 'body': '1', 'user_id': 2}

        delete_result = requests.post(
            'http://0.0.0.0:5000/comments/deletemultiple', json=payloads)
        delete_result.raise_for_status()

        payloads = {
            'comment_id': 3
        }

        #test read one
        read_result = requests.post(
            'http://0.0.0.0:5000/comments/readone', json=payloads)
        read_result.raise_for_status()

        #test read multiple
        payloads = {'comment_id': 4, 'body': '5', 'user_id': 6}

        read_result = requests.post(
            'http://0.0.0.0:5000/comments/readmultiple', json=payloads)
        read_result.raise_for_status()

        #test update one
        payloads = {
            'filter': {'comment_id': 4},
            'update': {'$set': {'body': 'hello world!'}}
        }

        update_result = requests.post('http://0.0.0.0:5000/comments/updateone', json=payloads)
        update_result.raise_for_status()

    def test_articles_integration(self):
        # test create one
        payloads = {
            'title': 'hello world',
            'body': 'test article creating',
            'article_id': 50,
            'creator_id': 50,
            'irc_id' : 50
        }

        create_result = requests.post('http://0.0.0.0:5000/article/createone', json=payloads)
        create_result.raise_for_status()

        # test create multiple
        payloads = []
        upper = randint(30, 40)
        for i in range(0, upper):
            p = {
                'title': str(i),
                'body': str(i),
                'article_id': i,
                'creator_id': i,
                'irc_id' : i
            }
            payloads.append(p)

        create_result = requests.post('http://0.0.0.0:5000/article/createmultiple', json=payloads)
        create_result.raise_for_status()

        #test delete one
        payloads = {
            'article_id': 50
        }

        delete_result = requests.post('http://0.0.0.0:5000/article/deleteone', json=payloads)
        delete_result.raise_for_status()

        #test delete multiple
        payloads = {'article_id': 0, 'body': '1', 'creator_id': 2}

        delete_result = requests.post('http://0.0.0.0:5000/article/deletemultiple', json=payloads)
        delete_result.raise_for_status()

        payloads = {
            'irc_id': 3
        }

        #test read one
        read_result = requests.post('http://0.0.0.0:5000/article/readone', json=payloads)
        read_result.raise_for_status()

        #test read multiple
        payloads = {'creator_id': 4, 'body': '5', 'irc_id': 6}

        read_result = requests.post('http://0.0.0.0:5000/article/readmultiple', json=payloads)
        read_result.raise_for_status()

        #test update one
        payloads = {
            'filter': {'article_id': 4},
            'update': {'$set': {'body': 'mango pig!'}}
        }

        update_result = requests.post('http://0.0.0.0:5000/article/updateone', json=payloads)
        update_result.raise_for_status()

if __name__ == '__main__':
    unittest.main()

    
