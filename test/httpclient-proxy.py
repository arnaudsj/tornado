#!/usr/bin/env python2.6

import time
import unittest
from tornado import httpclient, ioloop

#TODO: Add Async tests (but no easy way to do this elegantly so I pass for now)

class TestHTTPClient(unittest.TestCase):
    def setUp(self):
        """ Setup your test proxy host, port, username & password """
        self.test_url = "http://www.google.com/"
        self.test_proxy_host = "http://127.0.0.1/"
        self.test_proxy_port = 53747
        self.test_proxy_username = None
        self.test_proxy_password = None
       
    def tearDown(self):
        pass

    def test_1_sync_noproxy(self):
        http_client = httpclient.HTTPClient()
        response = http_client.fetch(self.test_url)
        self.assertEqual(response.code, 200)
        
    def test_2_sync_proxy(self):
        http_client = httpclient.HTTPClient(
        proxy_host = self.test_proxy_host,
        proxy_port = self.test_proxy_port, 
        proxy_username = self.test_proxy_username,
        proxy_password = self.test_proxy_password)
        response = http_client.fetch(self.test_url)
        self.assertEqual(response.code, 200)
        
if __name__ == '__main__':
    unittest.main()

