print("Followers of foodtalkindia")
print()
def get_followers_username(handle_name):
    driver.get('https://instagram.com/'+handle_name)

    # wait till page is loaded
    wait = WebDriverWait(driver,20) #all imports done on top . No need to import again
    followers = wait.until(EC.presence_of_element_located( (By.PARTIAL_LINK_TEXT, 'followers') ))
    driver.execute_script('arguments[0].click()',followers)        

    time.sleep(2) # wait to get list of followers displayed

    while True:
        # locate any element on pop_up page
        obj_created_for_pop_up_scroll = driver.find_element_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
        followers_list = driver.find_elements_by_class_name('wFPL8')
        if len(followers_list) >= 500:
            break
        obj_created_for_pop_up_scroll.send_keys(Keys.END)
        time.sleep(2) # wait to load new followers

    for i in range(500):
        print(str(i+1)+") ",followers_list[i].get_attribute('innerHTML'))
        
# Get usernames of followers of foodtalkindia
get_followers_username('foodtalkindia')
print()
print("FOLLOWERS OF sodelhi")
print()
get_followers_username('sodelhi')

########################################################################
#6 2
def get_followers_username(handle_name):
    l1=[]
    driver.get('https://instagram.com/'+handle_name)

    # wait till page is loaded
    wait = WebDriverWait(driver,20) #all imports done on top . No need to import again
    followers = wait.until(EC.presence_of_element_located( (By.PARTIAL_LINK_TEXT, 'followers') ))
    driver.execute_script('arguments[0].click()',followers)        

    time.sleep(2) # wait to get list of followers displayed

    while True:
        # locate any element on pop_up page
        obj_created_for_pop_up_scroll = driver.find_element_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
        followers_list = driver.find_elements_by_class_name('wFPL8')
        if len(followers_list) >= 202:
            break
        obj_created_for_pop_up_scroll.send_keys(Keys.END)
        time.sleep(2) # wait to load new followers
    for i in range(len(followers_list)):
        l1.append(followers_list[i].get_attribute('innerHTML'))
    return l1
def get_following_username(handle_name):
    l1=[]
    driver.get('https://instagram.com/'+handle_name)

    # wait till page is loaded
    wait = WebDriverWait(driver,20) #all imports done on top . No need to import again
    followers = wait.until(EC.presence_of_element_located( (By.PARTIAL_LINK_TEXT, 'following') ))
    driver.execute_script('arguments[0].click()',followers)        

    time.sleep(2) # wait to get list of followers displayed

    while True:
        # locate any element on pop_up page
        obj_created_for_pop_up_scroll = driver.find_element_by_xpath('//a[contains(@class,"FPmhX notranslate")]')
        following_list = driver.find_elements_by_class_name('wFPL8')
        if len(following_list) >= 220:
            break
        obj_created_for_pop_up_scroll.send_keys(Keys.END)
        time.sleep(2) # wait to load new followers
    
    for i in range(len(following_list)):
        l1.append(following_list[i].get_attribute('innerHTML'))
    return l1
    
l1=get_followers_username("foodtalkindia")#followers of foodtalkindia
l2=get_followers_username("rungta.ravi")#my followers
l3=get_following_username("rungta.ravi")#my following
for i in l1:#we will see all the followers of foodtalkindia 
    for j in l3:#and also of my account
        if i==j:#if my following equal to followers of foodindiatalk
            if i not in l2:#and if it is not present in ny followers than print
                print(i)      