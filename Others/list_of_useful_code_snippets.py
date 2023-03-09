import os
'''
# remove , from the last line of some rows
file1 = open(os.path.join(os.getcwd(), "sorted2.csv"),"r")
Lines = file1.readlines()

for line in Lines:
    if "," in str(line[-3:]):
        line = line[:-2]
        print((line + '\n'))
        
    new = (line + '\n')
                                                
    with open(os.path.join(os.getcwd(), "commaFree.csv"), 'a') as fd: 
        fd.write(new)
        fd.close()
                                 
print(len(Lines))
'''
'''
# remove , empty lines from csv file
import csv

in_fnam = os.path.join(os.getcwd(), "all.csv")
out_fnam = os.path.join(os.getcwd(), "clean.csv")



with open(in_fnam, newline='') as in_file:
    with open(out_fnam, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)
'''

'''
# remove double ,,
file = os.path.join(os.getcwd(), "day_sorted.csv")

# Read in the file
with open(file, "r") as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace(",,", ",")

# Write the file out again
with open("all.csv", "w") as file:
    file.write(filedata)
'''

'''
# Convert word2vectors
import os
from gensim.models import KeyedVectors

filepath = os.path.join(os.getcwd(), "vectors.vec") #"vectors.kv")
model = KeyedVectors.load_word2vec_format(filepath, binary=False)

model.save("word2vectors.vec")



#model = KeyedVectors.load(filepath)
'''

'''
# set date to acceptable format

# delete a column from the data frame and apply changes
#df.drop(columns = "Empty", axis="columns", inplace=True)

def scored(day, month, year):
        year = str(year)
        new = str(day) + "-" + str(month) + "-" + year[-2:]
        return new
 
df["Date"] = df.apply(lambda row: scored(row.Day, row.Month, row.Year), axis="columns")

'''

'''
# remove date that appears in some rows

file1 = open(os.path.join(os.getcwd(), "day_sorted.csv"),"r")
Lines = file1.readlines()

def findIndexOfOccurence(ini_str, sub_str, occurrence):
    #Finding nth occurrence of substring 
     val = -1
     for i in range(0, occurrence): 
         val = ini_str.find(sub_str, val + 1) 
     return val
             
first = Lines[0].count(",")
print(first)
for line in Lines:
    data = line.split(",")
    if "2021" in data[-2] or "2022" in data[-2]:
        phrase = line[(findIndexOfOccurence(line, ",", first -1) ): findIndexOfOccurence(line, ",", first)]
        before_phrase, temp_phrase, after_phrase = line.partition(phrase)
        line = before_phrase + after_phrase
        print(phrase)
                                      
    with open(os.path.join(os.getcwd(), "final_sorted.csv"), 'a') as fd: 
        fd.write((line))
        fd.close()
        
print(len(Lines))
'''

'''
#restore comma back to missing value
file1 = open(os.path.join(os.getcwd(), "final_sorted.csv"),"r")
Lines = file1.readlines()

def findIndexOfOccurence(ini_str, sub_str, occurrence):
    #Finding nth occurrence of substring 
     val = -1
     for i in range(0, occurrence): 
         val = ini_str.find(sub_str, val + 1) 
     return val
             
first = Lines[0].count(",")
print(first)
for line in Lines:
    data = line.split(",")
    if line.count(",") < first:
        n = ""
        if(line.count("Negative") > 0):
            n = "Negative"
        elif(line.count("Neutral") > 0):
            n = "Neutral"
        elif(line.count("Positive") > 0):
            n = "Positive"
            
        before_phrase, temp_phrase, after_phrase = line.partition(n)
        line = before_phrase+","+temp_phrase + after_phrase
        print(n)
               
    with open(os.path.join(os.getcwd(), "all_sorted.csv"), 'a') as fd: 
        fd.write((line))
        fd.close()
'''

# verify datatype
#print(type(df.Date[0]))

#convert csv to excel file
import pandas as pd
df = pd.read_csv("extra.csv")
df.to_excel("extra.xlsx", sheet_name="Olamiposi", index=False)


'''
# re-Order columns in the data frame by name.
import pandas as pd
df = pd.DataFrame(pd.read_csv("sorted.csv"))
df = df.loc[:,[ "Headline","Primary", "Secondary" , "Date" ,  "Day",  "Month", "Year",
 "Sentiment","SentimentPolarity", "Emotion",  "Url" ]]

print(df.head) 

# saving the dataframe
df.to_csv(("reordered_sorted" + ".csv"), index=False)

'''
'''
# Merge 2 csv files together
file1 = os.path.join(os.getcwd(), "sorted2.csv")
Lines = open(file1,"r").readlines()

file2 = os.path.join(os.getcwd(), "sorted.csv")
Lines2 = open(file2,"r").readlines()
 
 # First Write a new line
with open(os.path.join(os.getcwd(), "sorted2.csv"), 'a') as fd: 
          fd.write("")
          fd.close()

# Then append other lines to the file
for line in Lines2 :
     with open(os.path.join(os.getcwd(), "sorted2.csv"), 'a') as fd: 
          fd.write(line)
          fd.close()
          
print("sorted: " + str(len(Lines2)) )
print("sorted2: " + str(len(Lines)) )
print("Merged:  " + str(len(Lines) + len(Lines2) ) )
'''
#12, 149 rows scraped, sorted and ordered.

'''
# re-Order some rows that are mis-ordered and 
#cut out any of 3 specific keywords from the back of the url 

def findIndexOfOccurence(ini_str, sub_str, occurrence):
    #Finding nth occurrence of substring 
     val = -1
     for i in range(0, occurrence): 
         val = ini_str.find(sub_str, val + 1) 
     return val
           
file1 = open(os.path.join(os.getcwd(), "all.csv"),"r")
Lines = file1.readlines()
first = Lines[0].count(",")
count = 0 
print(first)
for line in Lines:
    data = line.split(",")
    if  data[6] == "2021" or data[6]  == "2022" :
        with open(os.path.join(os.getcwd(), "all_cleaned.csv"), 'a') as fd: 
            fd.write((line + '\n'))
            fd.close()        
    else:
        count += 1
        print('\n' + '\n'+ "##############   Danger Danger Pants on Fire: "+str(count)+"  ################## " +'\n' +'\n')
        print("ISSUE: " +'\n' + line + '\n')
                
        n = ""
        url = data[9]
        print("BEFORE URL " +'\n' + url[-9:] + '\n')
        if(url[-9:].lower().split()== "Negative".lower().split()):
            n = "Negative"
            url = url[:-9] 
            print("URL " +'\n' + url + '\n')
        elif(url[-8:].lower().split()== "Neutral".lower().split()):
            n = "Neutral"
            url = url[:-8] 
            print("URL " +'\n' + url + '\n')
        elif(url[-9:].lower().split() == "Positive".lower().split()):
            n = "Positive"
            url = url[:-9] 
            print("URL " +'\n' + url + '\n')
            
        new_line = data[0] + "," + data[1] + "," + data[7] + "," + data[2] + "," + data[3] + "," + data[4]+ ","  + data[5] + "," + n+ ","  + data[8]+ ","  + data[6]+ "," + url
                
        print("IDEAL: " +'\n' + new_line + '\n')
                
        with open(os.path.join(os.getcwd(), "all_cleaned.csv"), 'a') as fd: 
            fd.write((new_line + '\n'))
            fd.close()
        
print(len(Lines))
'''


