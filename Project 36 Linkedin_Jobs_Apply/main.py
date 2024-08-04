from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.linkedin.com/jobs/search/?currentJobId=3980180947&f_AL=true&f_WT=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&spellCorrectionEnabled=true')
sign=driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign.click()
time.sleep(3)
email=driver.find_element(By.XPATH, value='//*[@id="username"]')
email.send_keys("t9940472@gmail.com")
password=driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys("Suraj123456")
button=driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
button.click()

apply=driver.find_element(By.XPATH, value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/div/div/button')
apply.click()

mobile=driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3980180947-2439242377-phoneNumber-nationalNumber"]')
mobile.send_keys("2134445234")

next=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
next.click()
next=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next.click()
experience=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input')
experience.send_keys("0")
experience=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input')
experience.send_keys("0")
review=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
review.click()
submit=driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
submit.click()

