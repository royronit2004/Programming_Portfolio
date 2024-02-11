# EXTENSIONS

def main():
    # Prompt the user for input (file name)
    file_name = input("File Name: ")

    # Convert the file name to lowercase
    file_name = file_name.lower()

    # Check the file's suffix and output the corresponding media type
    if file_name.endswith(".gif") or file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        print("image/" + file_name.split('.')[-1])
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
