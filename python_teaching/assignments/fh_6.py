# Write a function to copy binary file using "rb"/"wb"

def copy_binary_file(source_path, destination_path):
    try:
        with open(source_path, "rb") as src_file:
            with open(destination_path, "wb") as dest_file:
                # Read and write in chunks to handle large files
                while chunk := src_file.read(4096):  # 4KB chunk
                    dest_file.write(chunk)
        print(f"File copied successfully from '{source_path}' to '{destination_path}'")
    except FileNotFoundError:
        print(f"Source file '{source_path}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")


copy_binary_file("source_image.jpg", "copied_image.jpg")