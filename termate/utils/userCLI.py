from termate.utils.openRouterClient import get_response
from termate.utils.processCommand import process
from termate.utils.bcolors import bcolors
import os, sys

def start_cli():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print(f"{bcolors.FAIL}❌ Error: OPENROUTER_API_KEY environment variable not set.{bcolors.ENDC}", flush=True)
        print(f"{bcolors.WARNING}➡️  Please run: export OPENROUTER_API_KEY='your_api_key_here' (Linux/Mac){bcolors.ENDC}", flush=True)
        sys.exit(1)

    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Welcome to CLI-AI!{bcolors.ENDC} (type 'exit' or 'quit' to leave)\n", flush=True)

    while True:
        query = input(f"{bcolors.OKGREEN}termate> {bcolors.ENDC}")

        if query.lower() in ["exit", "quit"]:
            print(f"{bcolors.OKBLUE}👋 Goodbye!{bcolors.ENDC}", flush=True)
            break

        if query.strip() == "":
            continue

        print(f"{bcolors.WARNING}⏳ Generating response...{bcolors.ENDC}", flush=True)
     
        try:
            response = get_response(query)
            process(response)
        except Exception as e:
            print(f"{bcolors.FAIL}❌ Error generating response: {e}{bcolors.ENDC}", flush=True)

        print()
