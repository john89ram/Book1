# Archived messages - Use your work from 8.10 and call the function send_messages but
    # with a copy of the list. Print the list to insure that the list was not modified.

def send_messages(text_messages, sent_messages):
    """
    This will take all messages that have been sent and archive them in the history folder.
    """
    while text_messages:
        old_messages = text_messages.pop()
        sent_messages.append(old_messages)

def show_messages(sent_messages):
    """
    Will show all text message history from newest to oldest
    """
    for messages in sent_messages:
        print(messages)


text_messages = ['Hey, babe it did it again.', 
'Send this to Andrew!', 
'Okay  update... clicked the I am here button. Curbside was an option, but I still have to sit and wait while they make it...',]
sent_messages = []

print(f"\n{text_messages}")
print(f"{sent_messages}\n")

send_messages(text_messages[:], sent_messages)

print(f"\n{text_messages}")
print(f"{sent_messages}\n")
