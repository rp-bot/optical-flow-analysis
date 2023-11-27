import numpy as np
from PIL import Image

# Load the image into a numpy array
img = Image.open('test.png')
img_array = np.array(img)

# Check if the image is grayscale
if len(img_array.shape) == 2 or img_array.shape[2] == 1:
    # Process the image starting from the bottom at x = 1313
    starting_x = 1313
    height = img_array.shape[0]

    # Initialize an empty list to store the points
    points = []

    # Iterate from the bottom to the top of the image
    # Adjust the loops to use while instead of for

# Re-initialize the array to hold the detected points
    detected_points = []

# Start at the bottom of the image and go up, scanning for changes in value
    for y in range(height - 1, -1, -1):  # Start at the bottom and move upwards
        left_change = None
        right_change = None
        x_left = starting_x
        x_right = starting_x

        # Scan to the left from the start position using a while loop
        while x_left >= 0:
            if img_array[y, x_left] != img_array[y, starting_x]:
                left_change = x_left + 1  # Mark the point after the change
                break
            x_left -= 1

        # Scan to the right from the start position using a while loop
        while x_right < img_array.shape[1]:
            if img_array[y, x_right] != img_array[y, starting_x]:
                right_change = x_right - 1  # Mark the point before the change
                break
            x_right += 1

        # Only record points if both a left and a right change were found
        if left_change is not None and right_change is not None:
            detected_points.append((y, left_change, right_change))

    # Convert the list of detected points to a numpy array
    detected_points_array = np.array(detected_points)
    detected_points_array[:10]  # Display the first 10 points for brevity

else:
    raise ValueError("Image is not in 8-bit grayscale format.")
