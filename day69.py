# multiprocessing
import multiprocessing
import requests
import os

def downloadfile(url, name):
    print(f"Started downloading {name}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(f"files/file{name}.jpg", "wb") as f:
            f.write(response.content)
        print(f"Finished downloading {name}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)
    url = "https://picsum.photos/200/300"
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadfile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()