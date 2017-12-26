import urllib.request
import urllib.error
import re

headers = ("User-Agent","User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]


url = "http://blog.csdn.net"
data = opener.open(url).read().decode("utf-8")

pat_link = '<a strategy=".*" href="(.*?)" target="_blank">'
pat_title = '<a strategy=".*" href=".*" target="_blank">\s*(.*?)\s*</a>'

all_link = re.compile(pat_link).findall(data)
all_title = re.compile(pat_title).findall(data)

for i in range(len(all_link)):
    print("正在保存：【"+str(i)+"】"+str(all_title[i])+",\t[来自网页]： "+str(all_link[i]))    
    try:       
        urllib.request.urlretrieve(all_link[i],"data\\["+str(i)+"]_"+str(all_title[i])+".html")
    except urllib.error.HTTPError as err:
        print("保存出错：【"+str(i)+"】"+str(all_title[i])+",\t[来自网页]： "+str(all_link[i]))
        print(" 页面返回码为：",end="")
        print(err.code)
        print(err.reason)
    
print("完成")
