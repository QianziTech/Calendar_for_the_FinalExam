
import modules.photo_hashing as photo_hashing

if __name__ == "__main__":
    image_path = "receipt.png"
    text=photo_hashing.process_image(image_path)