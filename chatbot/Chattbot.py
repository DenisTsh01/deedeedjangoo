# description: This is a `smart` chat bot program
# import  the libraries

import json
import nltk

# from teach_learn import append_dict, get_information, append_main_dict
from chatbot.weather_manager import func

nltk.download('punkt')
from newspaper import Article
import random
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import warnings

warnings.filterwarnings('ignore')

# get the article
article = Article('https://en.wikipedia.org/wiki/Blockchain')
article.download()
article.parse()
article.nlp()
corpus = article.text

# print the article text
# print(corpus)

# tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)  # a list of sentences


# print the list of sentences
# print(sentence_list)


# a FUNTION TO return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()

    # bots greeting response
    bot_greeting = ['howdy', 'hi', 'hey', 'hello', 'hola']
    # users greeting
    user_greeting = ['hi', 'hey', 'hello', 'hola', 'greetings', 'wassup']
    # weather

    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# create the bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            reponse_flag = 1
            j = j + 1
        elif j > 2:
            break
        elif response_flag == 0:
            bot_response = bot_response + ' ' + "I apologize, I don't understand."
        sentence_list.remove(user_input)

        return bot_response


# def get_response_from_bot(user_input):
#     if user_input.lower() in exit_list:
#         print('DeeDee: Chat with you later !')
#
#     if user_input.lower() in user_weather:
#         print("DeeDee: Tell me a city")
#         user_city = input().lower()
#         print(func(user_city))
#
#     elif user_input.lower() == 'information':
#         while(True):
#             print(
#                 "DeeDee: Type command teach to teach me or learn to tell you information about something...if i know the subject")
#             user_input = input().lower()
#             contor = 0
#             if user_input.lower() == user_teach_learn[0]:
#
#                 while (True):
#                     if contor != 0:
#                         print("DeeDee: Would you like to tell me more stuff ? If not, type commands exit or exit teach")
#                         user_input = input().lower()
#                         print(user_input)
#                     if contor == 0:
#                         print("DeeDee: Tell me the subject, then tell me the information")
#                         contor+=1
#
#                     if user_input == "exit teach" or user_input == "exit":
#                             append_main_dict()
#
#                             print("DeeDee: Exiting information...")
#                             break
#
#                     elif user_input == "yes" or user_input == "y":
#                         print("DeeDee: Then tell me!")
#
#                     subject = input().lower()
#                     information = input().lower()
#                     append_dict(subject, information)
#
#
#
#             if user_input.lower() == user_teach_learn[1]:
#               #  while (True): de implementat
#               # de implemenetat alegere subiecte + afisarea fiecaruia
#                 information_deedee_response = get_information()
#                 print(f'DeeDee: All I know is: {information_deedee_response}')
#
#             if user_input == "exit information" or user_input == "exit":
#
#                 break
#
#     else:
#         if greeting_response(user_input) != None:
#             print("DeeDee: " + greeting_response(user_input))
#         else:
#             print("DeeDee: " + bot_response(user_input))


def get_response_from_bot(user_input):
    exit_list = ['exit', "see you later", "bye", "quit", "break"]
    user_weather = ['weather']
    first_word = user_input.split(' ')[0]
    if user_input.lower() in exit_list:
        return 'Chat with you later !'

    if first_word.lower() in user_weather:
        second_word = user_input.split(' ')[1]
        return func(second_word)

    # elif user_input.lower() == 'information':
    #     while (True):
    #         print(
    #             "DeeDee: Type command teach to teach me or learn to tell you information about something...if i know the subject")
    #         user_input = input().lower()
    #         contor = 0
    #         if user_input.lower() == user_teach_learn[0]:
    #
    #             while (True):
    #                 if contor != 0:
    #                     print("DeeDee: Would you like to tell me more stuff ? If not, type commands exit or exit teach")
    #                     user_input = input().lower()
    #                     print(user_input)
    #                 if contor == 0:
    #                     print("DeeDee: Tell me the subject, then tell me the information")
    #                     contor += 1
    #
    #                 if user_input == "exit teach" or user_input == "exit":
    #                     append_main_dict()
    #
    #                     print("DeeDee: Exiting information...")
    #                     break
    #
    #                 elif user_input == "yes" or user_input == "y":
    #                     print("DeeDee: Then tell me!")
    #
    #                 subject = input().lower()
    #                 information = input().lower()
    #                 append_dict(subject, information)
    #
    #         if user_input.lower() == user_teach_learn[1]:
    #             #  while (True): de implementat
    #             # de implemenetat alegere subiecte + afisarea fiecaruia
    #             information_deedee_response = get_information()
    #             print(f'DeeDee: All I know is: {information_deedee_response}')
    #
    #         if user_input == "exit information" or user_input == "exit":
    #             break

    else:
        if greeting_response(user_input) != None:
            return greeting_response(user_input)
        else:
            return bot_response(user_input)

if __name__ == '__main__':

    # start the chat
    print(
        'DeeDee: I am DeeDee, sort of AI .I do not know many things but i can tell '
        'you different informations.If you want to know about the weather type command '
        'weather or ask me about cypto. If you want to exit, type bye.')

    exit_list = ['exit', "see you later", "bye", "quit", "break"]
    user_weather = ['weather']
    # teacb and learn
    user_teach_learn = ['teach', 'learn']

    while (True):
        user_input = input()
        get_response_from_bot(user_input)
