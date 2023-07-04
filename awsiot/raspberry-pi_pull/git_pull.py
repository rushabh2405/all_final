import os
import subprocess

def check_internet():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except:
        print("internet not avilable failed to update")
        return False

def main():
    flag=1
    if (os.path.exists("/home/raspberrypi/awsiot/raspberry-pi_pull/program") and check_internet()==True):
        subprocess.run(["rm", "-rf", "/home/raspberrypi/awsiot/raspberry-pi_pull/program"])
        flag = 0

    
    while flag == 0:
        try:
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/rushabh2405/raspberry-pi_send.git", "/home/raspberrypi/awsiot/raspberry-pi_pull/new_program/"])
            flag = 1
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
            
if __name__=="__main__":
        main()
