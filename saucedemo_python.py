from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.saucedemo.com/")

# Verify  title for Swag Labs
try:
    logo = driver.find_element("xpath","//*[@id='root']/div/div[1]")
    assert "Swag Labs" in logo.text
    print("Swag Labs present in the web page")
except NoSuchElementException:
    assert False, "Swag Labs not present in the web page, ending the execution"
    driver.close()

#Login                                        
username = driver.find_element("xpath","//*[@id='user-name']")
username.clear()
username.send_keys("standard_user") 
pwd = driver.find_element("xpath","//*[@id='password']")
pwd.clear()
pwd.send_keys("secret_sauce") 
login_button = driver.find_element("xpath","//*[@id='login-button']")
login_button.click()

# Add item to cart
shopping_item = driver.find_element("xpath","//button[contains(text(), 'Add to cart')]")
shopping_item.click()

#click cart
shopping_cart = driver.find_element("xpath","//*[@id='shopping_cart_container']/a")
shopping_cart.click()

# Verify item added to cart
try:
    cart_item = driver.find_element("xpath","//*[@id='cart_contents_container']/div/div[1]/div[3]/div[1]")
    assert cart_item is not None
    print("Item added to cart.")
except NoSuchElementException:
    assert False, "No items added to cart."
     
        
         
menu_button = driver.find_element("xpath","//*[@id='react-burger-menu-btn']") 
menu_button.click()

logout_button = driver.find_element("xpath","//*[@id='logout_sidebar_link']")
logout_button.click()

driver.quit()
