import os
files = os.listdir("exe7folder")
i = 1
for file in files :
    if file.endswith(".png"):
        print(file)
    os.rename(f"exe7folder/{file}",f"exe7folder/{i}.png")
    i = i+1