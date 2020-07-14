
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import Login

browser = webdriver.Chrome('/Users/nippon/Downloads/chromedriver') # put your own path of chromedriver
browser.get('https://linkedin.com')

browser.find_element_by_link_text('Sign in').click()
sleep(1)

browser.find_element_by_id('username').send_keys(Login.email)
sleep(1)

browser.find_element_by_id('password').send_keys(Login.password)
sleep(1)

browser.find_element_by_xpath("//button[@type = 'submit']").click()
sleep(6)

# write name of the person to send the message to in place of <sahil maurya> in below code line 
browser.find_element_by_xpath("//input[@placeholder = 'Search']").send_keys('sahil maurya')
sleep(1)

#change the <RETURN> to <ENTER> in below code line if you are using windows, for mac don't make any change
browser.find_element_by_xpath("//input[@placeholder = 'Search']").send_keys(Keys.RETURN)
sleep(10)

browser.find_element_by_xpath("//button[text() = 'Message' ]").click()
sleep(2)

browser.find_element_by_xpath("//div[ @aria-label = 'Write a message…']").click()
sleep(1)

## write your message in place of <ignore this message> in below code line 
browser.find_element_by_xpath("//div[ @aria-label = 'Write a message…']").send_keys("ignore this message")
sleep(1)

browser.find_element_by_xpath("//button[text() = 'Send']").click()

        
