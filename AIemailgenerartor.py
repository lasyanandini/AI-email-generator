from groq import Groq  

from dotenv import load_dotenv 

import os 

import requests 

 
load_dotenv() 

 
client = Groq(api_key = os.getenv("GROQ_API_KEY") ) 

def collect_input(): 

    try: 

        user_prompt = input("Enter email purpose: ") 

        if len(user_prompt) == 0: 

            user_prompt = input("Purpose cannot be blank. Please enter again: ").strip() 

 

            if len(user_prompt) == 0: 

                user_prompt = input("Purpose is required. Exiting application.") 

                return 

         

        user_recipient = input("Recipient Type: Manager / HR / project Lead etc. ? ") 

 

        if len(user_recipient) == 0: 

            user_recipient = input("Recipient cannot be blank. Please enter again: ") 

 

            if len(user_recipient) == 0: 

                    user_recipient = input("Recipient is required. Exiting application. ")  

                    return 

 

        user_tone = input( 

            "Tone: Professional / Personal / Friendly: ").strip() 

 

        if len(user_tone) == 0: 

            user_tone = input( 

                "Tone cannot be blank. Please enter again: " 

            ).strip() 

 

            if len(user_tone) == 0: 

                print("Tone is required. Exiting application.") 

                return 

 

        return build_prompt(user_prompt,user_recipient, user_tone) 

 

    except Exception as e: 

        print("Error occuured at collect_input(): ", e) 

 

def build_prompt(user_prompt,user_recipient, user_tone): 

    try:  

        prompt = f"""  

        You are a professional email writer 

 

        Write an email using the following details: 

 

        Purpose: {user_prompt} 

        Recipient: {user_recipient} 

        Tone: {user_tone} 

 

        The email should contain: 

        - A subject line 

        - A professional email body 

        - A proper closing 

        """ 

        return call_llm(prompt) 

 

    except Exception as e: 

        print("Exception occured at build_prompt", e) 

 

def call_llm(prompt): 

    try: 

        response = client.chat.completions.create( 

            model = "openai/gpt-oss-20b", 

            messages = [ 

                { 

                    "role" : "user", 

                    "content" : prompt 

                } 

            ] 

        ) 

        output = response.choices[0].message.content 

        return display_response(output) 


    except Exception as e: 

        print("Exception occured at call_llm :" , e) 

 
def display_response(output): 

    try: 

        print("Sucess response") 

        print(output) 

 

    except Exception as e: 

        print("exception occured at display_response", e) 

 

collect_input()