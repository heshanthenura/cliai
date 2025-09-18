import platform
import sys
from .utils.userCLI import start_cli

if platform.system() != "Linux":
    print("⚠️ TerMate only works on Linux!")
    sys.exit(1)

if __name__ == "__main__":
    start_cli()
