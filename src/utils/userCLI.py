from utils.openRouterClient import get_response
from utils.processCommand import process
from utils.bcolors import bcolors

def start_cli():
    print(f"{bcolors.OKCYAN}{bcolors.BOLD}Welcome to CLI-AI!{bcolors.ENDC} (type 'exit' or 'quit' to leave)\n")

    while True:
        query = input(f"{bcolors.OKGREEN}cli-ai> {bcolors.ENDC}")

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
