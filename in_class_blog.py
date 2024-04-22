from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ai import checkChatGPT
import os

#Load browser and navigate to url
browser = webdriver.Firefox()
url = 'https://hacking4lawyers.com/blog/index.php'
browser.get(url)

browser.find_element(By.ID,"username").send_keys(os.environ['blog_username'])
browser.find_element(By.ID,"password").send_keys(os.environ['blog_password'])
browser.find_element(By.ID,"loginbutton").click()


user = "You are a Hawaii based attorney who is very busy."
blog_prompt = "Write a blog that is relevant to the law today but like make it sound important."

blog_post = checkChatGPT(user,blog_prompt)
title = checkChatGPT("You are a great title writer","Give me a title for a blog post that matches this blog." + blog_post)


print(blog_post)
print(title)

browser.find_element(By.ID,"blogtitle").send_keys(title)
browser.find_element(By.ID,"blogpost").send_keys(blog_post)
browser.find_element(By.ID,"submitpostbutton").click()


