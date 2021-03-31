from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from re import sub
from decimal import Decimal
import keyboard
import os
import selenium
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
import sys
# sys.path.append('../work')
# from work import notifier

class Instabot:
    def __init__(self, username, password):
        opts = webdriver.ChromeOptions()
        opts.headless =True
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(7)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(1)
        
    def get_notifctions(self):
        button = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a")
        button.click()
        sleep(5)
        self.title = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/span/a").text
        self.desc = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/span/span").text
        # print(self.title, self.desc)
        pre_title = ""
        pre_desc = ""
        if self.title != pre_title:
            pass
        pre_title = self.title
        pre_desc = self.desc
        
        
    # def control_insta(self):
    #     for i in range(590):
    #         keyboard.press_and_release('down')
    #         sleep(0.2)
    #     # self.driver.get("https://www.instagram.com/" + OtherUserId)
    #     posts = self.driver.find_element_by_xpath("/html/body/div/section/main/div/header/section/ul/li/span/span").text
    #     posts = Decimal(sub(r'[^\d.]', '', posts))
    #     print(posts)
    #     pic = self.driver.find_element_by_class_name("_9AhH0")
    #     pic.click()
    #     sleep(2)
        # like = self.driver.find_element_by_xpath(
        #     '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        # like.click()
        # nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
        # nextPic.click()
        # print("success")
        # sleep(2)
        # for i in range(int(posts - 1)):
        #     like = self.driver.find_element_by_xpath(
        #         '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        #     sleep(2)
        #     like.click()
        #     sleep(2)
        #     nextPic = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        #     nextPic.click()
        #     sleep(2)


main = Instabot('unknown.domination', 'VoLksWAgOn69Q01BB10Q96')  # Username,password
main.get_notifctions()