from colorama import Fore, Style, init
import json
import os

init(convert=True)
class Logger:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.abspath(os.path.join(base_dir, "../../config.json"))

        with open(config_path, "r") as f:
            data = json.load(f)
        self.DebugMode = data.get("DebugMode", False)

    def DEBUG(self, text):
        if self.DebugMode:
            print(Fore.YELLOW+"[DEBUG] " + text + Style.RESET_ALL)
        else:pass
    def SERVER(self, text):
        if self.DebugMode:
            print(Fore.GREEN+"[SERVER] " + text + Style.RESET_ALL)
        else:pass
    def ERROR(self, text):
        if self.DebugMode:
            print(Fore.RED+"[ERROR] " + text + Style.RESET_ALL)
        else:pass
    def TODO(self, text):
        if self.DebugMode:
            print(Fore.CYAN+"[TODO] " + text + Style.RESET_ALL)
        else:pass
    def CLIENT(self, text):
        if self.DebugMode:
            print(Fore.MAGENTA+"[CLIENT] " + text + Style.RESET_ALL)
        else:pass

