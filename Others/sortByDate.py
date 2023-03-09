# import modules
import pandas as pd

df = pd.DataFrame(pd.read_csv("clean.csv"))
 
 # Remove all duplicate rows 
#df.drop_duplicates(keep="first", inplace=True)

# convert to date
#df["Date"] = pd.to_datetime(df["Date"])


df["Date"] = df.sort_values(by="Date", key=pd.to_datetime(df["Date"]), ascending=True)

#df.sort_values(by="Date", ascending=True, inplace=True)

# delete a column from the data frame and apply changes
#df.drop(columns = "Empty", axis="columns", inplace=True)

print(df.head) 

# verify datatype
print(type(df.Date[0]))

# saving the dataframe
df.to_csv(("date_sorted" + ".csv"), index=False)


'''
df = pd.read_csv("compiled.csv")
df.to_excel("compiled.xlsx", sheet_name="Olamiposi", index=False)
 '''
 