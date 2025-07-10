import math
import sys
from PIL import Image, ImageFilter, ImageEnhance

# Ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: python filter.py filename")

# Open image
image = Image.open(sys.argv[1]).convert("RGB")

# Filter image according to edge detection kernel
filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))

# Debug: Save the filtered image to see what it looks like
filtered.save("debug_filtered.png")
print("Filtered image saved as debug_filtered.png")

# Method 1: Try enhancing contrast to make edges more visible
enhancer = ImageEnhance.Contrast(filtered)
enhanced = enhancer.enhance(2.0)  # Increase contrast
enhanced.save("debug_enhanced.png")
print("Enhanced image saved as debug_enhanced.png")

# Method 2: Convert to grayscale for better edge detection
gray_image = image.convert("L")
gray_filtered = gray_image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))
gray_filtered.save("debug_gray_filtered.png")
print("Grayscale filtered image saved as debug_gray_filtered.png")

# Method 3: Use a different scale to normalize the result
normalized_filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1,
    offset=128  # Add offset to brighten the image
))
normalized_filtered.save("debug_normalized.png")
print("Normalized image saved as debug_normalized.png")

# Show all versions
try:
    filtered.show()
    print("Original filtered image displayed")
except Exception as e:
    print(f"Error showing original filtered image: {e}")

try:
    enhanced.show()
    print("Enhanced image displayed")
except Exception as e:
    print(f"Error showing enhanced image: {e}")

try:
    gray_filtered.show()
    print("Grayscale filtered image displayed")
except Exception as e:
    print(f"Error showing grayscale filtered image: {e}")

try:
    normalized_filtered.show()
    print("Normalized image displayed")
except Exception as e:
    print(f"Error showing normalized image: {e}")
