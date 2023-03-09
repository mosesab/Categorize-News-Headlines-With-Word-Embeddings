import os
import openai

# Fill in your own secret key
openai.api_key = "insert your open ai API key here"


# max_tokens: The token number decides how long the response is going to be. 
#NOTE: A token is not the number of words but it represents the largeness of the response text.
#temperature: Temperature determines the randomness of a response. A higher temperature will produce a more creative response, while a lower temperature will produce a more well-defined response.

def generate_article(topic):
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Write a paragraph about the following topic. ' + topic,
    max_tokens = 500,
    temperature = 0.3
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

# For GPT-3, the API rate limit is 20 requests per minute. it's fine as long as we don't run the function that fast.
paragraph_topics = [
"Drowsiness Detection Systems",
"ways Drowsiness Detection is done",
"opencv and Deep learning",
"Raspberry pi",
"Deep learning ensemble learning",
"Deep learning Face detection",
"comparison between face detect models, Haar, opencv's DNN face and Dlib's CNN",
"Deep learning CNN in Drowsiness Detection",
"7 layers in Deep learning CNN",
"Deep learning transfer learning",
"MobileNet, YOLO and Raspberry Pi"
]

for paragraph_topic in paragraph_topics:
    new = generate_article(paragraph_topic)
    output_file = os.path.join(os.getcwd(), "paragraphs.csv")
    # create output_file if it does not exist, or append to it if it does exist
    with open(output_file, 'a') as fd:
        fd.write(new)
        fd.close()
    
    print(new)
  
    
#print(generate_article('Why NYC is better than your city.'))
