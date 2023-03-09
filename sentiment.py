# import modules
import pandas as pd
from textblob import TextBlob
 
# function to return the sentiment as text
def s_emote(text):
    score = TextBlob(text).sentiment.polarity
    n = ""
    if(score < 0):
        n = "Negative"
    elif(score == 0 or (score > 0 and score < 0.1 )):
        n = "Neutral"
    else:
        n = "Positive"
    return str(n)
            
# function to return the sentiment polarity
def scored(text):    
        score = TextBlob(text).sentiment.polarity
        return str.format('{0:.1f}', score)
 
if __name__ == "__main__":
    df = pd.DataFrame(pd.read_csv("compiled.csv")) 
    
    # Remove all duplicate rows 
    df.drop_duplicates(keep="first", inplace=True)
    
    # delete a column from the data frame and apply changes
    #df.drop(columns = "Empty", axis="columns", inplace=True)
    
    df["Sentiment"] = df.apply(lambda row: s_emote(row.Headline), axis="columns")
    
    df["SentimentPolarity"] = df.apply(lambda row: scored(row.Headline), axis="columns")
    
    print(df.head) 
    
    # saving the dataframe
    df.to_csv('file3.csv', index=False)
    