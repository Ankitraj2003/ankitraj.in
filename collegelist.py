from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd


clg_name=[]
clg_address=[]
clg_url=[]
clg_email=[]
clg_phone=[]
all_clg = []
             

n = int(input("\b Enter 1 for tire 1 city like Mumbai,Delhi,kolkata and Chennai. \n Enter 2 for Capital of every state. \n Enter 3 for every city.  \n Enter = "))


if n==1:
        url = ["http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=DL",
                "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MH&ct=159",
                "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=WB&ct=221",
                "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=1"]



#def tire_one_clg():
        for url in url:
            content= requests.get(url)
            html_content= content.content
       #print(html_content)
            soup = BeautifulSoup(html_content,"html.parser")
            title= soup.title
            clist= soup.find_all("table",{"class":"clg-listing"})
       #print(clist)
            for clist in clist:
                anchor = clist.find_all('a')
      
                for i in range(len(anchor)):
                    all_clg.append(anchor[i]['href'])
                


                
        def new_appending():
            if "College Name" in info_list:
                index= info_list.index('College Name')
                clg_name.append(info_list[index+1])
            else:
                clg_name.append("NULL")
            if "Address" in info_list:
                index= info_list.index("Address")
                clg_address.append(info_list[index+1])
            else:
                clg_address.append("NULL")
            if "Website" in info_list:
                index= info_list.index("Website")
                clg_url.append(info_list[index+1])
            else:
                clg_url.append("NULL")
            if "E-Mail" in info_list:
                index= info_list.index("E-Mail")
                clg_email.append(info_list[index+1])
            else:
                clg_email.append("NULL")
            if "Phone" in info_list:
                index= info_list.index("Phone")
                clg_phone.append(info_list[index+1])
            else:
                clg_phone.append("NULL")


        for link in all_clg:
            r= requests.get(link)
            html= r.content
            soup= BeautifulSoup(html,'html.parser')
            clg_data= soup.find_all("table",{"class":"altcolor1"})
            clg_info=clg_data[0].find_all("td")
            info_list= []
            for i in range(len(clg_info)):
                info_list.append(clg_info[i].text.strip())
            new_appending()     






        df_tire_one= pd.DataFrame({"College Name":clg_name,"Address":clg_address,"Url Address":clg_url,"E-Mail":clg_email,"Phone":clg_phone})
        df_tire_one.to_csv('tire1.csv')
        print("File create sucessfull")
        content.close()

if n==2:
        url = ["http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AN",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AR",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=BR",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=CT",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=DL",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=HR",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=JK",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=KL",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MH",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=ML",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MP",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=NL",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=PB",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=RJ",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=UL",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=WB",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AP",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AS",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=CH",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=DD",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=DN",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=HP",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=JH",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=KA",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=LD",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=ML",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MN",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MZ",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=OR",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=PY",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=SK",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TR",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=UP"]



#def tire_one_clg():
        for url in url:
            content= requests.get(url)
            html_content= content.content
       #print(html_content)
            soup = BeautifulSoup(html_content,"html.parser")
            title= soup.title
            clist= soup.find_all("table",{"class":"clg-listing"})
       #print(clist)
            for clist in clist:
                anchor = clist.find_all('a')
      
                for i in range(len(anchor)):
                    all_clg.append(anchor[i]['href'])
                


                
        def new_appending():
            if "College Name" in info_list:
                index= info_list.index('College Name')
                clg_name.append(info_list[index+1])
            else:
                clg_name.append("NULL")
            if "Address" in info_list:
                index= info_list.index("Address")
                clg_address.append(info_list[index+1])
            else:
                clg_address.append("NULL")
            if "Website" in info_list:
                index= info_list.index("Website")
                clg_url.append(info_list[index+1])
            else:
                clg_url.append("NULL")
            if "E-Mail" in info_list:
                index= info_list.index("E-Mail")
                clg_email.append(info_list[index+1])
            else:
                clg_email.append("NULL")
            if "Phone" in info_list:
                index= info_list.index("Phone")
                clg_phone.append(info_list[index+1])
            else:
                clg_phone.append("NULL")


        for link in all_clg:
            r= requests.get(link)
            html= r.content
            soup= BeautifulSoup(html,'html.parser')
            clg_data= soup.find_all("table",{"class":"altcolor1"})
            if len(clg_data)==0:
                continue
            clg_info=clg_data[0].find_all("td")
            info_list= []
            for i in range(len(clg_info)):
                info_list.append(clg_info[i].text.strip())
            new_appending()     






        df_tire_one= pd.DataFrame({"College Name":clg_name,"Address":clg_address,"Url Address":clg_url,"E-Mail":clg_email,"Phone":clg_phone})
        df_tire_one.to_csv('state.csv')
        print("File create sucessfull")
        content.close()
        
        
        
if n==3:
        url = ["http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MH&ct=159",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=WB&ct=221",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AP&ct=45",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ&ct=68",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ&ct=79",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=4",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=UP&ct=208",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MP&ct=143",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=BR&ct=832",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=KL&ct=142",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=29",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=UP&ct=206",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AP&ct=54",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=UP&ct=203",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=11",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=DL&ct=232",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=1",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=KA&ct=99",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MH&ct=163",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=RJ&ct=190",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=PB&ct=182",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=MH&ct=160",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=BR&ct=63",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AS&ct=57",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ&ct=78",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ&ct=78",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=GJ&ct=912",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=TN&ct=35",
              "http://www.studyguideindia.com/Colleges/Engineering/default.asp?State=AP&ct=53"]



#def tire_one_clg():
        for url in url:
            content= requests.get(url)
            html_content= content.content
       #print(html_content)
            soup = BeautifulSoup(html_content,"html.parser")
            title= soup.title
            clist= soup.find_all("table",{"class":"clg-listing"})
       #print(clist)
            for clist in clist:
                anchor = clist.find_all('a')
      
                for i in range(len(anchor)):
                    all_clg.append(anchor[i]['href'])
                


                
        def new_appending():
            if "College Name" in info_list:
                index= info_list.index('College Name')
                clg_name.append(info_list[index+1])
            else:
                clg_name.append("NULL")
            if "Address" in info_list:
                index= info_list.index("Address")
                clg_address.append(info_list[index+1])
            else:
                clg_address.append("NULL")
            if "Website" in info_list:
                index= info_list.index("Website")
                clg_url.append(info_list[index+1])
            else:
                clg_url.append("NULL")
            if "E-Mail" in info_list:
                index= info_list.index("E-Mail")
                clg_email.append(info_list[index+1])
            else:
                clg_email.append("NULL")
            if "Phone" in info_list:
                index= info_list.index("Phone")
                clg_phone.append(info_list[index+1])
            else:
                clg_phone.append("NULL")


        for link in all_clg:
            r= requests.get(link)
            html= r.content
            soup= BeautifulSoup(html,'html.parser')
            clg_data= soup.find_all("table",{"class":"altcolor1"})
            if len(clg_data)==0:
                continue
            clg_info=clg_data[0].find_all("td")
            info_list= []
            for i in range(len(clg_info)):
                info_list.append(clg_info[i].text.strip())
            new_appending()     






        df_tire_one= pd.DataFrame({"College Name":clg_name,"Address":clg_address,"Url Address":clg_url,"E-Mail":clg_email,"Phone":clg_phone})
        df_tire_one.to_csv('city.csv')
        print("File create sucessfull")
        content.close()



        


           


        



