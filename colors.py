from turtle import color


class Colors:
    # ANSI escape codes for colors
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"
    
    class specfied:
        class interpreter:
            @staticmethod
            def error(text):
                print(f" │ {Colors.bright_red}error: {Colors.reset}{text}{Colors.reset}")
            @staticmethod
            def success(text):
                print(f" │ {Colors.bright_green}success: {Colors.reset}{text}{Colors.reset}")
            @staticmethod
            def warning(text):
                print(f" │ {Colors.bright_yellow}warning: {Colors.reset}{text}{Colors.reset}")

    class general:
        @staticmethod
        def error(text):
            print(f"{Colors.red}error: {text}{Colors.reset}")

        @staticmethod
        def big_error(text):
            print(f"{Colors.bright_red}ERROR: {text}{Colors.reset}")

        @staticmethod
        def warning(text):
            print(f"{Colors.yellow}WARNING: {text}{Colors.reset}")

        @staticmethod
        def info(text):
            print(f"{Colors.blue}INFO: {text}{Colors.reset}")

        @staticmethod
        def success(text):
            print(f"{Colors.green}SUCCESS: {text}{Colors.reset}")

        @staticmethod
        def debug(text):
            print(f"{Colors.magenta}DEBUG: {text}{Colors.reset}")

        @staticmethod
        def output(text):
            print(f"{Colors.cyan}OUTPUT: {text}{Colors.reset}")

        @staticmethod
        def result(text):
            print(f"{Colors.bright_green}RESULT: {text}{Colors.reset}")

if __name__ == "__main__":
    # Colors.se.s()
    # Colors.specfied.interpreter.error("hallo")
    # Colors.specfied.interpreter.success("hallo")
    # Colors.specfied.interpreter.warning("hallo")
    # Colors.se.e()
    print("COLROS LIB FOR FANGS-V1")