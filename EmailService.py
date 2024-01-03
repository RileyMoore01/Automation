#---------------------------------------------------------------------------------------
# Automated email service scheduled by windows task scheduler                         --
#---------------------------------------------------------------------------------------

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# set up browser
firefoxOptions = Options()
firefoxOptions.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
service = Service()
driver = Firefox(service=service, options=firefoxOptions)

# Open outlook
def openOutlook():

    # make a global function to decrypt password
    email = "riley_moore1@outlook.com"
    password = "Scooter2."

    # open github on firefox
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=19&ct=1704299547&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f0%252f%253fstate%253d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3df5130bb1-0d74-0b2d-0227-96079bc57019&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
    driver.maximize_window()

    # signInKey = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/section/div/div/div[1]/div/div[3]/div[1]/a")
    # signInKey.click()

    enterEmail = driver.find_element(By.XPATH, "//*[@id='i0116']")
    enterEmail.send_keys(email)

    submitEmail = driver.find_element("id", "idSIButton9")
    submitEmail.click()

    driver.implicitly_wait(10)

    enterPass = driver.find_element(By.XPATH, "//*[@id='i0118']")
    enterPass.send_keys(password)
    
    submitPass = driver.find_element("id", "idSIButton9") 
    submitPass.click()

    denySave = driver.find_element(By.XPATH, "//*[@id='idBtn_Back']")
    denySave.click()

    driver.implicitly_wait(10)

    
# Open a new email to send 
def openNewEmail():
    newEmail = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/span/button[1]")
    newEmail.click()

# Fill out email
# def populateEmail():

    
# Kill the active browser window
def killDriver():
    driver.quit()


# ----------- Function Calls -------------

openOutlook()
openNewEmail()
# populateEmail()

killDriver()
