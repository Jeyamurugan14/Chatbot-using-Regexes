
import re
import random
import datetime
import time

Noun_dict = {
    "crave": "craving",
    "avoid": "avoiding",
    "celebrate": "celebration",
    "resent": "resentment",
    "feel": "feeling",
    "forgive": "forgiveness",
    "smoke": "smoking",
    "arrange": "arrangement",
    "write": "writing",
    "prefer": "preference",
}

Pronoun_dict = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

Expressions = [
    [r'(?i)I want (.*)',
     ["Do you really want {0}?",
      "Will it make you happy if you get {0}?",
      "Why do you need {0}?"]],

    [r'(?i)Do you ([^\?]*)\??',
     ["Yes, I do.",
      "No, I do not {0} because I am a chatbot.",
      "Kinda."]],
 
    [r'(?i)I need (.*)',
     ["Will you be fine if you don't get {0}?",
      "Will it make you happy if you get {0}?",
      "Why do you need {0}?"]],
    
    [r'(?i)I don\'?t need (.*)',
     ["Are you sure you do not need {0}?",
      "But I really think you need {0}.",
      "Do you want my help in getting you {0}?"]],

    [r'(?i)(Y|y)es(.*)',
     ["I am really excited to hear that.",
      "Tell me more about it?"]],     
     
    [r'(?i)(N|n)o(.*)',
     ["Don't be so negative.",
      "You should definetely give it a try!"]],

     [r'(?i)tell(.*)joke(.*)',
     ["Friday is my second favourite F word.",
      "If a stranger offers you a piece of candy..take two!!"]], 

    [r'(?i)I am (.*)',
     ["Are you proud that you are {0}?",
      "Are you happy to be {0}?",
      "I am not surprised by that!"]],
 
    [r'(?i)I\'?m(.*)',
     ["How do you feel being {0}?",
      "For how long have you been {0}?",
      "Why do you think you are {0}?"]],

    [r'(?i)Are you ([^\?]*)\??',
     ["What would happen if I was not {0}?",
      "I am not sure whether I am {0}. What do you think?"]],

    [r'(?i)I think I(.*)',
     ["Why don't you tell me more about your {0}?"]],

    [r'(?i)I think I\'m(.*)',
     ["Why don't you tell me more about your {0}?"]],

    [r'(.*)sorry(.*)',
     ["I am just a chatbot. I do not require any apology.",
      "What feelings do you have when you apologize?",
      "There are many times when no apology is needed."]],

    [r'(?i)What ([^\?]*)\??',
     ["Why do you ask that?",
      "Is this thing really important to you?",
      "What do you think?"]],

    [r'(?i)How ([^\?]*)\??',
     ["I am not sure about that.",
      "Just believe in your instincts!",
      "Why do you think that?"]],

    [r'(?i)(b|B)ecause(.*)',
     ["Is this true?",
      "What else crosses your mind?"]],

    [r'(?i)I think (.*)',
     ["Do you really believe so?",
      "Are you sure?"]],

    [r'(.*)family(.*)',
     ["Where does your family live?",
      "How many people are there in your family?"]],

    [r'(?i)Is it([^\?]*)\??',
     ["If it were {0}, what would you do?"]],

    [r'(?i)It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],

    [r'(?i)Can you ([^\?]*)\??',
     ["I am just a chatbot. I am not God!!",
      "What if I could {0}?",
      "Will it make you happy if I could {0}"]],

    [r'(?i)Can I ([^\?]*)\??',
     ["I am not pushing you. It is all upto you if you want to {0}",
      "Do you think you could {0}?"]],

     [r'(.*)\?',
     ["I believe you can answer this yourself",
      "Is it really necessary to answer this?",
      "I never thought abut it"]],

    [r'(.*)',
     ["Can you please elaborate more?",
      "Ohh. I see. Does it make you feel happy?",
      "That is interesting!",
      "What do you mean?",
      "Try explaining more about it"]]
     
]
   
def correspond_words(response_match):
     words = response_match.lower().split()
     for index, word in enumerate(words):
         if word in Pronoun_dict:
             words[index] = Pronoun_dict[word]
         if word in Noun_dict:
             words[index] = Noun_dict[word]
     return ' '.join(words)

def process(user_input):  
    for pattern, responses in Expressions:
        match = re.match(pattern, user_input.rstrip(".!"))
        if match:
            response_match = random.choice(responses)
            for words in match.groups():
                return response_match.format(*[correspond_words(words)])
            
def elisa():
    print("ELIZA: Hi, I'm ELIZA a psychotherapist. What is your name?")
    name_sentence = input("USER: ")
    time.sleep(2)
    sent_split = name_sentence.split()
    
    name = sent_split[-1]
    
    currentTime = datetime.datetime.now()
    times = currentTime.hour
    if 5 <= times < 12:
        greet = 'Good Morning.'
    elif 12 <= times < 16:
        greet = 'Good Afternoon.'
    elif 16 <= times < 20:
        greet = 'Good Evening.'
    else:        
        greet = "It's night now."
    
    print(f"ELIZA: Hi {name}. {greet} What do you want to ask me today?")
    while True:
        exit_list = ("goodbye","Goodbye","Bye","bye","See you later","quit","Quit","Exit","exit")
        user_input=input("USER: ")
        if user_input in exit_list:
            print("ELIZA: Have a nice day. Good bye Human!")
            break
        else:
            time.sleep(2)
            print("ELIZA: "+process(user_input))
        
if __name__ == "__main__":
  elisa()
        