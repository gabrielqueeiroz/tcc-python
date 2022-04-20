from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

# classe com casos de teste
class Test(unittest.TestCase):
    # metodo responsavel por inicializar variaveis: driver do chrome, link utilizado para automação e dicionário de dados representando os dados do backend
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url ="https://www.grocerycrud.com/v1.x/demo/my_boss_is_in_a_hurry/bootstrap"
        self.person = {
            "name": "Tcc",
            "last_name": "Gabriel",
            "contact_first_name": "Teste",
            "phone": "92 9999-9999",
            "addressLine1": "Av Darcy Vargas, 1200",
            "addressLine2": "Stem",
            "city": "Manaus",
            "state": "AM",
            "postal_code": "69050-020",
            "country": "Brasil",
            "from_employeer": "Fixter",
            "credit_limit": "200" 
        }

    # caso de teste responsavel por verificar o cadastro de usuario
    def test_registerUser(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.combo_select = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/select/option[4]")
        self.combo_select.click()
        self.add_customer_button = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[1]/div[1]/a")
        self.add_customer_button.click()
        
        self.name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-customerName\"]")
        self.last_name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-contactLastName\"]")
        self.contact_first_name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-contactFirstName\"]")
        self.phone = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-phone\"]")
        self.addressLine1 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-addressLine1\"]")
        self.addressLine2 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-addressLine2\"]")
        self.city = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-city\"]")
        self.state = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-state\"]")
        self.postal_code = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-postalCode\"]")
        self.country = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-country\"]")
        self.from_employeer = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-salesRepEmployeeNumber\"]")
        self.credit_limit = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-creditLimit\"]")
        
        self.name.send_keys(self.person.get("name"))
        self.last_name.send_keys(self.person.get("last_name"))
        self.contact_first_name.send_keys(self.person.get("contact_first_name"))
        self.phone.send_keys(self.person.get("phone"))
        self.addressLine1.send_keys(self.person.get("addressLine1"))
        self.addressLine2.send_keys(self.person.get("addressLine2"))
        self.city.send_keys(self.person.get("city"))
        self.state.send_keys(self.person.get("state"))
        self.postal_code.send_keys(self.person.get("postal_code"))
        self.country.send_keys(self.person.get("country"))
        self.from_employeer.send_keys(self.person.get("from_employeer"))
        self.credit_limit.send_keys(self.person.get("credit_limit"))
        self.save_button = self.driver.find_element(by=By.XPATH, value="//*[@id=\"form-button-save\"]")
        self.save_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"report-success\"]")))
        self.form_message = self.driver.find_element(by=By.XPATH, value="//*[@id=\"report-success\"]")
        self.assertEqual(self.form_message.text, "Your data has been successfully stored into the database. Edit Record or Go back to list")
    
    # caso de teste responsavel por verificar a remoção de usuario
    def test_deleteUser(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.combo_select = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/select/option[4]")
        self.combo_select.click()
        self.add_customer_button = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[1]/div[1]/a")
        self.add_customer_button.click()
        
        self.name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-customerName\"]")
        self.last_name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-contactLastName\"]")
        self.contact_first_name = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-contactFirstName\"]")
        self.phone = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-phone\"]")
        self.addressLine1 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-addressLine1\"]")
        self.addressLine2 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-addressLine2\"]")
        self.city = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-city\"]")
        self.state = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-state\"]")
        self.postal_code = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-postalCode\"]")
        self.country = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-country\"]")
        self.from_employeer = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-salesRepEmployeeNumber\"]")
        self.credit_limit = self.driver.find_element(by=By.XPATH, value="//*[@id=\"field-creditLimit\"]")
        
        self.name.send_keys(self.person.get("name"))
        self.last_name.send_keys(self.person.get("last_name"))
        self.contact_first_name.send_keys(self.person.get("contact_first_name"))
        self.phone.send_keys(self.person.get("phone"))
        self.addressLine1.send_keys(self.person.get("addressLine1"))
        self.addressLine2.send_keys(self.person.get("addressLine2"))
        self.city.send_keys(self.person.get("city"))
        self.state.send_keys(self.person.get("state"))
        self.postal_code.send_keys(self.person.get("postal_code"))
        self.country.send_keys(self.person.get("country"))
        self.from_employeer.send_keys(self.person.get("from_employeer"))
        self.credit_limit.send_keys(self.person.get("credit_limit"))
        self.save_and_back_buttton = self.driver.find_element(by=By.XPATH, value="//*[@id=\"save-and-go-back-button\"]")
        self.save_and_back_buttton.click()
        
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[3]/input")))
        self.search_name = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[3]/input")
        self.update_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/table/thead/tr[2]/td[2]/div[2]/a")
        self.actions_checkbox = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[1]/div/input")
        self.delete_button = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[2]/div[1]/a")
        self.delete_message = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/div/div/div[2]/p[2]")
        self.delete_popup_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/div/div/div[3]/button[2]")
        self.search_name.send_keys(self.person.get("name"))
        self.update_button.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]")))
        self.actions_checkbox.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[2]/td[2]/div[1]/a")))
        self.delete_button.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/div[3]/button[1]")))
        self.assertEqual(self.delete_message.text, "Are you sure that you want to delete this 1 item?")
        self.delete_popup_button.click()
        WebDriverWait(self.driver, 100).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/span[3]/p")))
        self.popup_message = self.driver.find_element(by=By.XPATH, value="/html/body/div[4]/span[3]/p")
        self.assertEqual(self.popup_message.text, "Your data has been successfully deleted from the database.")

    # caso de teste responsavel por verificar o titulo das colunas     
    def test_checkColumns(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        
        column_1 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[1]/th[1]")
        column_2 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[1]/th[2]")
        column_3 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[1]/th[3]")
        column_4 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[1]/th[4]")
        column_5 = self.driver.find_element(by=By.XPATH, value="//*[@id=\"gcrud-search-form\"]/div[2]/table/thead/tr[1]/th[5]")

        self.assertEqual(column_1.text, "Actions")
        self.assertEqual(column_2.text, "CustomerName")
        self.assertEqual(column_3.text, "Phone")
        self.assertEqual(column_4.text, "AddressLine1")
        self.assertEqual(column_5.text, "CreditLimit")

if __name__ == "__main__":
    unittest.main()