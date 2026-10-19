import os
import subprocess

# BAD: Hardcoded secret (Will trigger Bandit B105 / hardcoded password check)
DATABASE_PASSWORD = "super_secret_admin_password_123"

def insecure_command_runner(user_input):
    # BAD: Unsafe use of shell execution (Will trigger Bandit security warnings)
    os.system("echo " + user_input)

if __name__ == "__main__":
    insecure_command_runner("Hello Test")