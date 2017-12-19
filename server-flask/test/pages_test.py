import unittest
import requests
from random import randint


class TestIntegratedCase(unittest.TestCase):

    def test_pages_integration(self):

        # test create one
	    payloads = {
	        'page_name': 'main_page',
	        'directories': [{'article_id': 0, 'directory_name': 'new1'}, {'article_id': 1, 'directory_name': 'new2'}, {'article_id': 2, 'directory_name': 'new3'}, {'article_id': 3, 'directory_name': 'new4'}]
	    }

	    create_result = requests.post(
	        'http://0.0.0.0:5000/pages/createone', json=payloads)
	    create_result.raise_for_status()
	    # test create multiple
	    payloads = []
	    upper = randint(30, 40)
	    for i in range(0, upper):
	        p = {
	            'page_name': str(i),
	            'directories': [{
	                'article_id': i, 'directory_name': str(i)
	            }]
	        }
	        payloads.append(p)

	    create_result = requests.post(
	        'http://0.0.0.0:5000/pages/createmultiple', json=payloads)
	    create_result.raise_for_status()

	    # test delete one
	    payloads = {
	        'page_name': 'main_page'
	    }

	    delete_result = requests.post(
	        'http://0.0.0.0:5000/pages/deleteone', json=payloads)
	    delete_result.raise_for_status()

	    # test delete multiple
	    payloads = {'page_name': '0',
	                'directories': [{'directory_name': '1'}]}

	    delete_result = requests.post(
	        'http://0.0.0.0:5000/pages/deletemultiple', json=payloads)
	    delete_result.raise_for_status()

	    payloads = {
	        'page_name': '3'
	    }

	    #test read one
	    read_result = requests.post(
	        'http://0.0.0.0:5000/pages/readone', json=payloads)
	    read_result.raise_for_status()

	    #test read multiple
	    payloads = {'page_name': '4', 'directories': [{'directory_name': '10'}]}

	    read_result = requests.post(
	        'http://0.0.0.0:5000/pages/readmultiple', json=payloads)
	    read_result.raise_for_status()

	    #test update one
	    payloads = {
	        'filter': {'page_name': '3'},
	        'update': {'$set': {'page_name': 'hello world!'}}
	    }

	    update_result = requests.post('http://0.0.0.0:5000/pages/updateone', json=payloads)
	    update_result.raise_for_status()

if __name__ == '__main__':
    unittest.main()


