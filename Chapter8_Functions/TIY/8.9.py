# Messages - Create a list of short messages called 'text_messages' and write a function called
    # 'show_messages', that will print each message.

def show_messages(text_messages):
    """
    Will show all text message history from newest to oldest
    """
    for messages in text_messages:
        print(messages)


text_messages = ['Hey, babe it did it again.', 
'Send this to Andrew!', 
'Okay  update... clicked the I am here button. Curbside was an option, but I still have to sit and wait while they make it...',]

show_messages(text_messages)