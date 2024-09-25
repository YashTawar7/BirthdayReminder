import base64
from io import BytesIO
from PIL import Image


def decode_base64_image(base64_string):
    # Remove the data URL prefix if present
    if base64_string.startswith('data:image'):
        base64_string = base64_string.split(',', 1)[1]

    # Decode the Base64 string
    image_data = base64.b64decode(base64_string)

    # Create an in-memory stream from the decoded image data
    stream = BytesIO(image_data)

    # Open the image using PIL (Python Imaging Library)
    image = Image.open(stream)

    return image


# Example usage
base64_string = 'data:image/png;base64,iVBORw0KG...'
decoded_image = decode_base64_image(base64_string)

# Show the decoded image
decoded_image.show()
