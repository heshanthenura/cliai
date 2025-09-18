import subprocess
from .bcolors import bcolors

def runInCLI(command):
    user_input = input(
        f"{bcolors.OKCYAN}Press Enter to run, or 's' to skip: {bcolors.ENDC}"
    )

    if user_input.lower() == "s":
        print(f"{bcolors.WARNING}Skipped command.{bcolors.ENDC}\n")
        return False

    print(f"{bcolors.OKGREEN}Running command...{bcolors.ENDC}\n")

    try:
       
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1 
        )

       
        for line in process.stdout:
            print(line, end="", flush=True)  

        process.wait() 

    except Exception as e:
        print(f"{bcolors.FAIL}Error running command: {e}{bcolors.ENDC}")

    print(f"\n{bcolors.OKBLUE}Command finished.{bcolors.ENDC}\n")
    return True
