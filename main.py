from PIL import Image

def text_to_binary(text):
    binary_values = [format(ord(char), '08b') for char in text]

    binary_string = ''.join(binary_values)

    return binary_string

def binary_to_hexadecimal(binary_str):
    
    decimal_value = int(binary_str, 2)
    hexadecimal_value = hex(decimal_value)[2:]

    return hexadecimal_value

def encode_binary_to_image(binary_str, image_size):
    num_pixels = len(binary_str)
    image = Image.new("1", (num_pixels, 1), color=255)

    # Create an iterator for the binary string
    binary_iterator = iter(binary_str)

    
    for x in range(num_pixels):
        pixel_value = int(next(binary_iterator))
        image.putpixel((x, 0), pixel_value)

    
    image = image.resize(image_size)

    return image

# Get text input from the user
text_input = input("Enter the text: ")

# Translate text to binary
binary_output = text_to_binary(text_input)

# Translate binary to hexadecimal
hexadecimal_output = binary_to_hexadecimal(binary_output)


image_size = (100, 100)


image = encode_binary_to_image(binary_output, image_size)

# Save the image as a PNG file
image.save("output_image.png")

# Display the results
print("Text:", text_input)
print("Binary:", binary_output)
print("Hexadecimal:", hexadecimal_output.upper())
print("Image saved as 'output_image.png'")
