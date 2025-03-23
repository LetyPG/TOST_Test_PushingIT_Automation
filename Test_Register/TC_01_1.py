#Test Case Navegación a la página de registro
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador 
driver = webdriver.Chrome()  # O el navegador que estés utilizando

# URL de la página de registro (reemplaza con la URL real)
url_registro = "https://pushing-it.vercel.app/"

def test_acceso_pagina_registro():
    """
    Test para verificar que se accede correctamente a la página de registro.
    """
    try:
        # Navegar a la página de registro
        driver.get(url_registro)
        print(f"Accedimos a la URL: {url_registro}")

        # Esperar hasta que un elemento clave de la página de registro sea visible
        # Puedes elegir un elemento como el campo de usuario, el campo de contraseña o el botón de registro
        wait = WebDriverWait(driver, 10)
        campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "field-:r0:-label"))) 
        print(f"Se visualiza el campo de usuario con ID: {campo_usuario.get_attribute('id')}")

        # Otra opción sería verificar el título de la página
        titulo_esperado = "Register" # titulo de la página
        assert titulo_esperado in driver.title, f"El título de la página '{driver.title}' no coincide con el esperado '{titulo_esperado}'"
        print(f"El título de la página es correcto: '{driver.title}'")

        print("Test de acceso a la página de registro PASSED")

    except Exception as e:
        print(f"Test de acceso a la página de registro FAILED: {e}")
        raise
    finally:
        # Cerrar el navegador al finalizar el test
        driver.quit()

if __name__ == "__main__":
    test_acceso_pagina_registro()