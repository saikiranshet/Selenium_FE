import shutil
import os

folders_to_clean = ["logs", "reports", "screenshots"]

for folder in folders_to_clean:
    path = os.path.join(os.getcwd(), folder)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Deleted {path}")
    os.makedirs(path, exist_ok=True)
