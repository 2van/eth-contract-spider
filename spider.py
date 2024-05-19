from bs4 import BeautifulSoup
import urllib.request,urllib.error
import urllib.parse


count=0
def main():
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
   
    baseurl="https://etherscan.io/contractsVerified/"
    for i in range(1,10):
         url=baseurl+str(i)
         print(url)
         request = urllib.request.Request(url,headers=head,method="GET")
         response = urllib.request.urlopen(request,timeout=30)
         html=response.read().decode("gbk")
         Parse_html(html)

def Parse_html(html):
    bs = BeautifulSoup(html,"html.parser")
    head = {  
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    t_list=bs.find_all('span',{"data-highlight-target":True}) 


    for item in t_list:
        global count
        url="https://etherscan.io/address/" +item.get('data-highlight-target')+"#code"
        request = urllib.request.Request(url, headers=head, method="GET")
        print("contract:"+url)
        response = urllib.request.urlopen(request,timeout=30)
        contract = response.read().decode("utf-8") 
        ds = BeautifulSoup(contract, "html.parser")
        contract = ds.find_all(class_="js-sourcecopyarea editor")
        text=contract[0]
        result=text.get_text()
        filename =  'Contract-'+str(count)+'.sol'
        count=count+1
        with open(filename, 'w',encoding='utf-8') as file_object:
             file_object.write(str(result))
main()
