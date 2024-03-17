import replicate
import os
from dotenv import load_dotenv
from PIL import Image
load_dotenv()

with open("images/vibranium.jpg", "rb") as f:
    image_bytes = f.read()

text_extract = replicate.run(
    "abiruyt/text-extract-ocr:a524caeaa23495bc9edc805ab08ab5fe943afd3febed884a4f3747aa32e9cd61",
        input={},
        files=[("image", image_bytes)]
)

print(text_extract)