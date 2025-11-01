from .colors import Colors
from datetime import datetime
import pytz
import traceback

class PypeLogger:
    @staticmethod
    def info(message):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        print(f"{Colors.GRAY}[{now}] {Colors.GREEN}[INFO] {message}{Colors.RESET}")

    @staticmethod
    def error(message, exception=None):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        main_error = f"{Colors.GRAY}[{now}] {Colors.RED}[ERROR] {message}{Colors.RESET}"
        error_messages = [main_error]
        if exception:
            exception_message = f"\n{Colors.GRAY}[{now}] {Colors.RED}[ERROR]      - Exception: {exception}"
            traceback_message = f"\n{Colors.GRAY}[{now}] {Colors.RED}[ERROR]      - Traceback: {traceback.format_exc()}"
            error_messages.append(exception_message)
            error_messages.append(traceback_message)
        for error_message in error_messages:
            print(error_message)

    @staticmethod
    def debug(message):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        print(f"{Colors.GRAY}[{now}] {Colors.BLUE}[DEBUG] {message}{Colors.RESET}")
    
    @staticmethod
    def warning(message):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        print(f"{Colors.GRAY}[{now}] {Colors.YELLOW}[WARNING] {message}{Colors.RESET}")
    
    @staticmethod
    def success(message):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        print(f"{Colors.GRAY}[{now}] {Colors.LIME}[SUCCESS] {message}{Colors.RESET}")

    @staticmethod
    def command(message):
        now = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M:%S")
        print(f"{Colors.GRAY}[{now}] {Colors.MAGENTA}[COMMAND] {message}{Colors.RESET}")