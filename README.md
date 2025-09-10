# Marker Detector: YOLOv5 for UNIQUE Marker Detection

This project contains a trained YOLOv5 model designed for the fast and accurate detection of a specific type of ArUco marker. The model was trained to recognize a single class: `marker`.\

---
### Why YOLO, why not OpenCV?
The standard OpenCV library includes built-in functions for ArUco marker detection, but these methods can sometimes struggle in less-than-ideal conditions such as low lighting, motion blur, or when markers are partially occluded. By training a robust object detection model like YOLOv5 on a custom dataset of these markers, we can achieve more reliable and faster detection, especially in challenging real-world scenarios.

---
### Marker Generation

The target marker used for this project is an ArUco code generated using a public web tool. The code is a `4x4` binary matrix with an ID of `0`. This is a common and easily reproducible type of marker, making the dataset creation process straightforward.

<img width="208" height="222" alt="Screenshot 2025-09-10 130308" src="https://github.com/user-attachments/assets/640c3604-f3e9-44c4-b828-23836378569e" />

### Dataset and Training

The dataset for training the YOLO model was created by:
1.  Generating the target ArUco marker image.
2.  Capturing a variety of images of the marker in different environments, lighting conditions, and from various angles.
3.  Manually labeling the bounding boxes for the marker in each image using the YOLO format.

The model was then trained using the `train.py` script, which fine-tunes a pretrained YOLOv5 architecture on this custom dataset. The training process focused on optimizing for high precision and recall to ensure the model reliably locates the marker.

---
### File Structure

-   **`data/`**: Contains the images and corresponding YOLO annotations (`.txt` files) used for training.
-   **`models/`**: Stores the final trained model weights (`yolo_marker.pt`).
-   **`train.py`**: The script used to train the model.
-   **`detect.py`**: The script for running inference on new images or video streams.
-   **`utils.py`**: Helper functions for data processing and visualization.


