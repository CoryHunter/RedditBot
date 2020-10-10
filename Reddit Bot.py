# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:20:58 2019
Reddit Bot
@author: coryr
"""

import praw
import random as rand
from time import time as time
from time import sleep




"""
clientID: Given By Reddit, TYPE: STR
clientSecret: Given By Reddit, TYPE: STR
USERNAME: username for bot account, TYPE: STR
PASSWORD: password for bot account, TYPE: STR
mainUsername: Username of Personal Account, TYPE: STR
subReddit: Subreddit to post on, TYPE: STR
triggerPhrases1:  List of phrases to search for, TYPE: LIST(STR)
triggerPhrases2: List of phrases to search for, TYPE: LIST(STR)
responses1:  List of Repsonses if a phrase in triggerPhrases1 occurs in the post, TYPE: LIST(STR)
responses2:  List of Repsonses if a phrase in triggerPhrases2 occurs in the post, TYPE: LIST(STR)
"""



def run_bot(clientID, clientSecret, USERNAME, PASSWORD, mainUsername, subReddit,
            triggerPhrases1, triggerPhrases2, responses1, responses2):                   

    try:
        reddit = praw.Reddit(client_id = clientID,
                             client_secret = clientSecret,
                             username = USERNAME,
                             password = PASSWORD,
                             user_agent = "repostbot by /u/" + mainUsername)
    except:
        raise ValueError("Log In failed, check input values")
    try:
        subreddit = reddit.subreddit(subReddit)
        
    except:
        raise ValueError("Invalid Subreddit, please try again")
        
    start_time = time()
    for submission in subreddit.stream.submissions():
        if submission.created_utc < start_time:
            continue
        try:
            normalized_title = submission.title.lower()
            for trigger1 in triggerPhrases1:
                if trigger1 in normalized_title:
                    index = rand.randint(0,len(responses1)-1)
                    submission.reply(responses1[index])
                    print("posted: " , responses1[index])
                    sleep(605)
            for trigger2 in triggerPhrases2:
                if trigger2 in normalized_title:
                    index = rand.randint(0,len(responses2)-1)
                    submission.reply(responses2[index])
                    print("posted: " , responses2[index])
                    sleep(605)
            continue
        except:
            continue
    
    


        