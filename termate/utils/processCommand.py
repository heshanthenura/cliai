from termate.utils.bcolors import bcolors
from termate.utils.runCommand import runInCLI

def process(commands):
    print(f"{bcolors.WARNING}\n⚠️  Run these commands at your own risk:{bcolors.ENDC}", flush=True)
    
    for c in commands:
        print(flush=True)
        print(f"[{c['step']}] {bcolors.BOLD}{c['brief']}{bcolors.ENDC}", flush=True)
        print(f"> {c['command']}", flush=True)
        runInCLI(c['command'])
