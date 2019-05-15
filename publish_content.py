#coding:utf-8

from selenium import webdriver



dr = webdriver.Chrome()
dr.get('http://www.qq.com')
text=dr.find_element_by_css_selector('hd .news-top').text
print(text)