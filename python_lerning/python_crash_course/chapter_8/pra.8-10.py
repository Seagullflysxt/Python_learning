#pra.8-10
def send_messages(unsent_msgs,sent_msgs):
    while unsent_msgs:
        current_msg = unsent_msgs.pop()
        print(f"Current message:{current_msg}")
        sent_msgs.append(current_msg)
    
def show_message(msgs1,msgs2):
    print("Unsent_messages:")
    for msg1 in msgs1:
        print(msg1)
    print("\nSent_messages:")
    for msg2 in msgs2:
        print(msg2)

unsent_messages = ['Hello','Hi','How are you?']
sent_messages = []

send_messages(unsent_messages[:],sent_messages)
print("\n")
show_message(unsent_messages,sent_messages)
