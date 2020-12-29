search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("food")
#time.sleep to load complete data of search food in search bar
time.sleep(3)
names=driver.find_elements_by_xpath("//div[@class='uyeeR']/span")
print("LIST OF ALL INSTAGRAM HANDLES ARE AS FOLLOWS : ")
print()
for i in names:
    if i.text[0]!="#":   #as as-tags starts with # therefore we will not consider it we have to print only instagram handle
        print(i.text)
clear=driver.find_element_by_class_name("coreSpriteSearchClear")
clear.click()