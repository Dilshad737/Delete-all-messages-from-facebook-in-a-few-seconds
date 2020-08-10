from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time

options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.facebook.com/messages/t/")

wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.ID, 'email'))).send_keys("Your email")
wait.until(EC.visibility_of_element_located((By.ID, 'pass'))).send_keys("Your password")
wait.until(EC.element_to_be_clickable((By.ID, 'loginbutton'))).click()
print("\n\nLogged in ...")

while True:
	try:
		driver.find_element_by_id("dots-3-horizontal").click()
		actions = ActionChains(driver)

		actions.send_keys(Keys.ARROW_DOWN *3, Keys.SPACE ).perform()

		actions.send_keys(Keys.TAB, Keys.SPACE).perform()
		time.sleep(0.5)
	except:
		print("\nMessages deleted.")
		break

time.sleep(2)
driver.refresh()
time.sleep(3)
print("\n\nProcess complete. \nIf some messages aren't deleted, run the script again.\n")
driver.close()
