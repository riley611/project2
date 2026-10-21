import subprocess
import sys

DATABASE_PASSWORD = "1H0P3_iPASS645"

def insecure_command_runner(user_input):
    subprocess.run(
        [sys.executable, "-c", "import sys; print(sys.argv[1])", user_input],
        check=True,
    )

if __name__ == "__main__":
    insecure_command_runner("Initial Test Complete")