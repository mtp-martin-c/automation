import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Funciones:

    def __init__(self, driver):
        self.driver =driver


    def Time(self, tim):
        t = time.sleep(tim)
        return t

    def Navigate(self,url,tim):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Web page open:" + str(url))
        t = time.sleep(tim)
        return t





    def text_name(self, name, texto, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, name)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.NAME, name)
            val.clear()
            val.send_keys(texto)
            print(f"On element with name: '{name}' writing: {texto}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print("Unable to find Element with name: " + name)



    def screen_shoot(self, file_name, file_path=r"C:\Users\Ancch\PycharmProjects\Testing_World\Practica2\Screenshots"):
        if file_path is None:
            full_path = file_name + '.png'
        else:
            full_path = os.path.join(file_path, file_name + '.png')

        print(f"Saving screenshot to: {full_path}")
        try:
            success = self.driver.save_screenshot(full_path)
            if success:
                print("Screenshot saved successfully.")
            else:
                print("Failed to save screenshot.")
        except Exception as e:
            print(f"Error saving screenshot: {e}")

    def click_class(self, clas, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, clas)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.CLASS_NAME, clas)
            val.click()
            print(f"Successfully clicked element with class: {clas}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find Element with class: {clas}")


    def select_id_text(self, id, text, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.ID, id)
            val = Select(val)
            val.select_by_visible_text(text)
            print(f"The selected field is : {text}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {text}")


    def select_id_type(self, id, type, data, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.ID, id)
            val = Select(val)
            if type == "text":
                val.select_by_visible_text(data)
            elif type == "index":
                val.select_by_index(data)
            elif type == "value":
                val.select_by_value(data)
            print(f"The selected field is : {data}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {id}")

    def select_class_text(self, css, text, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.CLASS_NAME, css)
            val = Select(val)
            val.select_by_visible_text(text)
            print(f"The selected field is : {text}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {text}")



    def select_css_type(self, css, type, data, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.CLASS_NAME, css)
            val = Select(val)
            if type == "text":
                val.select_by_visible_text(data)
            elif type == "index":
                val.select_by_index(data)
            elif type == "value":
                val.select_by_value(data)
            print(f"The selected field is : {data}")
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {id}")

    def upload_id(self, id, route, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.ID, id)
            val.send_keys(route)
            print(" Image has been  uploaded {} ".format(route))
            time.sleep(tim)
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {id}")

    def check_id(self, id, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            print("Click on Element {} ".format(id))
            time.sleep(tim)
            return tim
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {id}")

    def check_class(self, css, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, css)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.CLASS_NAME, css)
            val.click()
            print("Click on Element {} ".format(css))
            time.sleep(tim)
            return tim
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {css}")

    def check_xpath(self, xpath, tim):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Click on Element {} ".format(xpath))
            time.sleep(tim)
            return tim
        except TimeoutException as ex:
            print(ex.msg)
            print(f"Unable to find field : {xpath}")

    def check_id_multiples(self, tim, *args):
        for num in args:
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, num)))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
                val.click()
                print(f"Click on Element {num}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"Unable to find field: {num}")



    def text_mixto(self, type, selector, texto, tim):
        if type == "Id":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                                 val)
                val = self.driver.find_element(By.ID, selector)
                val.clear()
                val.send_keys(texto)
                print(f"On ID with name: '{selector}' writing: {texto}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print("Unable to find Element " + selector)

        elif type == "Name":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                                 val)
                val = self.driver.find_element(By.CLASS_NAME, selector)
                val.clear()
                val.send_keys(texto)
                print(f"On element with name: '{selector}' writing: {texto}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print("Unable to find Element " + selector)

        elif type == "Xpath":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                                 val)
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                print(f"On element with name: '{selector}' writing: {texto}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print("Unable to find Element " + selector)

    def click_mixt(self, type, selector, tim):
        if type == "Xpath":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",val)
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                print(f"Successfully clicked element with Xpath : {selector}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"Unable to find Element with Xpath : {selector}")

        elif type == "Id":
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print(f"Successfully clicked element with ID: {selector}")
                time.sleep(tim)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"Unable to find Element with ID: {selector}")


