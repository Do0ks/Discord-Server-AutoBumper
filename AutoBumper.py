from datetime import datetime
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import FirefoxProfile

sleep = time.sleep

x = 0

def bump():
    try:
        now = datetime.now()
        timedate = now.strftime("%d/%m/%Y - %H:%M:%S")
        global x
        global a
        x=x+1

        #google this.
        profile = FirefoxProfile("Your_Firefox_Profile_Location")
        s=Service('Your_Geckodriver_Location')

        driver = webdriver.Firefox(profile, service=s)
        driver.maximize_window()
        # This should work out of the box for discord.me, if not you can use the selenium addon for firefox to get the code.
        driver.get("https://discord.me/dashboard")
        driver.execute_script("window.scrollBy(0,250)")
        driver.find_element(By.LINK_TEXT, "Bump Server").click()
        sleep(1)
        driver.find_element(By.ID, "bump-server-submit").click()
        sleep(1)
        # Add your servers bump url for disboard.org. Right click "bump", copy URL.
        driver.get("YOUR_URL_HERE")
        sleep(3)
        driver.close()
        print("Bump'd @: " + str(timedate) + "!")
        x=0
    except:
        while x < 5:
            print("That's weird.. Retrying (" +str(x) +" of 5)..")
            driver.close()
            x+1
            bump()
        else:
            print("To many trys.. Restarting script.")
            x = 0
            s.start()

bump()

a = schedule.every(2).hours.do(bump)

while True:
    schedule.run_pending()
    sleep(1)
