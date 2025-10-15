# import argparse
# from cli import command_handler
from chatbot import chat

def main():
    
    _chat=chat.AIEngine('AIzaSyCbgHunXmHu3i0tUSNaUPPzaqcqnyjMDns')
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = _chat.chat_with_ai(user_input)
        print(response)

if __name__ == '__main__':
    main()