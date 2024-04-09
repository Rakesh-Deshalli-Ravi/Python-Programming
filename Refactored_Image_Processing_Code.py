import numpy as np
import matplotlib.pyplot as plt

def generate_salt_pepper_noise(image, probability):
    """
    Generate salt-and-pepper noise in the given image.

    Args:
    - image: Input image as a NumPy array.
    - probability: Probability of adding salt or pepper noise to each pixel.

    Returns:
    - Noisy image with salt-and-pepper noise.
    """
    # If the image has 3 channels, convert it to a single channel (grayscale)
    if image.ndim == 3:
        image = np.dot(image[..., :3], [1, 0, 0])
    
    noisy_image = np.copy(image)
    
    # Create masks for salt and pepper noise based on probability
    salt_mask = np.random.rand(*image.shape) < probability / 2
    pepper_mask = np.random.rand(*image.shape) < probability / 2
    
    # Add salt noise (set pixel value to 255) and pepper noise (set pixel value to 0)
    noisy_image[salt_mask] = 255
    noisy_image[pepper_mask] = 0
    return noisy_image


def apply_custom_median_filter(image, window_size):
    """
    Apply a custom median filter to the given image.

    Args:
    - image: Input image as a NumPy array.
    - window_size: Size of the filter window (should be an odd number).

    Returns:
    - Filtered image using the custom median filter.
    """
    height, width = image.shape
    
    filtered_image = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            # Extract the window around the current pixel
            window = image[max(0, i - window_size // 2):min(height, i + window_size // 2 + 1),
                           max(0, j - window_size // 2):min(width, j + window_size // 2 + 1)]
            # Apply median operation to the window and assign the result to the current pixel
            filtered_image[i, j] = np.median(window)
    return filtered_image

def main():
    # Path to the image file
    image_path = "Depaul.jpg"
    # Read the input image using Matplotlib
    input_img = plt.imread(image_path)

    # Probability of adding noise to the image
    noise_probability = 0.80

    # Generate a noisy image with salt-and-pepper noise
    noisy_image = generate_salt_pepper_noise(input_img, noise_probability)

    # Window size for the median filter
    window_width = 8  
    # Apply custom median filter to the noisy image
    filtered_image = apply_custom_median_filter(noisy_image, window_width)

    # Display the images using Matplotlib
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(input_img, cmap='gray') 
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(noisy_image, cmap='gray') 
    plt.title('Noisy Image')

    plt.subplot(1, 3, 3)
    plt.imshow(filtered_image, cmap='gray') 
    plt.title('Filtered Image')

    plt.show()

if __name__ == "__main__":
    main()
