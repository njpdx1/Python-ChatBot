import openai

#AI Class
class chat:
    #Constructor
    def __init__(self):
        with open('hidden.txt') as file:
            openai.api_key = file.read()

    #Welcome user to the program
    def welcome(self):
        print("Welcome to the AI chatbot program Marv will be assisting you today\n")

    #Read input from user
    def input(self):
        prompt = input("User: ")
        #Get repsonse from API
        reponse = self.get_response(prompt)
        #Display data to user
        print("AI: ", reponse)

    #Get response from API
    def get_response(self, prompt: str) -> str | None:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                    "role": "system",
                    "content": "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
                    },
                    {
                    "role": "user",
                    "content": prompt  
                    }
                ],
                temperature=0.5,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=[" User: ", " AI:"]
            )
            #Return AI repsonse
            return response['choices'][0]['message']['content']
        except Exception as error:
            print("Error: ", error)


def main():
    bot = chat()
    bot.welcome()
    while True:
        bot.input()

if __name__ == "__main__":
    main()
