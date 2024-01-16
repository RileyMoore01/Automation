#---------------------------------------------------------------------------------------
# 1.) If something breaks, ensure that the order of operations is correct             --
# 2.) Ensure that the element id's are correct                                        --              
# 3.) Query should always remain the same but in some odd case check it               --
#---------------------------------------------------------------------------------------

# Database connection
import PCCAPythonDatabase as Database
Database.SetConnectionServer("prod")

# Screen scraping tools.
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import json #To convert some python structures to JSON for a request.

def UpdatePassword():

    # ----------------------   Query needed to retreive passwords and ids  -----------------
    query = f"""
        SELECT user_id, trim(password)
        FROM someDatabaseHere
        WHERE active = '1'
    """

    cursor = Database.ExecuteQuery('Transmissions', query)
    # --------------------------------------------------------------------------------------

    # Set up the browse
    firefoxOptions = Options()
    firefoxOptions.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    service = Service()

    # open the ewr web page
    driver = Firefox(service=service, options=firefoxOptions)
    driver.maximize_window()
    driver.implicitly_wait(0.5)
    driver.get("https://www.ewrinc.com/cotton/Default.aspx")

    # update the password for each account
    for row in cursor.fetchall():
        
        # Set the user and password
        user_name = row[0]
        password = row[1]

        # were all inactive on gintool. made the change to the table
        # may have to do this everytime if it continues to not update the profileEWR table
        # if user_name != "G50083" and user_name != "G70116" and user_name != "Miller" and user_name != "GREGP " and user_name != "GULF11" and user_name != "GULF12":

        # Start clicking elements on the page according to id
        login = driver.find_element("id","Main_lvWelcome_lnkLogOut")
        login.click()

        # Enter the username and password here
        userDriver = driver.find_element("id", "Main_lgMain_UserName")
        userDriver.send_keys(user_name)

        passwordDriver = driver.find_element("id", "Main_lgMain_Password")
        passwordDriver.send_keys(password)

        # login with credentials 
        login = driver.find_element("id","Main_lgMain_LoginButton")
        login.click()

        # Go to account settings
        account = driver.find_element("id", "lvWelcome_lnkPreferences")
        account.click()

        # Go to reset password link
        resetPass = driver.find_element("id", "Main_btnResetPassword")
        resetPass.click()

        # Enter the same password for current, new pass, and confirm new pass -----------------
        curPassword = driver.find_element("id", "Main_txtOldPassword")
        curPassword.send_keys(password)

        newPass = driver.find_element("id", "Main_txtPassword1")
        newPass.send_keys(password)

        confirmPass = driver.find_element("id", "Main_txtPassword2")
        confirmPass.send_keys(password)

        # --------------------------------------------------------------------------------------

        # Save the new password
        save = driver.find_element("id", "Main_btnSave")
        save.click()

        # cancel for testing
        # cancel = driver.find_element("id", "Main_btnCancel")
        # cancel.click()

        logout = driver.find_element("id", "lvWelcome_lsWelcome")
        logout.click()

    # Kill the driver (web page)
    driver.quit()


# ------------------------------------------------------------------------------------
# Execute functions

UpdatePassword()
