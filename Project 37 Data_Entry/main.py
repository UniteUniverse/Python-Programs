from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://appbrewery.github.io/Zillow-Clone/')
appartment_links=[]
price_list=[]
address_list=[]
links=driver.find_elements(By.CSS_SELECTOR, value='#zpid_2056905294 > div > div.StyledPropertyCardPhotoWrapper > div.StyledPropertyCardPhotoBody > a')
price=driver.find_elements(By.CSS_SELECTOR, value='#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > div.StyledPropertyCardDataArea-fDSTNn > div > span')
address=driver.find_elements(By.CSS_SELECTOR, value='#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a > address')
for i in range(len(links)):
    appartment_links.append(links[i].get_attribute('href'))
    price_list.append(price[i].text.split('+')[0].split('/')[0])
    address_list.append(address[i].text.replace('|','').replace('#',''))
    i+=1

for i in range(len(address_list)):
    driver.get(url='https://docs.google.com/forms/d/e/1FAIpQLScBRl1GxRnS-61RnrZ5pys4Mq51lJiiJFv3R8Sl-Ddw77pbdA/viewform?usp=sf_link')
    time.sleep(1)
    adress_input=driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adress_input.send_keys(f"{address_list[i]}")
    price_input=driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(f'{price_list[i]}')
    link_input=driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(f"{appartment_links[i]}")
    submit=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    i+=1
    time.sleep(1)
driver.quit()