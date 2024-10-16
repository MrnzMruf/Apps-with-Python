import openai  

# Enter your OpenAI API key here  
openai.api_key = 'YOUR_API_KEY'  

def ask_gpt(question):  
    # Call the API to get a response from the GPT model  
    response = openai.ChatCompletion.create(  
        model='gpt-4',  
        messages=[  
            {'role': 'user', 'content': question}  
        ]  
    )  
    return response['choices'][0]['message']['content']  

# User input  
user_question = input("Ask the robot: ")  

# GPT response  
answer = ask_gpt(user_question)  
print("Robot's response:", answer)
