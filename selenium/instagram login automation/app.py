from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Replace 'your_username' and 'your_password' with your Instagram credentials
username = "aswinraja8098@gmail.com"
password = "Aswin@2002"

# Provide the correct path to your chromedriver.exe
driver = webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/")

# Wait for the page to load
time.sleep(2)

# Find the username and password input fields and enter credentials
username_field = driver.find_element("name", "username")
username_field.send_keys(username)

password_field = driver.find_element("name", "password")
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Directly access the followers list page


# Wait for the followers modal to appear
followers_modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))

# Scroll the followers modal to load all followers
while True:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
    time.sleep(2)  # Adjust the sleep time as needed
    # Check if the end of the followers list is reached
    end_of_followers = driver.find_element_by_xpath("//div[@role='dialog']//li[last()]")
    if end_of_followers.text == driver.find_elements_by_xpath("//div[@role='dialog']//li")[-1].text:
        break

# Get the usernames of followers
followers = driver.find_elements_by_xpath("//div[@role='dialog']//li//a")

followers_list = []
for follower in followers:
    followers_list.append(follower.text)

# Print the followers list
print("Followers List:")
print(followers_list)

# Close the browser window
driver.quit()
