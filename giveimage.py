# **Import the necessary libraries.**
import os
from PIL import Image
import pytesseract


# 2. **Prompt the user to select an image file.**

#    ```python
# Load the image file.
image_path = input("Enter the path to the image file: ")

image = Image.open(image_path)

# Print the image size to verify successful loading.
print(f"Image size: {image.size}")

   

# 4. **Convert the image to grayscale.**


image = image.convert("L")


# 5. **Perform OCR on the image.**

#    ```python
text = pytesseract.image_to_string(image)
   

# 6. **Send the text to the Gemini API.**

#    ```python
import requests

url = "https://api.gemini.com/v1/ocr"

data = {"text": text}

response = requests.post(url, data)

# 7. **Parse the API response.**

#    ```python
json_data = response.json()

if json_data["status"] == "success":
       print("The text was successfully converted to Unicode.")
       print("The Unicode text is:")
       print(json_data["text"])
else:
       print("An error occurred while converting the text to Unicode.")
       print(json_data["error"])
   
# 8. **Save the converted text to a file.**

#    ```python
with open("converted_text.txt", "w") as f:
    f.write(json_data["text"])