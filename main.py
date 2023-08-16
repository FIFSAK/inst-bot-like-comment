import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import random

NoSuchElementException

def like_posts_by_hashtag(username, password, hashtag):
    # Set up ChromeDriver options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Set up ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Log in to Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(7)

    # Go to the hashtag page
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(5)  # Increase the delay
    # Click on the first thumbnail to open the first post
    driver.find_element(By.CSS_SELECTOR, "html").click()  # Use a different CSS selector
    time.sleep(4)
    comments = ["Супер", "классно", "очень красиво"]
    while True:
        try:
            # Click on the like button
            driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Like']").click()
            time.sleep(2)
            # Click on the comment button
            comment_button = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Comment']")
            comment_button.click()
            time.sleep(2)
            
            # Find the comment input field and add your comment
            comment_input = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']")
            comment_input.send_keys(random.choice(comments))
            comment_input.send_keys(Keys.RETURN)
            time.sleep(4)
            # next post
            driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Next']").click()

            time.sleep(2)
        except Exception as e: 
            print(e)
            break

    # Close the ChromeDriver instance
    driver.quit()


if __name__ == "__main__":
    username = ""
    password = ""

    hashtag = input("Enter the hashtag: ")
    like_posts_by_hashtag(username, password, hashtag)