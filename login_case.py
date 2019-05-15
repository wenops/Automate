#coding:utf-8

import unittest
from selenium import webdriver
import time

class LoginCase(unittest.TestCase):

    def setUp(self):
        print('before test')
        self.dr = webdriver.Chrome()
        self.dr.get('http://192.168.1.165/wordpress/wp-login.php')

    def test_post(self):
        user_name = 'young'
        password = '123456'
        self.login(user_name,password)
        title = 'this is title %s'%(time.time())

        self.dr.get('http://192.168.1.165/wordpress/wp-admin/post-new.php')
        self.by_name('post_title').send_keys(title)
        self.set_content('2333332333333')
        self.by_name('publish').click()
        self.dr.get('http://192.168.1.165/wordpress/wp-admin/edit.php')
        self.assertEqual(self.by_css('.row-title').text,title)

    def set_content(self,text):
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerText = '%s'"% text
        print(js)
        self.dr.execute_script(js)

    def login(self,user_name,password):
        self.by_id('user_login').send_keys(user_name)
        self.by_id('user_pass').send_keys(password)
        self.by_name('wp-submit').click()

    def by_id(self,the_id):
        return self.dr.find_element_by_id(the_id)

    def by_css(self,css):
        return self.dr.find_element_by_css_selector(css)

    def by_name(self,name):
        return self.dr.find_element_by_name(name)

    def tearDown(self):
        print('after every test')
        self.dr.quit()
if __name__ == '__main__':
    unittest.main()