import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

def preprocess_data(file_name):
    # Open the file and read the lines
    try:
        with open(diary.txt, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except IOError:
        print("Error: The file {} does not exist.".format(file_name))
        return None, None

    # Initialize empty lists to store the user and bot responses
    user_responses = []
    bot_responses = []

    # Iterate through the lines and extract the user and bot responses
    for line in lines:
        if line.startswith("[User]:"):
            user_response = line[7:].strip() # remove the label and any leading/trailing whitespace
            user_responses.append(user_response)
        elif line.startswith("[Bot]:"):
            bot_response = line[6:].strip() # remove the label and any leading/trailing whitespace
            bot_responses.append(bot_response)

    user_count = len(user_responses)
    bot_count = len(bot_responses)
    if user_count != bot_count:
        print(f"Error: The number of user responses is {user_count} and the number of bot responses is {bot_count}.")
        return None, None
    else:
        print(f"Both lists are of the same length with {user_count} elements each.")

    if not user_responses:
        print("Error: The user_responses list is empty.")
        return None, None
    elif not bot_responses:
        print("Error: The bot_responses list is empty.")
        return None, None

    # Preprocessing the data
    user_responses = [" ".join([word.lower() for word in word_tokenize(response)]) for response in user_responses]
    bot_responses = [" ".join([word.lower() for word in word_tokenize(response)]) for response in bot_responses]
    # Create a dataframe from the lists of user and bot responses
    df = pd.DataFrame({"user_response": user_responses, "bot_response": bot_responses})

    # Save the dataframe to a CSV file
    try:
        df.to_csv("chatbot_data.csv", index=False)
    except IOError:
        print("Error: The file chatbot_data.csv could not be created.")
    print("Data preprocessing and saving to CSV file completed successfully.")
   
    # Tokenize all the sentences
    word_tokens = [word_tokenize(sentence) for sentence in sentences]

    # Flatten the list of lists into a single list of words
    words = [word for sublist in word_tokens for word in sublist]

    # Create a set of unique words
    vocab = set(words)
    vocab_size = len(vocab)
    print(f"The vocabulary size is: {vocab_size}")
    return vocab, vocab_size

