import requests

URL = "http://localhost:5000/upload"

def file_upload(i):
    with open("./testfiles/file_to_upload.txt", "rb") as file:
        file_name = "file_to_upload_{}.txt".format(str(i))
        #file_name = "tails-amd64-6.4.img"
        files = {"file": (file_name, file)}
        response = requests.post(URL, files=files)
    if response.status_code == 200:
        return f'{file_name} upload successful'
    else:
        print(f"Failed to upload file. Status code: {response.status_code}")


def main():
    for i in range(0,15):
        print(file_upload(i))


if __name__ == '__main__':
    main()