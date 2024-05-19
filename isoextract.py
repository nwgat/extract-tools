import os
import subprocess

def main():
    ISOI = input("Enter iso you want to extract: ")
    os.makedirs(f"/mnt/{ISOI}", exist_ok=True)
    subprocess.run(["mount", "-o", "loop", ISOI, f"/mnt/{ISOI}"])
    subprocess.run(["cp", "-r", f"/mnt/{ISOI}", f"{os.getcwd()}/{ISOI}.out"])
    subprocess.run(["umount", f"/mnt/{ISOI}"])

if __name__ == "__main__":
    main()
