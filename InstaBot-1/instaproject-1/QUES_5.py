#5 LIKE AND UNLIKE OF POST
search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("dilsefoodie")
time.sleep(3)

name=driver.find_element_by_xpath("//div[@class='uyeeR']/span")
name.click()
time.sleep(5)
#as each div contains 3 post and initialy 4 divs are present so, we have 3*4=12 post therefore we have to scroll 3 times for 30 posts
count=0
while (count<3):
    current_height=driver.execute_script("return document.body.scrollHeight;")
    driver.execute_script("window.scrollTo(0,arguments[0]);",current_height)
    new_height=driver.execute_script("return document.body.scrollHeight;")
    current_height=new_height
    count+=1
#scrolling is done
#liking post
print("LIKE PART")
print()
div="//div[@class=' _2z6nI']/article/div/div/div/div"
click=driver.find_element_by_xpath(div)
click.click()
time.sleep(2)
for i in range(30):
    driver.find_element_by_class_name("fr66n").click()
    print("POST NO ",i+1," IS LIKED")
    driver.find_element_by_xpath("//div[@class='DdSX2']/a[last()]").click()
    time.sleep(4)
#UNLIKE PART
print()
print("UNLIKE PART")
print()
driver.refresh()
time.sleep(5)
search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("dilsefoodie")
time.sleep(3)

name=driver.find_element_by_xpath("//div[@class='uyeeR']/span")
name.click()
time.sleep(5)
#as each div contains 3 post and initialy 4 divs are present so, we have 3*4=12 post therefore we have to scroll 3 times for 30 posts
count=0
while (count<4):
    current_height=driver.execute_script("return document.body.scrollHeight;")
    driver.execute_script("window.scrollTo(0,arguments[0]);",current_height)
    new_height=driver.execute_script("return document.body.scrollHeight;")
    current_height=new_height
    count+=1
#scrolling is done
#liking post
url=driver.current_url
div="//div[@class=' _2z6nI']/article/div/div/div/div"
click=driver.find_element_by_xpath(div)
click.click()
time.sleep(2)
for i in range(30):
    driver.find_element_by_class_name("fr66n").click()
    print("POST NO ",i+1," IS UNLIKED")
    driver.find_element_by_xpath("//div[@class='DdSX2']/a[last()]").click()
    time.sleep(4)
driver.refresh()