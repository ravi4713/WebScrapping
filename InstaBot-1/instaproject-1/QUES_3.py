search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("So Delhi")
time.sleep(3)
name=driver.find_element_by_xpath("//div[@class='uyeeR']/span")
name.click()
time.sleep(5)
bio_of_sodelhi=driver.find_element_by_class_name("-vDIg").text
print(bio_of_sodelhi)