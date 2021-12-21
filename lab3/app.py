import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver = webdriver.Chrome(executable_path='D:\\study\\sem7\\software-quality\\lab3\\chromedriver.exe')
fb_old_url = 'http://www.fb.com'
fb_actual_url = 'http://www.facebook.com'

first_name = 'Jason'
last_name = 'Stethem'
email = 'cool.boy@bebra.com'
password = '$BiPk1$'
birth_day = '21'
birth_month = 'дек'
birth_year = '2007'
pronounce = 'Он/она: "Поздравьте его/ее с днем рождения!"'

try:
  # task1+2
  chrome_driver.get(url=fb_old_url)

  # task3
  WebDriverWait(chrome_driver, 0).until_not(lambda d: d.current_url == fb_actual_url)

  # task4
  chrome_driver.find_element(By.CSS_SELECTOR, '[data-testid="open-registration-form-button"').click()
  time.sleep(1)

  # task5
  chrome_driver.find_element(By.NAME, 'firstname').send_keys(first_name)
  chrome_driver.find_element(By.NAME, 'lastname').send_keys(last_name)
  time.sleep(1)

  chrome_driver.find_element(By.NAME, 'reg_email__').send_keys(email)
  time.sleep(1)

  chrome_driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys(email)
  time.sleep(1)

  chrome_driver.find_element(By.NAME, 'reg_passwd__').send_keys(password)
  time.sleep(1)

  # task6
  Select(chrome_driver.find_element(By.NAME, 'birthday_day')).select_by_visible_text(birth_day)
  Select(chrome_driver.find_element(By.NAME, 'birthday_month')).select_by_visible_text(birth_month)
  Select(chrome_driver.find_element(By.NAME, 'birthday_year')).select_by_visible_text(birth_year)
  time.sleep(1)

  # task7
  chrome_driver.find_element(By.CSS_SELECTOR, '[data-name="gender_wrapper"] [value="-1"]').click()
  Select(chrome_driver.find_element(By.NAME, 'preferred_pronoun')).select_by_visible_text(pronounce)
  time.sleep(1)

  # task8
  chrome_driver.find_element(By.NAME, 'websubmit').click()
  time.sleep(3600)
except Exception as ex:
  print(ex)
finally:
  chrome_driver.close()
  chrome_driver.quit()