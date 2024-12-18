from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    # Convert pixels to a larger integer type to avoid overflow
    encrypted_pixels = (pixels.astype(np.int32) + key) % 256  # Ensure pixel values stay within 0-255
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value
    # Convert pixels to a larger integer type to avoid overflow
    decrypted_pixels = (pixels.astype(np.int32) - key) % 256  # Ensure pixel values stay within 0-255
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    print("Image Encryption Tool")
    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            input_image_path = input("Enter the path of the image: ")
            output_image_path = input("Enter the output path for the image: ")
            key = int(input("Enter a key (integer value for pixel manipulation): "))

            if choice == 'E':
                encrypt_image(input_image_path, output_image_path, key)
            elif choice == 'D':
                decrypt_image(input_image_path, output_image_path, key)
        else:
            print("Invalid choice. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()