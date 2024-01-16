#---------------------------------------------------------------------------------------
# Script to login and creat commits for github commit history performance             --
#---------------------------------------------------------------------------------------

#C:\Users\Zebu\Documents\GitHub\Personal\Automation\AutoCommit.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from cryptography.fernet import Fernet


# set to how many times you would like to run 
import random
limit = random.choice([1,2,3,4,5,6,7,8,9,10,11,12])

# set up browser
driver = webdriver.Firefox()

# set up fernet
key = Fernet.generate_key()
fernet = Fernet(key)

# Login to github
def loginToGitHub():

    # open github on firefox
    driver.get("https://github.com/login")

    # initailze the user and pass
    email = ""
    # encPassword = 'gAAAA2SCy4hJIor-9_QQRiTxHFl4niaRY-C4GHu0T1mWBe6ZPKjiWoVNB-3ora5mXQe9FJggRgLDhjlmig=='
    # password = fernet.decrypt(encPassword).decode()
    password = ""

    driver.maximize_window()
    enterEmail = driver.find_element("id", "login_field")
    enterEmail.send_keys(email)
    enterPass = driver.find_element("id", "password")
    enterPass.send_keys(password)
    submitLogin = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]")
    submitLogin.click()

    driver.implicitly_wait(1000)

# Seach for the destination repository
def findRepository():
    repoInput = driver.find_element(By.XPATH, "//*[@id='dashboard-repos-filter-left']")
    repoInput.send_keys("Bootcamp")
    driver.implicitly_wait(100)

# Open the bootcamp repo to edit
def openRepository():
    openRepo = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/ul[1]/li[1]/div/div/a")
    openRepo.click()
    # userBtn = driver.find_element(By.XPATH, "//*[@id='dialog-show-dialog-d79c6c8b-1576-4191-b661-cf1e0883dec9']")
    # userBtn.click()
    # repoBtn = driver.find_element(By.Id, "//*[@id='item-454af4ac-fd81-40b0-85ae-f0c0cf02726f']")
    # repoBtn.click()
    # bootcamp = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div/div[2]/turbo-frame/div/div[2]/ul/li[2]/div[1]/div[1]/h3/a")
    # bootcamp.click()

    driver.implicitly_wait(100)


# Open the file to be edited
def openFile():
    # click on file to edit
    file = driver.find_element(By.XPATH, "//*[@id='folder-row-4']/td[2]/div/div/h3/div/a")
    file.click()

    driver.implicitly_wait(100)

# Open the edit page to create a difference to commit
def editRepository():

    # start editing
    editBtn = driver.find_element(By.XPATH, "//*[@id='repos-sticky-header']/div[1]/div[2]/div[2]/div[1]/div[2]/span/a")
    editBtn.click()
    # write to the textbox
    textBox = driver.find_element(By.XPATH, "//*[@id='repo-content-pjax-container']/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[2]/span[2]/input")
    textBox.send_keys("$")

# Commit any changes
def commit():
    commit = driver.find_element(By.XPATH, "//*[@id='repo-content-pjax-container']/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/button")
    commit.click()
    driver.implicitly_wait(100)
    commitConfirm = driver.find_element(By.XPATH, "//*[@id='__primerPortalRoot__']/div/div/div/div[3]/button[2]")
    commitConfirm.click()


# Kill the active browser window
def killDriver():
    driver.quit()


# ----------- Function Calls -------------

count = 0   # always set to 0

loginToGitHub()
findRepository()
openRepository()
openFile()

while (count <= limit):

    editRepository()
    commit()

    count = count + 1

killDriver()
