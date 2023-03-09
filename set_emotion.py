# importing pandas as pd



import pandas as pd
from nrclex import NRCLex

# Creating the sentiment
def e_emote(text):
    # Create object
    emotion = NRCLex(text).raw_emotion_scores
    if(len(emotion) > 0):
        highest = analysis(emotion)
        return str(highest)
    return "0"

# function to analyze the reviews
def analysis(score):
    # taking list of car values in v
    v = list(score.values())
    
    # taking list of car keys in v
    k = list(score.keys())
    
    # get largest score in dictionary
    score = k[v.index(max(v))]
    
    if(score == "positive"):
        score = "anticipation"
    elif(score == "negative"):
        score = "sadness"
    return str(score)
    
    
    
if __name__ == "__main__":        
    df = pd.DataFrame(pd.read_csv("headLines.csv"))
     
    # creating a data frame
    #df = pd.DataFrame([csv_reader], index = None)
    
    #df.drop(columns = "no", axis="columns", inplace=True)
    
    df["Emotion"] = df.apply(lambda row: e_emote(row.Headline), axis="columns")
    
    print(df.head)
       
    # Print the dataframe
    print(df.head())      
    
    # saving the dataframe
    df.to_csv('file3.csv', index=False)
    
    