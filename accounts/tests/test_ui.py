# accounts/tests/test_ui.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI:
    def setup_method(self):
        self.driver = webdriver.Chrome()  # Ou `webdriver.Firefox()`

    def teardown_method(self):
        self.driver.quit()

    def test_signup_page(self):
        self.driver.get("http://localhost:8000/signup/")
        assert "Inscription" in self.driver.title

        # Test de l'inscription avec un nouveau compte
        self.driver.find_element(By.ID, "username").send_keys("nouveau_user")
        self.driver.find_element(By.ID, "password").send_keys("nouveau_password")
        self.driver.find_element(By.XPATH, "//button[text()='Inscription']").click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost:8000/")
        )
        assert "Accueil" in self.driver.title

    def test_login_page(self):
        self.driver.get("http://localhost:8000/login/")
        assert "Connexion" in self.driver.title

        # Test de la connexion avec un compte existant
        self.driver.find_element(By.ID, "username").send_keys("existant_user")
        self.driver.find_element(By.ID, "password").send_keys("existant_password")
        self.driver.find_element(By.XPATH, "//button[text()='Connexion']").click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost:8000/")
        )
        assert "Accueil" in self.driver.title
