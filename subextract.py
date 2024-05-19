import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = f"{input_file}.ass"

    try:
        # Run the ffmpeg command
        subprocess.run(["ffmpeg", "-hide_banner", "-i", input_file, "-map", "0:s:0", output_file], check=True)
        print(f"Subtitle file '{output_file}' created successfully.")
    except subprocess.CalledProcessError:
        print("Error executing ffmpeg command.")

if __name__ == "__main__":
    main()
