from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime
import time


if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = 'http://currentstudents.yorku.ca/'
    browser.get(url)
    browser.find_element_by_xpath("//*[@id='block-menu-menu-current']/ul/li[2]/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='content']/article/div/div/div/div/div[1]/ul/li[1]/a").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='content']/article/div/div/div/p[4]/a/button").click()
    time.sleep(2)
    elem = browser.find_element_by_xpath("//*[@id='mli']")
    elem.send_keys(os.environ.get('YORK_USER'))
    time.sleep(1)
    elem = browser.find_element_by_xpath("//*[@id='password']")
    elem.send_keys(os.environ.get('YORK_PW'))
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[3]/div/p[4]/a/strong").click()
    time.sleep(10)
    browser.quit()

