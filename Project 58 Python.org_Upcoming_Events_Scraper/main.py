from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")
list_item=1
events_list=[]
events_date_list=[]
for list_item in range(1,6):
    events=driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{list_item}]/a')
    events_date=driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{list_item}]/time')
    events_list.append(events.text)
    events_date_list.append(events_date.text)
    list_item+=1
dictionary={}
for i in range(len(events_list)):
    dictionary[i]={'time':events_date_list[i], 'name':events_list[i]}
    i+=1
print(dictionary)
driver.quit()


