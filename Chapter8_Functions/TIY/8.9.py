# Messages - Create a list of short messages called 'text_messages' and write a function called
    # 'show_messages', that will print each message.

def archiving_messages(text_messages, message_history):
    """
    This will take all messages that have been sent and archive them in the history folder.
    """
    while text_messages:
        old_messages = text_messages.pop()
        message_history.append(old_messages)

def show_messages(message_history):
    """
    Will show all text message history from newest to oldest
    """
    for messages in message_history:
        print(messages)




text_messages = ['Hey, babe it did it again.', 
'Send this to Andrew!', 
'Okay  update... clicked the I am here button. Curbside was an option, but I still have to sit and wait while they make it...',]
message_history = []

archiving_messages(text_messages, message_history)
show_messages(message_history)