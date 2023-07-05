[id]
driver.find_element_by_id("main").click()
driver.find_element(By.ID,"main").click() 

[class]
class_arr1 = driver.find_elements_by_id("Form-Input")
class_arr2 = driver.find_elements(By.CLASS_NAME,"Form-Input") 

[XPath]
driver.find_element_by_xpath("/html/body/form/div/input").send_keys("textarea1")
driver.find_element(By.XPATH,"/html/body/form/div/input").send_keys("textarea2") 

[CSS Selector]
driver.find_element_by_css_selector("body > form > div > textarea").send_keys("text1")
driver.find_element(By.CSS_SELECTOR,"body > form > div > textarea").send_keys("text2") 

[単数・複数]
driver.find_element(By.NAME,"name").send_keys("xxx")
driver.find_elements(By.NAME,"name").send_keys("xxx")


