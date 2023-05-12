import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Edge(executable_path = r'.\msedgedriver.exe')
df = pd.read_excel('challenge.xlsx')

driver.get('https://www.rpachallenge.com')

buttonStart = driver.find_element("xpath",'/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
buttonStart.click()


for i, row in df.iterrows():

    field_FirstName = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelFirstName']")
    field_LastName = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelLastName'")
    field_CompanyName = driver.find_element(By.CSS_SELECTOR,"input[ng-reflect-name='labelCompanyName'")
    field_RoleInCompany = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelRole'")
    field_Address = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelAddress'")
    field_Email = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelEmail'")
    field_PhoneNumber = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelPhone'")

    field_FirstName.send_keys(row[0])
    field_LastName.send_keys(row[1])
    field_CompanyName.send_keys(row[2])
    field_RoleInCompany.send_keys(row[3])
    field_Address.send_keys(row[4])
    field_Email.send_keys(row[5])
    field_PhoneNumber.send_keys(row[6])

    buttonSubimt = driver.find_element(By.CSS_SELECTOR, "input[value='Submit']")
    buttonSubimt.click()
    





