#TestCase Validacion Obligatoria de selector de Genero
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


    def test_registro_sin_seleccionar_genero(self):
        """Test para verificar el comportamiento cuando no se selecciona el género."""
        username = self.generate_random_alphanumeric(8)
        password = self.generate_random_alphanumeric_with_special(10)

        self.driver.find_element(By.ID, "user").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID,"submitForm").click()

       
        error_message = self.wait.until(EC.visibility_of_element_located((By.ID, "messageError"))) 
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error al no seleccionar el género.")
        # O si el botón de registro permanece habilitado o la página no cambia
        self.assertTrue(self.driver.find_element(By.ID, "submitForm").is_enabled(), "El botón de registro no debería estar habilitado sin seleccionar el género (esto puede variar).")
        print("Test de no seleccionar género PASSED")


if __name__ == "__main__":
    unittest.main()