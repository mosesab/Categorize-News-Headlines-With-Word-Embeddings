import os
# importing pandas as pd
import pandas as pd

from gensim.models import KeyedVectors
from gensim.parsing.preprocessing import remove_stopwords
from text_cleaner import clean_text

import gensim.downloader as api


categories = [
"Administrative",
"Aviation", 
"Agriculture", 
"Border Control", 
"Crime", 
"Defense", 
"Education", 
"Entertainment", 
"Environment", 
"Finance", 
"Foreign Affairs", 
"Health", 
"Information and Culture", 
"Justice", 
"Legal", 
"Legislative",
"Labor and Productivity",
"Petroleum Resources",
"Power", 
"Politics",
"Sports",
"Transportation",
"Youth Development"]


filepath = os.path.join(os.getcwd(), "word2vectors.vec")

# if the local word-vectors model exists
if(os.path.exists(filepath)): 
    print('\n' + '\n'+ "##############   LOADING THE  WORD-VECTOR MODEL FROM LOCAL STORAGE   ################## " +'\n' +'\n')

    # Load pre-trained Word2Vec model.
    model = KeyedVectors.load(filepath)
else:
    print('\n' + '\n'+ "##############   DOWNLOADING  A LARGE WORD-VECTOR MODEL FROM THE 'gensim' LIBRARY. ################## " +'\n' +'\n')

    # show info about available models/datasets
    print(api.info(name_only=True))
    # download the pre-trained word-vectors model from gensim-data and return as object ready for use
    model = api.load("glove-wiki-gigaword-100")  
    # word-vectors model type 
    print(type(model))


print('\n' + '\n'+ "##############   LOADING WORD-VECTOR MODEL COMPLETE - SYSTEM CAN NOW CATEGORIZE TEXT BY CALCULATING SIMILARITES BETWEEN WORDS.    ################## " +'\n' +'\n')
       
def get_score(my_list):
    scores = []
    s_largest_index = -1 # it's -1 because if high_score is index 0, it'll stay on high_score index.
    # calculate the highest and second highest scores
    for n in range(len(my_list)):
        scores.append(my_list[n][1])
        
    # calculate the highest 
    high_score = max(scores)
    largest_index = scores.index(high_score)
    
    #replace highest element with 0
    scores[largest_index] = 0
    
    # calculate the second highest 
    s_high_score = max(scores)
    s_largest_index = scores.index(s_high_score)

    #print('\n' + '\n'+ "Most Similar: "+str(categories[largest_index])+ '\n' +'\n')
    #print('\n' + '\n'+ "Second Most Similar: "+str(categories[s_largest_index])+ '\n' +'\n')
                
    #print('\n' + '\n'+ "high_score: "+str(high_score)+ '\n' +'\n')
    #print('\n' + '\n'+ "s_high_score: "+str(s_high_score)+ '\n' +'\n')

    return str(categories[largest_index]), str(categories[s_largest_index])

                                                                  
def c_emote(text):
    my_list = []
    phrase = clean_text(remove_stopwords(text)).split()
    #print('\n' + '\n'+ "phrase: "+str(phrase)+ '\n' +'\n')

    # get local word vector
    for i in range(len(categories)):
        total = 0
        category = clean_text(categories[i])
        
        # Petroleum Resources" and "Border Control" change semantic meaning, if split
        if category ==  clean_text("Youth Development" ): # Youth Development not in Word2Vec
            category = clean_text("Child" ).split()
        elif category != (clean_text("Border Control") or clean_text("Petroleum Resources")):
            category = category.split()
        else:
            category = category.split("$")
            
        for k in phrase:
            try:
                for c in range(len(category)):
                    total += model.similarity( k, category[c])
            except Exception as e:
                #print('\n' + '\n'+ "##############   ERROR  OCCURED,  SKIPPED: "+"  ################## " +'\n' +'\n')
                #print(e)
                pass
        current_score = (total / len(category))
        #print('\n' + '\n'+ "Category: "+str(category) + "CurrentScore: " +str(current_score) +'\n' +'\n')
        my_list.append([str(category) , current_score])
    return get_score(my_list)
    



if __name__ == "__main__":
    df = pd.DataFrame(pd.read_csv("compiled.csv"))
     
    # delete a column from the data frame and apply changes
    #df.drop(columns = "Empty", axis="columns", inplace=True)
    
    #df["Emotion"] = df.apply(lambda row: emote(row.Headline), axis="columns")
    
    #df["Primary"] , df["Secondary"] = emote(df["Headline"])
    #df["Primary"] , df["Secondary"] = zip(*df["a"].apply(emote))
    
    
    df["Primary"], df["Secondary"] = zip(*df["Headline"].apply(c_emote))
    
    print(df.head)
    
    # saving the dataframe
    df.to_csv('file3.csv', index=False)
