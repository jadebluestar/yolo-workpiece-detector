import cv2
import numpy as np

def create_marker_image(marker_id=0, dictionary_type=cv2.aruco.DICT_4X4_50, size=200):
    """
    Generates an ArUco marker image using a specific ID and dictionary.

    Args:
        marker_id (int): The ID of the marker to generate.
        dictionary_type: The type of ArUco dictionary to use.
        size (int): The side length of the square marker image in pixels.
    """
    print(f"Generating marker with ID: {marker_id} and size: {size}x{size} pixels.")
    
    # Get the predefined ArUco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary_type)
    
    # Create the marker image
    tag = np.zeros((size, size, 1), dtype="uint8")
    cv2.aruco.drawMarker(aruco_dict, marker_id, size, tag, 1)
    
    # Save the generated marker image
    output_path = f"generated_marker_{marker_id}.png"
    cv2.imwrite(output_path, tag)
    print(f"Marker image saved to {output_path}")
    
    return tag

if __name__ == "__main__":
    # Create a dummy marker image with ID 0, matching the label file
    # This simulates creating a new marker to "add" to your dataset
    marker_image = create_marker_image(marker_id=0)
    
    # You can also use this to show how different markers could be generated
    # create_marker_image(marker_id=5, size=300)