#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# get_ip.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import undetected_chromedriver as uc
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
import platform
# from dotenv import load_dotenv
from requests import get
from fake_useragent import UserAgent

# load_dotenv()

# def ip_check():
#     # data['ip-info']['old'] = get('https://api.ipify.org').content.decode('utf8')
#     ip_now = get('https://api.ipify.org').content.decode('utf8')
#     return ip_now


def start_driver():
    osID = platform.system().lower()
    ## Function to initiate webdriver based on device

    ua = UserAgent(browsers=['safari', 'firefox'])

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")


    ## When on mac load MAC DRIVER
    ## Update where you added your chromedriver
    if 'darwin' in osID:
        return uc.Chrome()
        # return webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver", options=options)
        # return webdriver.Chrome(ChromeDriverManager().install())
        # return webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")

        # When Chromedriver installed over homebrew
        # xattr -d com.apple.quarantine /opt/homebrew/bin/chromedriver

    ## When on linux load LINUX DRIVER
    ## Update where you added your chromedriver
    if 'linux' in osID:
        return webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

    ## When on linux load LINUX DRIVER
    ## Update where you added your chromedriver
    if 'windows' in osID:
        return webdriver.Chrome(executable_path="DIRECTION TO - chromedriver.exe", options=options)


def godaddy(current_ip):
    driver = start_driver()
    # driver = uc.Chrome()
    driver.get('https://dcc.godaddy.com/manage/okame.xyz/dns')
    username = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@id='username']"))).send_keys(os.environ.get('daddy-user'))
    password = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@id='password']"))).send_keys(os.environ.get('daddy-pass'))
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@id='submitBtn']"))).click()
    try:
        error = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@id='browser-error-modal']"))).text
        print(error)
        driver.close()
    except:
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@aria-label='Edit']"))).click()
        x = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@placeholder='XX.XX.XX.XX']")))
        # WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@placeholder='XX.XX.XX.XX']"))).send_keys('test')
        # x = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@placeholder='XX.XX.XX.XX']"))).set_attribute("value", "your value")
        y = x.get_attribute('value')
        if current_ip not in y:
            print(f'Updating Godaddy')

            for i in y:
                x.send_keys(Keys.BACKSPACE)

            x.send_keys(ip_check())
            # x.send_keys('50.47.92.132')

            WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH,".//*[@id='btnRecordSave']"))).click()
        else:
            print(f'Godaddy IP is the same')
        driver.close()
