# import modules
import pandas as pd

df = pd.DataFrame(pd.read_csv("clean.csv"))
 
 # Remove all duplicate rows 
#df.drop_duplicates(keep="first", inplace=True)

# convert to date
#df["Date"] = pd.to_datetime(df["Date"])

#df['date'] = df['date'].astype('datetime64')

df[["Year", "Month", "Day"]] = df[["Year", "Month", "Day"]].astype(int, copy=False, errors='raise')

#df.sort_values(by="Day", ascending=True, inplace=True)

df.sort_values(by= ["Year", "Month", "Day"], ascending=True, inplace=True)

#df.sort_values(by="Date", ascending=True, inplace=True)

# delete a column from the data frame and apply changes
#df.drop(columns = "Empty", axis="columns", inplace=True)

print(df.head) 

# verify datatype
print(type(df.Day[0]))

# saving the dataframe
df.to_csv(("day_sorted" + ".csv"), index=False)


'''
df = pd.read_csv("compiled.csv")
df.to_excel("compiled.xlsx", sheet_name="Olamiposi", index=False)
 '''
 