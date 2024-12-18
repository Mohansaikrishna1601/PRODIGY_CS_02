## Image Encryption/Decryption Tool


## Description 

This Python script implements a simple image encryption and decryption tool. The tool allows users to encrypt and decrypt images using a specified integer key. The encryption process involves modifying the pixel values of the image based on the key, ensuring that the original image is transformed into an encrypted version and vice versa.

# Features
  -Encrypt Images: Converts an original image into an encrypted image by adding a key value to each pixel.
  -Decrypt Images: Converts an encrypted image back into its original form by subtracting the key value from each pixel.
  -Interactive Interface: Provides a user-friendly command-line interface for choosing between encryption, decryption, or quitting the program.

# How It Works
   -Encryption: Each pixel value in the input image is modified by adding a specified key value. The operation ensures the pixel values remain within the valid range (0-255) using modulo 256.
   -Decryption: The encrypted pixel values are restored to their original values by subtracting the same key value. The operation ensures the pixel values remain within the valid range (0-255) using modulo 256.
   -Key: The script supports any integer key value for pixel manipulation.

## Code Explanation

    encrypt_image(input_image_path, output_image_path, key):
  -Opens the input image and converts it to a NumPy array of pixels.
  -Encrypts the image by adding the key value to each pixel and ensures the pixel values stay within 0-255 using modulo 256.
  -Saves the encrypted image to the specified output path.

    decrypt_image(input_image_path, output_image_path, key):
  -Opens the encrypted image and converts it to a NumPy array of pixels.
  -Decrypts the image by subtracting the key value from each pixel and ensures the pixel values stay within 0-255 using modulo 256.
  -Saves the decrypted image to the specified output path.

    main():
  -Provides an interactive interface for the user to choose between encryption, decryption, or quitting the program.
  -Prompts the user to enter the image paths and key value.
  -Calls the appropriate function based on user choice and displays the result.

## Usage
Clone the Repository:

    git clone https://github.com/Mohansaikrishna1601/PRODIGY_CS_01.git
    cd PRODIGY_CS_01

Install Required Libraries:

    pip install pillow numpy

Run the Script:

    python image_encryption_tool.py

# Follow the Prompts:  
- Choose whether to encrypt, decrypt, or quit.
- Enter the input image path, output image path, and the key value.
- View the encrypted or decrypted image saved to the specified output path.

# Example 
-Image Encryption Tool
-Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? E
-Enter the path of the image: input_image.jpg
-Enter the output path for the image: encrypted_image.jpg
-Enter a key (integer value for pixel manipulation): 50
-Image encrypted and saved as encrypted_image.jpg

# Requirements  
- Python 3.x
- Pillow (PIL)
- NumPy

# Author
- Mohan Saikrishna

