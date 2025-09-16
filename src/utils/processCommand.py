from utils.bcolors import bcolors
from utils.runCommand import runInCLI

def process(commands):
    print(f"{bcolors.WARNING}\n⚠️  Run this commands at your own risk:{bcolors.ENDC} ")
    for c in commands:
        print()
        print(f"[{c["step"]}] {bcolors.BOLD}{c["brief"]}{bcolors.ENDC}")
        print(f"> {c["command"]}")
        runInCLI(c["command"])
