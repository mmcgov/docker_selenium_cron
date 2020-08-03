#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


class gym_scheduler():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--proxy-auto-detect")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--user-data-dir=/tmp/user-data")
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--log-level=0")
        chrome_options.add_argument("--v=99")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--data-path=/tmp/data-path")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--homedir=/tmp")
        chrome_options.add_argument("--disk-cache-dir=/tmp/cache-dir")
        chrome_options.add_argument("user-agent=Mozilla/5.0 "
                                    "(X11; Linux x86_64) "
                                    "AppleWebKit/537.36 "
                                    "(KHTML, like Gecko) "
                                    "Chrome/61.0.3163.100 "
                                    "Safari/537.36")
        self.driver = webdriver.Chrome('/chromedriver/chromedriver',
                                       options=chrome_options)

    def book_classes(self):
        """
        Function which books classes from the flyefit website
        """
        # gets login page
        self.driver.get('https://myflye.flyefit.ie/login')
        # inputs email and password on page and clicks login
        email = self.driver.find_element_by_id("email_address")
        password = self.driver.find_element_by_id("password")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        self.driver.find_element_by_name("log_in").click()
        # navigates to workouts page
        self.driver.find_element_by_xpath(
                './/a[contains(@href, "/myflye/book-workout")]').click()
        # navigates to tomorrows schedule as can book 24 hrs in advance
        self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/section/div[3]/div/div[3]/a/img')\
        .click()
        time.sleep(2)
        # activates dropdown box to filter on gym classes
        self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/section/div[2]/div'
                '/form/div/div[1]/div/div/div[2]/b').click()
        # chooses gym classes from dropdown
        self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/section'
                '/div[2]/div/form/div/div[1]/div/div'
                '/div[3]/div/ul/li[2]').click()
        # collects all available classes
        classlist = self.driver.find_elements_by_xpath(
                '//*[starts-with(@id, "btn")]')
        id_values = [x.get_attribute("data-course-id") for x in classlist]
        cls_names = [x.get_attribute("data-course-title") for x in classlist]
        cls_time = [x.get_attribute("data-course-time") for x in classlist]
        class_dict = dict(zip(id_values, zip(cls_names, cls_time)))
        chosen_class = [k for k, v in class_dict.items() if '06:05' in v[1]][0]
        self.driver.find_element_by_id(f"btn_{chosen_class}").click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                            ((By.ID, 'book_class'))).click()


def main():
    gs_1 = gym_scheduler(os.environ['email_1'], os.environ['password_1'])
    gs_1.book_classes()


if __name__ == '__main__':
    main()
