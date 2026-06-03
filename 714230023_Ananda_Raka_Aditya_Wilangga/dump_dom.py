import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:64852/register")
time.sleep(10) # wait for flutter to load
page_source = driver.page_source
with open("dom_dump.html", "w", encoding="utf-8") as f:
    f.write(page_source)
driver.quit()
