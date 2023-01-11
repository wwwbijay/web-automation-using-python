import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# constants
base_url = 'http://192.168.1.216:81/mypayadmin'
maxSigns = 13

# Connect chrome driver
ser = Service("../chromedriver_win32/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
# Open page
driver.get(base_url)
# Select username and password
loginForm = driver.find_element(By.TAG_NAME, 'form')
inputUsername = driver.find_element(By.ID, 'inputUsername')
inputPassword = driver.find_element(By.ID, 'inputPassword')
# Add username and password
inputUsername.send_keys('admin')
inputPassword.send_keys('Admin@123')
# Submit Login form
loginForm.submit()
# Wait for login
time.sleep(3)

# Goto update-daily Page
driver.get(base_url + '/horoscope/update-daily')

for x in range(1, maxSigns):
    # Click "New Daily +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)
    # Add Nepali Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_editor_editor1 .cke_wysiwyg_frame")))
    editor_body = driver.find_element(By.TAG_NAME, 'body')
    # driver.execute_script("arguments[0].innerHTML = '<p>आज नयाँ ज्ञान सिक्ने मौका मिल्नेछ । धैर्य एवं लगनशीलताले अवसर दिलाउनेछ । आर्थिक क्षेत्रमा राम्रो सफलता मिल्नेछ ।</p>'", editor_body)
    editor_body.clear()
    editor_body.send_keys('आज नयाँ ज्ञान सिक्ने मौका मिल्नेछ । धैर्य एवं लगनशीलताले अवसर दिलाउनेछ । आर्थिक क्षेत्रमा राम्रो सफलता मिल्नेछ ।')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_editor_editor2 .cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('These vibes can be particularly troublesome if you don’t get enough alone time, so make sure you’re taking plenty of breaks from socializing in order to recharge between work and personal engagements.')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()

driver.get(base_url + '/horoscope/update-weekly')

for x in range(1, maxSigns):
    # Click "New Daily +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)
    # Add Nepali Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_editor_editor1 .cke_wysiwyg_frame")))
    editor_body = driver.find_element(By.TAG_NAME, 'body')
    # driver.execute_script("arguments[0].innerHTML = '<p>आज नयाँ ज्ञान सिक्ने मौका मिल्नेछ । धैर्य एवं लगनशीलताले अवसर दिलाउनेछ । आर्थिक क्षेत्रमा राम्रो सफलता मिल्नेछ ।</p>'", editor_body)
    editor_body.clear()
    editor_body.send_keys('आज नयाँ ज्ञान सिक्ने मौका मिल्नेछ । धैर्य एवं लगनशीलताले अवसर दिलाउनेछ । आर्थिक क्षेत्रमा राम्रो सफलता मिल्नेछ ।')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_editor_editor2 .cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('These vibes can be particularly troublesome if you don’t get enough alone time, so make sure you’re taking plenty of breaks from socializing in order to recharge between work and personal engagements.')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()


driver.get(base_url + '/horoscope/update-monthly')
for x in range(1, maxSigns):
    time.sleep(2)
    # Click "New Monthly +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('These vibes can be particularly troublesome if you don’t get enough alone time, so make sure you’re taking plenty of breaks from socializing in order to recharge between work and personal engagements.')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()

driver.get(base_url + '/horoscope/update-monthly/np')
for x in range(1, maxSigns):
    # Click "New Daily +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('आज नयाँ ज्ञान सिक्ने मौका मिल्नेछ । धैर्य एवं लगनशीलताले अवसर दिलाउनेछ । आर्थिक क्षेत्रमा राम्रो सफलता मिल्नेछ ।')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()

driver.get(base_url + '/horoscope/update-yearly')
for x in range(1, maxSigns):
    # Click "New Daily +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('These vibes can be particularly troublesome if you don’t get enough alone time, so make sure you’re taking plenty of breaks from socializing in order to recharge between work and personal engagements.')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()

driver.get(base_url + '/horoscope/update-yearly/np')
for x in range(1, maxSigns):
    # Click "New Daily +" button
    newDailyBtn = driver.find_element(By.CSS_SELECTOR, '.page-entry-heading a')
    newDailyBtn.click()
    time.sleep(2)

    # Add English Content to CK Editor
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,".cke_wysiwyg_frame")))
    editor_body1 = driver.find_element(By.TAG_NAME, 'body')
    editor_body1.clear()
    editor_body1.send_keys('These vibes can be particularly troublesome if you don’t get enough alone time, so make sure you’re taking plenty of breaks from socializing in order to recharge between work and personal engagements.')

    # Switch back from iframe to parent content
    driver.switch_to.parent_frame()

    sign_select = Select(driver.find_element(By.ID, "horoscopeId"))
    sign_select.select_by_index(x)

    submitBtn = driver.find_element(By.CSS_SELECTOR, '.modal-footer button[type="submit"]')
    submitBtn.click()


# Wait for 5 seconds before closing browser
driver.quit()
