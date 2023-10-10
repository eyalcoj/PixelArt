from PIL import Image


def pixelate_image(input_path, output_path, pixel_size):
    # Open the input image
    image = Image.open(input_path)

    # Calculate the new size with integer division
    width, height = image.size
    new_width = width // pixel_size
    new_height = height // pixel_size

    # Resize the image to the new size
    small_image = image.resize((new_width, new_height), resample=Image.NEAREST)

    # Resize the small image back to the original size
    pixelated_image = small_image.resize(image.size, resample=Image.NEAREST)

    # Save the pixelated image
    pixelated_image.save(output_path)


if __name__ == "__main__":
    input_image_path = r"C:\Users\Eyal\Downloads\Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched (1).jpg"  # Replace with the path to your input image
    output_image_path = r"C:\Users\Eyal\Desktop.THE_PIC.jpg"  # Replace with the desired output path
    pixel_size = 10  # Adjust this value to control the pixelation level

    pixelate_image(input_image_path, output_image_path, pixel_size)
