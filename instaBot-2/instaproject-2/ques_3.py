top_5_followers_handle_name=['dilsefoodie','foodtalkindia','foodbossindia','food_lunatic','food']
total=[]
def get_likes(handle_name):
    driver.get('https://instagram.com/'+handle_name)

    
    time.sleep(4) # wait to get list of followers displayed
    driver.find_element_by_xpath("//div[contains(@class,'Nnq7C')]/div/a").click()
    time.sleep(2)
    likes_=[]
    for i in range(10):
        oth=driver.find_element_by_xpath("//section[contains(@class,'EDfFK')]/div/div/button")
        oth.click()
        new_=[1]
        l=0
        while True:
            
            time.sleep(3)
            obj_created_for_pop_up_scroll = driver.find_elements_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
            likes=driver.find_elements_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
            last_name=likes[-1].get_attribute('innerHTML')
            obj_created_for_pop_up_scroll[1].send_keys(Keys.END)
            
            time.sleep(2) # wait to load new likes
            new_=driver.find_elements_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
            l+=len(new_)
            if last_name==new_[-1].get_attribute('innerHTML'):
                break
            
        close=driver.find_elements_by_class_name("QBdPU")
        close[-1].click()
        likes_.append(l)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='EfHg9']/div/div/a[last()]").click()
        time.sleep(3)
    print(likes_)
    total.append(sum(likes_))
        

    
        
# Get usernames of followers of foodtalkindia
for i in top_5_followers_handle_name:
    get_likes(i)
print('Total Likes')
print(total)

print("AVERAGE LIKE OF POST")
print()
for i in range(5):
    print(top_5_followers_handle_name[i]," : ",int(total[i]/10))
followers_5=[518066,297867,155856,84695,47178]
print()
print("average followers:like")
print()
for i in range(5):
    print(top_5_followers_handle_name[i]," : ",((total[i]/10)/followers_5[i]))
	
plt.bar(top_5_followers_handle_name,followers_5)
plt.title("BAR graph")
plt.xlabel("HANDLE NAME")
plt.ylabel("Follolwers")
plt.xticks(rotation=90)
plt.show()

plt.bar(top_5_followers_handle_name,total)
plt.title("BAR graph")
plt.xlabel("HANDLE NAME")
plt.ylabel("Total likes of first 10 post")
plt.xticks(rotation=90)
plt.show()
