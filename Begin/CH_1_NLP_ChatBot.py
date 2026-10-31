#### sentiment-based responses for a chatbot using TextBlob

from textblob import TextBlob

# Define intents and their corresponding responses based on keywords
intents = {
    "hours":{
        "keywords":["hours", "open", "close"],
        "response": "We are open from 9AM to 5PM, M/F"
    },
    "return":{
       "keywords": ["refound", "money back", "return"],
       "response": "happy to help, let me transfer to a live agent"
    },
    "grades":{
       "keywords": ["grades", "grade", "gpa", "transcript", "marks", "score", "result"],
       "response": "happy to help, let me transfer to your division coordinator \nTell me your student ID and I will check your grades for you"
    },
    "greeting":{
       "keywords": ["hi", "hello", "hey", "greetings"],
       "response": "Hello! How can I assist you today?"
    },
    "identificationJ":{
         "keywords": ["1", "2", "3", "4", "5" ],
         "response": "I'll transfer you to The Junior School Principal, please wait..."
    },
    "identificationS":{
         "keywords": ["6", "7", "8", "9"],
         "response": "I'll transfer you to The Middle School Principal, please wait..."
    },
    "identificationH":{
         "keywords": ["10", "11", "12"],
         "response": "I'll transfer you to The Senior School Principal, please wait..."
    }

}
def get_response(message):
    # Convert the message to lowercase for consistent keyword matching
    message = message.lower()
  
    # Check if the message contains any keywords associated with defined intents
    #if any(word in message for word in intent_data["keywords"]):
    # Return the corresponding message if a keyword matches
    #    return intent_data["response"]   

    #corrected
    for intent_data in intents.values():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]
    
    #for intent_data in intents.values():
    #    if any(keyword in message.split() for keyword in intent_data["keywords"]):
    #        return intent_data["response"]
        
    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity

    # Return a response based on the sentiment score
    return ("That's so great to hear" if sentiment > 0 else
        "I'm so sorry to hear that, how can I help?" if sentiment < 0 else
        "I see, can you tell me more about that?")

def chat():
       
    # Greet the user and prompt for input
    print("Chatbot: Hi, how can I help you today?")
   
    # Continuously prompt the user for input until they choose to exit
    while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")
   
    # Thank the user for chatting when they exit
    print("Chatbot: Thank for chating, have a great day")


if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
