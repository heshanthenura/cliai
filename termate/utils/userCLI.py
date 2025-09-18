from .openRouterClient import get_response
from .processCommand import process
from .bcolors import bcolors
import os,sys

def start_cli():

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print(f"{bcolors.FAIL}❌ Error: OPENROUTER_API_KEY environment variable not set.{bcolors.ENDC}")
        print(f"{bcolors.WARNING}➡️  Please run: export OPENROUTER_API_KEY='your_api_key_here' (Linux/Mac){bcolors.ENDC}")
        print(f"{bcolors.WARNING}➡️  Or: setx OPENROUTER_API_KEY \"your_api_key_here\" (Windows PowerShell){bcolors.ENDC}")
        sys.exit(1)

    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Welcome to CLI-AI!{bcolors.ENDC} (type 'exit' or 'quit' to leave)\n")

    while True:
        query = input(f"{bcolors.OKGREEN}termate> {bcolors.ENDC}")

        if query.lower() in ["exit", "quit"]:
            print(f"{bcolors.OKBLUE}👋 Goodbye!{bcolors.ENDC}")
            break

        if query.strip() == "":
            continue

        print(f"{bcolors.WARNING}⏳ Generating response...{bcolors.ENDC}")
     
        try:
            response = get_response(query)
            process(response)
        except Exception as e:
            print(f"{bcolors.FAIL}❌ Error generating response: {e}{bcolors.ENDC}")

        print()  
