
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def document_initialised(driver):
    return driver.find_element(By.ID, 'choice-1685059209622')
quitte = False

nombre_aleatoire = random.randint(3, 5)
(str(nombre_aleatoire) + "s")
driver = webdriver.Chrome()
driver.get('https://www.surveylegend.com/s/4zfi')
driver.implicitly_wait(nombre_aleatoire)
WebDriverWait(driver, timeout=10).until(document_initialised)

# Boucle pour répéter l'opération 10 fois
for _ in range(10000):
    try:
        # Initialisation du pilote Chrome WebDriver
        if(quitte):
            nombre_aleatoire = random.randint(3, 5)
            (str(nombre_aleatoire) + "s")
            driver = webdriver.Chrome()
            driver.get('https://www.surveylegend.com/s/4zfi')
            driver.implicitly_wait(nombre_aleatoire)
            WebDriverWait(driver, timeout=10).until(document_initialised)
            quitte = False

        # Sélection de la reine et soumission du vote
        start = time.time()
        reine_element = driver.find_element(By.ID, 'choice-1685059209622')
        reine_element.click()
        submit_button = driver.find_element(By.CLASS_NAME, 'my-enter-button')
        submit_button.click()
        end = time.time()
        duree = start - end

        driver.delete_cookie("surveylegend.com")
        driver.delete_cookie("s.surveylegend.com")
        # Fermeture du pilote Selenium
        driver.refresh()

        print(str(_ + 1) + " vote - Confirmation : Succès")

        # Temps d'attente aléatoire entre 0 secondes et 10 s
        wait_time = random.randint(0, int(duree)+1)
        time.sleep(wait_time)



    except NoSuchElementException as e:
        quitte = True
        print("Élément non trouvé : ", str(e))
        print(str(_ + 1) + " vote - Confirmation : Échec")
        driver.quit()


    except Exception as e:
        print("Erreur inattendue : ", str(e))
        print(str(_ + 1) + " vote - Confirmation : Échec")
