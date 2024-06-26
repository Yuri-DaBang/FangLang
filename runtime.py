import json
import os

class se:
    def __init__(self, filename,runtimename):
        self.ssid = runtimename
        self.filename = filename
        self.errors = []
        self.warnings = []
        self.success = []
        self.data = {
            filename: {
                "errors": self.errors,
                "warnings": self.warnings,
                "success": self.success
            }
        }
        self.create_json_file()
        
    def return_filename(self):
        return str(self.filename)

    def create_json_file(self):
        with open(f"{self.ssid}.json", 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_json_file(self):
        with open(f"{self.ssid}.json", 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_e(self, e):
        self.errors.append(e)
        self.update_json_file()

    def add_w(self, w):
        self.warnings.append(w)
        self.update_json_file()

    def add_s(self, s):
        self.success.append(s)
        self.update_json_file()

    def get_data(self):
        with open(f"{self.ssid}.json", 'r') as file:
            return json.load(file)

    def delete_json_file(self):
        if os.path.exists(f"{self.ssid}.json"):
            os.remove(f"{self.ssid}.json")

    def s(self):
        print(f"[H] OUTPUT ({self.filename})")

    def m(self, text):
        print(f" │ {Colors.white}{text}{Colors.reset}")

# Example usage:
class Colors:
    white = '\033[97m'
    reset = '\033[0m'

# output = se("example_file")
# output.add_e("system error: abc is not defined")
# output.add_w("you are using debugging mode, switch to normal please")
# output.add_w("you are using example_file")
# output.add_s("file (example_file) executed successfully")
# print(output.get_data())
# output.delete_json_file()
