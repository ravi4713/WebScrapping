#2



hash_tag=[]
base_url=base_url="https://www.instagram.com/"
for i in top_h[:5]:
    driver.get(base_url+i+"/")
    time.sleep(5)
    driver.find_element_by_xpath("//div[contains(@class,'Nnq7C')]/div/a").click()
    time.sleep(2)
    for i in range(10):
        try:
            hash_=driver.find_elements_by_class_name("xil3i")
            for i in hash_:
                hash_tag.append(i.text)
            driver.find_element_by_xpath("//div[@class='EfHg9']/div/div/a[last()]").click()
            time.sleep(3)
        except NoSuchElementException:
            pass

df=pd.DataFrame(hash_tag)
f=[]
h=[]
for i in df[0].value_counts().values[1:]:
    f.append(i)
for i in df[0].value_counts().index[1:]:
    h.append(i)

for i in range(5):
    print(h[i]," : ",f[i])

csv_=pd.DataFrame(list(zip(h,f)),columns=["Hashtag","frequency"])
csv_.head()

plt.pie(f[:5],labels=h[:5],autopct="%.2f")
plt.show()

