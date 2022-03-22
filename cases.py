from selenium import webdriver
from HomePage import HomePage
from FormPage import FormPage

person = {
    "name", "Tcc" ,
    "last_name", "Gabriel" ,
    "contact_first_name", "Teste" ,
    "phone", "92 9999-9999" ,
    "addressLine1", "Av Darcy Vargas, 1200" ,
    "addressLine2", "Stem" ,
    "city", "Manaus" ,
    "state", "AM" ,
    "postal_code", "69050-020" ,
    "country", "Brasil" ,
    "from_employeer", "Fixter" ,
    "credit_limit", "200" 
}


driver = webdriver.Chrome()
url ="https://www.grocerycrud.com/v1.x/demo/my_boss_is_in_a_hurry/bootstrap"
driver.get(url)
home = HomePage()
form = FormPage()


def registerUser():
    home.initialize_variables(driver)
    home.addCustomer()
    form.initialize_variables(driver)
    form.fillForm01(person)

def deleteUser():
    home.addCustomer()
    form.fillForm02(person)
    home.deleteCustomer(person.get("name"))

registerUser()
deleteUser()