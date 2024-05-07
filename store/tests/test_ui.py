from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI:
    def setup_method(self):
        self.driver = webdriver.Chrome()  # Ou `webdriver.Firefox()`

    def teardown_method(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.get("http://localhost:8000/billets/")
        assert "Billets" in self.driver.title

        # Test de l'ajout d'un article au panier
        self.driver.find_element(By.XPATH, "//button[text()='Ajouter au panier']").click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost:8000/panier/")
        )
        assert "Panier" in self.driver.title

    def test_checkout(self):
        self.driver.get("http://localhost:8000/panier/")
        assert "Panier" in self.driver.title

        # Test du processus de paiement
        self.driver.find_element(By.XPATH, "//button[text()='Procéder au paiement']").click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost:8000/confirmation_paiement/")
        )
        assert "Paiement Réussi" in self.driver.title
