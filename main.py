import os
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import traceback 

from sentiment import s_emote, scored
from semantic_similarity import c_emote
from set_emotion import e_emote

passed_first_run = False

#number_of_pages= 1690 #31st January 2021
#i =   0

number_of_pages= 165 
i = 64 
                     
while i <= number_of_pages:
    try:
            i += 1
            numberPerPage = 26
            new_df = pd.DataFrame(pd.read_csv("all_cleaned.csv"))
            
            print('\n' + '\n'+ "##############   LOADING  HTML "+str(i)+"  ################## " +'\n' +'\n')
            
            punch_news ="https://punchng.com/all-posts/page/"+str(i)+"/"
            res = requests.get(punch_news)
            soup = BeautifulSoup(res.text, 'html.parser')
            
            print('\n' + '\n'+ "##############   PARSING  HTML    ################## " +'\n' +'\n')
            
            title_boxes = soup.find_all('div', attrs={'class':'post-content'})
            len(title_boxes)
            
            j = 0
            file_write = 0
            while j <= numberPerPage:
                header = title_boxes[j].find(attrs={'class':'post-title'})
                #date = title_boxes[j].find(attrs={'class':'post-date'}).text
                url = header.find('a').attrs['href']
                
                if (url in new_df["Url"].values) :
                    j += 1
                    print('\n' + "##############   URL ALREADY SCRAPED "+str(j)+"  ################## " +'\n')
                    continue
                
                print('\n' + "##############   FINDING ACTUAL DATE "+str(j)+"  ################## " +'\n')
            
                s_res = requests.get(url)
                s_soup = BeautifulSoup(s_res.text, 'html.parser')
                #s_box = soup.find_all('div', attrs={'class':'clearfix'})

                s_box = s_soup.find_all(attrs={'class':'post-date'})                
                datex = s_box[0].text
                datex = datex.replace("st", " ")
                datex = datex.replace("nd", " ")
                datex = datex.replace("rd", " ")
                datex = datex.replace("th", " ")
                datex = datex.replace("Augu", "August")
                datex = datex.strip()
                print('\n' + "Len: "+str(len(s_box)))
                print('\n' + "date: "+ datex)
        
                #22nd November 2022
              
                # Full month format
                full_month_format = "%d %B %Y"

                # Convert the string into a datetime object
                date = datetime.strptime(datex, full_month_format)
                             
                instances = len(new_df[new_df.Date == (str(date.day) + "-" + str(date.month) + "-" + (str(date.year)[-2:]))])                
                instances = instances  + file_write
                j += 1
                
                
                #scrape a specific month only
                #if (date.month != 2):
                    #print('\n' + "##############   DATE MONTH IS NOT 02, SKIPPED "+str(date.month)+"  ################## " +'\n')
                    #break
                
                    
                if instances > 25:
                    print('\n' + "##############   DATE IS COMPLETE: "+str(instances)+"  ################## " +'\n')
                    break
                
                print('\n' + "##############   WRITING TO  FILE,  j: "+str(j)+ " and instances: "+str(instances)+  "  ################ " +'\n')
                
                headLine = header.text.replace("," , "") 
                primary, secondary = c_emote(headLine) 
                
                new = (headLine + "," + primary + "," + secondary + "," + (str(date.day) + "-" + str(date.month) + "-" + (str(date.year)[-2:]))
                +","+ str(date.day)+ "," + str(date.month) + "," + str(date.year) 
                + "," + s_emote(headLine) + "," + scored(headLine) + "," + e_emote(headLine) + "," + url + '\n')
                
                file_write += 1
                with open(os.path.join(os.getcwd(), "all_cleaned.csv"), 'a') as fd: 
                    fd.write(new)
                    fd.close()
                    
                print (new)
    except:
            print('\n' + '\n'+ "##############   ERROR  OCCURED,  SKIPPED: "+str(i)+"  ################## " +'\n' +'\n')
            # printing stack trace
            traceback.print_exc()
            time.sleep(2)
    
    
