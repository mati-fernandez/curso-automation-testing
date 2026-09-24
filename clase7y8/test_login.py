from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_exitoso():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    # Abrir página
    driver.get("https://www.saucedemo.com/")

    time.sleep(2)

    # Localizar elementos
    user = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")   


    # Completar formulario
    user.send_keys("standard_user")
    password.send_keys("secret_sauce")   

    time.sleep(2)

    # Hacer login
    login_button.click()

    # Validar URL después del login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Validar titulo
    titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert titulo.text == "Products"
    
    input("Presiona alguna tecla para cerrar...")

    time.sleep(2)


    driver.quit()

# def test_login_usuario_invalido():
