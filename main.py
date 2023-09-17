import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

# Get reposnse from API


def get_response(prompt: str) -> str | None:
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
        print(response)

    except Exception as error:
        print("Error: ", error)


def main():
    prompt = input("User: ")
    get_response(prompt)


if __name__ == "__main__":
    main()
