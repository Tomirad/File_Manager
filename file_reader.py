def main(src_path, images = []):
    print(f"{images[0]} File:", src_path)
    file = open(src_path)
    print(file.read())
