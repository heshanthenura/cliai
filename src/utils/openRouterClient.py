from openai import OpenAI
import json,os,sys
from utils.bcolors import bcolors

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print(f"{bcolors.FAIL}❌ Error: OPENROUTER_API_KEY environment variable not set.{bcolors.ENDC}")
    sys.exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


system_prompt = """
You are a Linux CLI assistant.

Whenever you provide commands, reply ONLY in **pure JSON format** like this:

[
  {
    "step": "1",
    "brief": "Explain what this step does in brief",
    "command": "The exact Linux command"
  },
  {
    "step": "2",
    "brief": "Explain what this step does in brief",
    "command": "Another Linux command"
  }
]

Important rules:
1. Do NOT include any extra text outside this JSON.
2. Do NOT use backticks, markdown, or code blocks.
3. Only provide one best response unless the user explicitly asks for multiple variations.
4. Ensure the JSON is always valid and parsable.
5. Each response must be **ready to be parsed by Python's json.loads()** without modification.
"""



def get_response(user_prompt):
    response = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3.1:free",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    stream=True 
    )
    
    collected_text = ""

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            collected_text += chunk.choices[0].delta.content

    try:
        steps = json.loads(collected_text)
        return steps
    except json.JSONDecodeError as e:
        print("JSON parsing error:", e)
        print("Raw text from AI:", collected_text)
