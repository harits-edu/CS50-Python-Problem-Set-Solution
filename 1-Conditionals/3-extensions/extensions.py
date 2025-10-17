def main():
    filename = input("File name: ")
    parts = filename.strip().lower().split('.')
    type = parts[-1]
    extensions(type)

def extensions(suffix):
    match suffix:
        case "jpg" | "jpeg":
            print("image/" + "jpeg")
        case "gif" | "png":
            print("image/" + suffix)
        case "pdf" | "zip":
            print("application/" + suffix)
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
