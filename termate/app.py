import platform
import sys
from termate.utils.userCLI import start_cli

def main():
    if platform.system() != "Linux":
        print("⚠️ TerMate only works on Linux!", file=sys.stderr, flush=True)
        sys.exit(1)
    start_cli()

if __name__ == "__main__":
    main()
