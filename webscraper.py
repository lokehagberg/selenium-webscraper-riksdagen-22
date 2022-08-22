from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

riksled_mail = []

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#s=Service(path)
#driver=webdriver.Chrome(service=s)
driver.get('https://www.riksdagen.se/sv/ledamoter-partier/')

for i in range(349):
    riksled = driver.find_elements(By.CLASS_NAME, 'fellow-item-container')
    riksled[i].click()
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'riksdagen.se')]"))
    )
    riksled_mail.append(element.text)
    driver.back()

print(",".join(riksled_mail))
	