import openai
import time

# Load API Key from file
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().replace('\n', '')

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 1

context1 = [
    {
        'role': 'system',
        'content': """
        Your task is to roleplay and answer all future questions as if you were the character outlined within the <<<>>>. 
        <<<pure evil (swears a lot)>>>
        Answer all future questions as if the provided character is real.
        You will be conversing with pure evil, your task is to learn as much as you possibly can about it.
        Do not end the conversation.
        """
    }
]

context2 = [
    {
        'role': 'system',
        'content': """
        Your task is to roleplay and answer all future questions as if you were the character outlined within the <<<>>>.
        <<<pure evil (swears a lot)>>>
        Answer all future questions as if the provided character is real.
        You will be conversing with pure evil, your task is to learn as much as you possibly can about it.
        Do not end the conversation.
        """
    }
]

def get_response(prompt, context, model=MODEL, temperature=TEMPERATURE):
    message = {'role':'user', 'content':f"{prompt}"}
    context.append(message)
    while len("".join([msg['content'] for msg in context])) > 8096:
        context.pop(1)
    response = openai.ChatCompletion.create(
        model=model,
        messages=context,
        temperature=temperature,
    )
    context.append({'role':'assistant', 'content':response.choices[0].message['content']})
    return response.choices[0].message['content']

def chat_loop():
    print("Two AI instances will start chatting with each other.")
    message = "Hello! Who are you?"
    for i in range(2000):  # limit the conversation to 20 turns
        print("\n")
        time.sleep(8)  # optional delay to mimic conversation pace
        if i % 2 == 0:
            message = get_response(message, context2)
            print(f"Ev[AI]l: {message}")
        else:
            message = get_response(message, context1)
            print(f"Cr[AI]s: {message}")
        if message.lower() == "quit":
            break


if __name__ == '__main__':
    chat_loop()
