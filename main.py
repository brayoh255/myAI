import openai

openai.api_key  = "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"

def chat_with_gpt(prompt);
 
 response = openai.ChatCompletion.create(
     model = "gpt -3.5-turbo",
     messages = [{"role": "user": "prompt"}]
 )
 
 return response.choices[0].message.content.strip()

if __name__ == "__main__":
    
    while True:
        user_input =  input("You:")
        if user_input.lower() in ["quit","exit","bye", "Asante", ]
        break
    
    response = chat_with_mrtuagize (user_input)
    
    print("Chatbot:" , response)