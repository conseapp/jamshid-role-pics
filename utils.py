from PIL import Image
from pathlib import Path
from io import BytesIO
import tempfile


def process_image(input_path: Path, quality: int = 30) -> Path:
    # Open the image from the input path
    with open(input_path, 'rb') as file:
        image_data = BytesIO(file.read())
        image = Image.open(image_data)

    # Perform any image processing here if needed

    # Create a temporary file to store the processed image data
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        # Export the image to the temporary file without saving it as a separate file on disk
        image.save(temp_file, format='JPEG', quality=quality)

    # Return the Path object of the temporary file
    return Path(temp_file.name)

# RETURNS BYTES

# def process_image(input_path: Path, quality: int = 30) -> BytesIO:
#     # Open the image from the input path
#     with open(input_path, 'rb') as file:
#         image_data = BytesIO(file.read())
#         image = Image.open(image_data)
#
#     # Perform any image processing here if needed
#
#     # Create a new BytesIO object to store the processed image data
#     output_data = BytesIO()
#
#     # Export the image to the output BytesIO object without saving it as a file
#     image.save(output_data, format='JPEG', quality=quality)
#
#     # Move the cursor to the beginning of the BytesIO object
#     output_data.seek(0)
#
#     return output_data
