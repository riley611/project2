"""Run a command-line test securely."""

import subprocess
import sys


def secure_command_runner(user_input):
    """Print user input by passing it as a subprocess argument."""
    subprocess.run(
        [sys.executable, "-c", "import sys; print(sys.argv[1])", user_input],
        check=True,
    )

if __name__ == "__main__":
    secure_command_runner("Secure Test Complete")
