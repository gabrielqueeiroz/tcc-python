from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    # def __init__(self, driver):
    #     # driver = webdriver.Chrome()
    #     self.driver = driver
    #     start = self.driver.find_element_by_xpath("//*[@id=\"gcrud-search-form\"]/div[1]/div[1]/a")
    #     start.click()
    #     self.name = self.driver.find_element_by_xpath("//*[@id=\"field-customerName\"]")
    #     self.last_name = self.driver.find_element_by_xpath("//*[@id=\"field-contactLastName\"]")
    #     self.contact_first_name = self.driver.find_element_by_xpath("//*[@id=\"field-contactFirstName\"]")
    #     self.phone = self.driver.find_element_by_xpath("//*[@id=\"field-phone\"]")
    #     self.addressLine1 = self.driver.find_element_by_xpath("//*[@id=\"field-addressLine1\"]")
    #     self.addressLine2 = self.driver.find_element_by_xpath("//*[@id=\"field-addressLine2\"]")
    #     self.city = self.driver.find_element_by_xpath("//*[@id=\"field-city\"]")
    #     self.state = self.driver.find_element_by_xpath("//*[@id=\"field-state\"]")
    #     self.postal_code = self.driver.find_element_by_xpath("//*[@id=\"field-postalCode\"]")
    #     self.country = self.driver.find_element_by_xpath("//*[@id=\"field-country\"]")
    #     self.from_employeer = self.driver.find_element_by_xpath("//*[@id=\"field-salesRepEmployeeNumber\"]")
    #     self.credit_limit = self.driver.find_element_by_xpath("//*[@id=\"field-creditLimit\"]")
    #     self.save_button = self.driver.find_element_by_xpath("//*[@id=\"form-button-save\"]")
    #     self.form_message = self.driver.find_element_by_xpath("//*[@id=\"report-success\"]")
    #     self.save_and_back_buttton = self.driver.find_element_by_xpath("//*[@id=\"save-and-go-back-button\"]")

    def initialize_variables(self, driver):
        # driver = webdriver.Chrome()
        self.driver = driver        
        self.name = self.driver.find_element_by_xpath("//*[@id=\"field-customerName\"]")
        self.last_name = self.driver.find_element_by_xpath("//*[@id=\"field-contactLastName\"]")
        self.contact_first_name = self.driver.find_element_by_xpath("//*[@id=\"field-contactFirstName\"]")
        self.phone = self.driver.find_element_by_xpath("//*[@id=\"field-phone\"]")
        self.addressLine1 = self.driver.find_element_by_xpath("//*[@id=\"field-addressLine1\"]")
        self.addressLine2 = self.driver.find_element_by_xpath("//*[@id=\"field-addressLine2\"]")
        self.city = self.driver.find_element_by_xpath("//*[@id=\"field-city\"]")
        self.state = self.driver.find_element_by_xpath("//*[@id=\"field-state\"]")
        self.postal_code = self.driver.find_element_by_xpath("//*[@id=\"field-postalCode\"]")
        self.country = self.driver.find_element_by_xpath("//*[@id=\"field-country\"]")
        self.from_employeer = self.driver.find_element_by_xpath("//*[@id=\"field-salesRepEmployeeNumber\"]")
        self.credit_limit = self.driver.find_element_by_xpath("//*[@id=\"field-creditLimit\"]")
        self.save_button = self.driver.find_element_by_xpath("//*[@id=\"form-button-save\"]")
        self.form_message = self.driver.find_element_by_xpath("//*[@id=\"report-success\"]")
        self.save_and_back_buttton = self.driver.find_element_by_xpath("//*[@id=\"save-and-go-back-button\"]")

    def fillForm01(self, person):
        self.name.sendKeys(person.get("name"))
        self.last_name.sendKeys(person.get("last_name"))
        self.contact_first_name.sendKeys(person.get("contact_first_name"))
        self.phone.sendKeys(person.get("phone"))
        self.addressLine1.sendKeys(person.get("addressLine1"))
        self.addressLine2.sendKeys(person.get("addressLine2"))
        self.city.sendKeys(person.get("city"))
        self.state.sendKeys(person.get("state"))
        self.postal_code.sendKeys(person.get("postal_code"))
        self.country.sendKeys(person.get("country"))
        self.from_employeer.sendKeys(person.get("from_employeer"))
        self.credit_limit.sendKeys(person.get("credit_limit"))
        self.save_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"report-success\"]")))
        assert self.form_message.getText() == "Your data has been successfully stored into the database. Edit Customer or Go back to list"
    
    def fillForm02(self, person):
        self.name.sendKeys(person.get("name"))
        self.last_name.sendKeys(person.get("last_name"))
        self.contact_first_name.sendKeys(person.get("contact_first_name"))
        self.phone.sendKeys(person.get("phone"))
        self.addressLine1.sendKeys(person.get("addressLine1"))
        self.addressLine2.sendKeys(person.get("addressLine2"))
        self.city.sendKeys(person.get("city"))
        self.state.sendKeys(person.get("state"))
        self.postal_code.sendKeys(person.get("postal_code"))
        self.country.sendKeys(person.get("country"))
        self.from_employeer.sendKeys(person.get("from_employeer"))
        self.credit_limit.sendKeys(person.get("credit_limit"))
        self.save_and_back_buttton.click()
    