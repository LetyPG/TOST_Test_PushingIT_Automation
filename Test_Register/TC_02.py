#Test Case Requerimiento Invalido de User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import unittest
import random
import string

class TestRegistroError(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada test."""
        self.driver = webdriver.Chrome()  
        self.url_registro = "https://pushing-it.vercel.app/"  
        self.driver.get(self.url_registro)
        self.wait = WebDriverWait(self.driver, 6)

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
    def test_registro_usuario_min_length(self):
        """Test para verificar el límite mínimo de caracteres en el campo de usuario."""
        username = self.generate_random_alphanumeric(2)
        password = self.generate_random_alphanumeric_with_special(8) # Longitud arbitraria para este test

        self.driver.find_element(By.ID, "user").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'span[data-cy="Female"]').click()
        self.driver.find_element(By.ID, "submitForm").click()
        

        # Verificar el mensaje de error o que el registro no se completó
        # Esto dependerá de cómo la aplicación maneja los errores de validación
        error_message = self.wait.until(EC.visibility_of_element_located((By.ID, "messageError"))) 
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error para el usuario con longitud mínima.")
        print("Test de límite mínimo de usuario PASSED")

    def test_registro_usuario_max_length(self):
        """Test para verificar el límite máximo de caracteres en el campo de usuario."""
        username = self.generate_random_alphanumeric(80)
        password = self.generate_random_alphanumeric_with_special(8) # Longitud arbitraria

        self.driver.find_element(By.ID, "user").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'span[data-cy="Female"]').click()
        self.driver.find_element(By.ID, "submitForm").click()

        # Similar al test anterior, verifica el mensaje de error
        error_message = self.wait.until(EC.visibility_of_element_located((By.ID, "messageError"))) 
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error para el usuario con longitud máxima.")
        print("Test de límite máximo de usuario PASSED")

    def test_registro_usuario_caracteres_no_alfanumericos(self):
        """Test para verificar que el campo de usuario solo acepta caracteres alfanuméricos."""
        username = "usuario!/(/)"
        password = self.generate_random_alphanumeric_with_special(8)

        self.driver.find_element(By.ID, "user").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'span[data-cy="Female"]').click()
        self.driver.find_element(By.ID, "submitform").click()

        # Verifica el mensaje de error
        error_message = self.wait.until(EC.visibility_of_element_located((By.ID, "messageError"))) 
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error para caracteres no alfanuméricos en el usuario.")
        print("Test de caracteres no alfanuméricos en usuario PASSED")

    
        

if __name__ == "__main__":
    unittest.main()