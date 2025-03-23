#Test Case Validacion de Requerimiento 1 de Registro
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import unittest
import random
import string

class TestRegistro(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada test."""
        self.driver = webdriver.Chrome()  
        self.url_registro = "https://pushing-it.vercel.app/"  
        self.driver.get(self.url_registro)
        self.wait = WebDriverWait(self.driver, 7)

        # Esperar a que la página de registro se cargue
        self.wait.until(EC.visibility_of_element_located((By.ID, "field-:r0:-label")))

    def tearDown(self):
        """Cerrar el navegador después de cada test."""
        self.driver.quit()

    def generate_random_alphanumeric(self, length):
        """Genera una cadena alfanumérica aleatoria de la longitud especificada."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

    def generate_random_alphanumeric_with_special(self, length):
        """Genera una cadena alfanumérica aleatoria con al menos un carácter especial."""
        alphanumeric = self.generate_random_alphanumeric(length - 1)
        special_chars = ['_', '&', '#', '%', '@']
        random_special = random.choice(special_chars)
        index = random.randint(0, length - 1)
        return alphanumeric[:index] + random_special + alphanumeric[index:]

    def test_acceso_pagina_registro(self):
        """Test para verificar que se accede correctamente a la página de registro."""
        self.assertEqual(self.driver.current_url, self.url_registro, f"No se accedió a la URL esperada: {self.url_registro}")
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "field-:r0:-label"))), "El campo de usuario no está visible.")
        print("Test de acceso a la página de registro PASSED")

    def test_registro_usuario_valido(self):
        """Test para registrar un usuario con datos válidos."""
        username = self.generate_random_alphanumeric(10)
        password = self.generate_random_alphanumeric_with_special(12)

        self.driver.find_element(By.ID, "user").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)

        # Seleccionar género (ejemplo: Male)
        self.driver.find_element(By.CSS_SELECTOR, 'span[data-cy="Male"]').click()
      

        # Seleccionar fecha de nacimiento (select WebElements)
        day_select = Select(self.driver.find_element(By.NAME, "day")) 
        day_select.select_by_value("1") # Selecciona el día 1

        month_select = Select(self.driver.find_element(By.NAME, "month"))
        month_select.select_by_value("1") # Selecciona el mes de enero

        year_select = Select(self.driver.find_element(By.NAME, "year")) 
        year_select.select_by_value("2000") # Selecciona el año 2000

        # Hacer clic en el botón de registro
        self.driver.find_element(By.ID, "submitForm").click() 

        # Esperar a ser redirigido a la página siguiente 
        try:
            self.wait.until(EC.url_changes(self.url_registro))
            self.assertNotEqual(self.driver.current_url, self.url_registro, "El registro fue exitoso y se redirigió a la siguiente página.")
            print("Test de registro de usuario válido PASSED")
        except:
            self.fail("El registro falló o no se redirigió a la página siguiente.")

    

if __name__ == "__main__":
    unittest.main()