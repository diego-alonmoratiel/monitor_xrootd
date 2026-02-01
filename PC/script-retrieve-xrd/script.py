import os
import requests
import time
from XRootD import client

# --- CONFIGURATION ---
XROOTD_URL = "root://eospublic.cern.ch//eos/root-eos/h1"
FILES = ["dstarmb.root"]
RPI_URL = "http://192.168.0.40:5000/uploads"

def process_and_send():
    my_client = client.FileSystem(XROOTD_URL)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for file_name in FILES:
        local_path = os.path.join(current_dir, file_name)
        remote_path = f"{XROOTD_URL}/{file_name}"

        # 1. Download from XRootD
        print(f"Downloading {file_name}...")
        copyjob = client.CopyProcess()
        copyjob.add_job(remote_path, local_path)
        copyjob.prepare()
        copyjob.run()
 
        # 2. Send to the PI using HTTP POST
        for i in range(0, 10):
            if os.path.exists(local_path):
                print(f"Sending {file_name} to the PI via HTTP...")
                with open(local_path, 'rb') as f:
                    files = {'file': f}
                    response = requests.post(RPI_URL, files=files)
                if response.status_code == 200:
                    print("Sucess:", response.text)
                else:
                    print("Error:", response.status_code)
            else:
                print(f"File {file_name} cannot be found in {local_path}")
if __name__ == "__main__":
    process_and_send()
