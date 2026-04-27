import os

def shutdown():
    """
    Function to shut down the computer.
    Works for Windows, Linux, and macOS.
    """
    # Detect the operating system
    if os.name == 'nt':  # Windows
        os.system("shutdown /s /t 1")
    else:  # Linux or macOS
        os.system("shutdown -h now")

# Example usage:
# user_input = input("Do you want to shut down? (yes/no): ")
# if user_input.lower() == 'yes':
#     shutdown()
