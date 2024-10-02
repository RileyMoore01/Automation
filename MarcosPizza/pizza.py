
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver (replace with the path to where you have stored your WebDriver)
driver_path = '/path/to/chromedriver'

# Instantiate a browser driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open Marco's Pizza website
driver.get('https://www.marcos.com')

try:
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Close pop-up or cookies consent if needed
    try:
        consent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        consent_button.click()
    except:
        print("No cookies consent popup found, proceeding...")

    # click the menu menu item
    order_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation--mobile"]/div[1]/a[1]')))
    order_button.click()

    # Choose a pizza (This step varies based on the website's current design)
    pizza_selection = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Pizzas"]/div[2]/div[5]/div/div[2]/a')))
    pizza_selection.click()

    # Input the location (zip code or address)
    # location_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'location-input')))
    # location_input.send_keys('79407')  # Replace with desired ZIP code
    # location_input.send_keys(Keys.RETURN)

    # select location
    pizza_selection = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_locations_store_card_LP9M8B"]')))
    pizza_selection.click()

    # continue as guest
    guest_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_signin_guest"]')))
    guest_select.click()

    # select takeout
    takeout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_order_type_2"]/label/span')))
    takeout_button.click()

    # continue
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_order_type_continue"]')))
    continue_button.click()

    # Proceed to checkout
    checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_cart_checkout"]')))
    checkout_button.click()

    # click no thanks
    no_thanks_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_upsale_close"]')))
    no_thanks_button.click()

    # Here you might need to log in or provide payment information
    # This part is website-specific and may require additional interactions.

    print("Order placed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)  # Wait a few seconds before closing to observe actions (if needed)
    driver.quit()
