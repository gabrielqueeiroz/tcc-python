from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    # def __init__(self, driver):
    #     self.driver = driver
    #     self.combo_select = self.driver.find_element_by_xpath("/html/body/div[1]/select/option[4]")
    #     self.add_customer_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[1]/a")
    #     self.search_name = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[3]/input")
    #     self.actions_checkbox = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[1]/div/input")
    #     self.delete_button = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[2]/div[1]/a")
    #     self.delete_message = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div/div/div[2]/p[2]")
    #     self.delete_popup_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div/div/div[3]/button[2]")
    #     self.update_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[2]/div[2]/a")

    def initialize_variables(self, driver):
        self.driver = driver
        self.combo_select = self.driver.find_element_by_xpath("/html/body/div[1]/select/option[4]")
        self.add_customer_button = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[1]/div[1]/a")
        self.search_name = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[3]/input")
        self.actions_checkbox = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[1]/div/input")
        self.delete_button = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[2]/div[1]/a")
        self.delete_message = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div/div/div[2]/p[2]")
        self.delete_popup_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div/div/div[3]/button[2]")
        self.update_button = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[2]/div[2]/a")

    def addCustomer(self):
        self.combo_select.click()
        self.add_customer_button.click()

    def deleteCustomer(self, name):
        self.search_name.send_keys(name)
        self.update_button.click
        self.actions_checkbox.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[2]/div[1]/a")))
        self.delete_button.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/div[1]")))
        assert self.delete_message.getText() == "Are you sure that you want to delete this 1 item?"
        self.delete_popup_button.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/span[3]/p")))
        self.popup_message = self.driver.find_element_by_xpath("/html/body/div[4]/span[3]/p")
        assert self.popup_message.getText() == "Your data has been successfully deleted from the database."
    