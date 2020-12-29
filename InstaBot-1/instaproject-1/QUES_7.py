#7
driver.find_element_by_class_name("cq2ai").click()
time.sleep(5)
search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("coding.ninjas")
time.sleep(3)

name=driver.find_element_by_xpath("//div[@class='uyeeR']/span")
name.click()
time.sleep(4)

bio_of_CODING=driver.find_element_by_class_name("-vDIg").text
print(bio_of_CODING)
sty=driver.find_element_by_xpath("//div[contains(@class,RR-M-)]/span/img")
sty.click()
print()
print("WE WILL GET NO ERROR")