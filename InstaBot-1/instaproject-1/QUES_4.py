follow=driver.find_element_by_xpath("//span[contains(@class,'vBF20')]/button")
follow.click()
print("WE HAVE Followed So Delhi Instagram Handle ")
print()
time.sleep(2)
click=driver.find_element_by_xpath("//div[contains(@class,'Igw0E')]/span/span/button").click()
time.sleep(2)
unfollow=driver.find_element_by_xpath("//div[contains(@class,'RnEpo')]/div/div/div/div[3]/button")
unfollow.click()
print("WE HAVE UNFOLLOWED So Delhi Instagram Handle")
time.sleep(1)