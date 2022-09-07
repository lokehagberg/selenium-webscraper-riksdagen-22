from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

number_list = []

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#s=Service(path)
#driver=webdriver.Chrome(service=s)
driver.get('https://www.hitta.se/s%C3%B6k?vad=v%C3%A4sterort%20stockholms%20l%C3%A4n')

cook = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Jag godkänner')]"))
)

cook.click()

next_exists = len(driver.find_elements(By.XPATH, "//a/span[contains(text(), 'Nästa')]"))

while next_exists >= 1:
    lnth = len(driver.find_elements(By.XPATH, "//span[contains(text(), 'Visa') and contains(text(), '07')]"))
    for i in range(lnth):
        element = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Visa') and contains(text(), '07')]"))
        )
        number_list.append(element.text)
    next = WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Nästa')]"))
    )
    next.click()
print(",".join(number_list))
	