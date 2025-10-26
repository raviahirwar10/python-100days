import os

folders = os.listdir("data")

print(os.getcwd())
os.chdir("/users/rk853/onedrive/desktop/python-100days")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))