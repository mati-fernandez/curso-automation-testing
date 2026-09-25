from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_exitoso():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    # Abrir página
    driver.get("https://www.saucedemo.com/")


    # Localizar elementos
    user = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "user-name"))
)
    password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)    
    login_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "login-button"))
)

    # Completar formulario
    user.send_keys("standard_user")
    password.send_keys("secret_sauce")   

    # Hacer login
    login_button.click()

    # Validar URL después del login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Validar titulo
    titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert titulo.text == "Products"
    
    driver.quit()

# def test_login_usuario_invalido():
