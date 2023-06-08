import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key=os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message["content"]

text = f"""
There was once a hare who was friends with a tortoise. One day, he challenged the tortoise to a race. \
Seeing how slow the tortoise was going, the hare thought he’ll win this easily. So he took a nap while the tortoise kept on going. \
When the hare woke up, he saw that the tortoise was already at the finish line. \
Much to his chagrin, the tortoise won the race while he was busy sleeping.
"""

prompt_1 = f"""
Perform the following actions: 
1 - Summarize the moral of the story of the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into German.
3 - List each character present in the story in the German Summary. 
4 - Output a json object that contains the following \
keys: german_summary, characters.
Separate your answers with line breaks.
Text:```{text}```
"""

response = get_completion(prompt_1)
print ("Completion for prompt 1:")
print (response)