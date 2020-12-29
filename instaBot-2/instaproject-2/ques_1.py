#code for searching food in instagram
list_=[]
search=driver.find_element_by_xpath("//div[contains(@class,'MWDvN')]/div[2]/input")
search.send_keys("food")
#time.sleep to load complete data of search food in search bar
time.sleep(3)
names=driver.find_elements_by_xpath("//div[@class='uyeeR']/span")
for i in names:
    if i.text[0]!="#":   #as as-tags starts with # therefore we will not consider it we have to print only instagram handle
        list_.append(i.text)
    if len(list_)==10:
        break
clear=driver.find_element_by_class_name("coreSpriteSearchClear")
clear.click()


#1


follower=[]
no_post=[]

base_url="https://www.instagram.com/"
for i in list_:
    url=base_url+i+"/"
    driver.get(url)
    time.sleep(5)
    followers=driver.find_elements_by_class_name("g47SY")
    follower.append(followers[1].get_attribute("title"))
    driver.find_element_by_xpath("//div[contains(@class,'Nnq7C')]/div/a").click()
    count=0
    time.sleep(5)
    while True:
        t=driver.find_element_by_tag_name("time").text
        if "h" in t:
            count+=1
        elif t=="1d":
            count+=1
        elif t=="2d":
            count+=1
        elif t=="3d":
            count+=1
        else:
            break
        driver.find_element_by_xpath("//div[@class='EfHg9']/div/div/a[last()]").click()
        time.sleep(3)
        
    no_post.append(count)
       
print("Handle","------","Followers","-------","NO. of post")
for i in range(10):
    print(list_[i],"------",follower[i],"-------",no_post[i]


df=pd.DataFrame(list(zip(list_,follower,no_post)),columns=["Handle","Followers","NUMBER OF POST"])
df.head()
df["Followers"]=df["Followers"].str.replace(",","")
top_h=[]
top_follower=[]
print("top 5 which have the highest number of followers")
print()
df["Followers"]=pd.to_numeric(df["Followers"])
for i in df["Followers"].sort_values(ascending=False).index :
    top_h.append(df["Handle"].loc[i])
    top_follower.append(df["Followers"].loc[i])
for i in range(5):
    print(top_h[i],"  ",top_follower[i])


  plt.bar(df["Handle"],df["Followers"],edgecolor='black')
plt.title("BAR graph")
plt.xlabel("HANDLE NAME")
plt.ylabel("Follolwers")
plt.xticks(rotation=90)
plt.show()
plt.bar(df["Handle"],df["NUMBER OF POST"],edgecolor='black')
plt.title("BAR graph")
plt.xlabel("HANDLE NAME")
plt.ylabel("NUMBER OF POST")
plt.xticks(rotation=90)
plt.show()
plt.pie(top_follower[0:5],labels=top_h[0:5],autopct="%.2f")
plt.title("PIE")
plt.show()
  