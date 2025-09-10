import cv2
import yaml
import numpy as np

def load_config(config_path="config.yaml"):
    """
    Loads a dummy configuration file.
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        print("Configuration loaded.")
        return config
    except FileNotFoundError:
        print("Dummy config.yaml not found. Using default values.")
        return {
            'model_name': 'yolov5s',
            'epochs': 50,
            'batch_size': 16,
            'image_size': 416
        }

def visualize_bbox(image, bbox, label="marker", color=(0, 255, 0)):
    """
    Simulates drawing a bounding box on an image.
    
    Args:
        image (np.array): The input image.
        bbox (list): [x_min, y_min, x_max, y_max]
        label (str): Label for the bounding box.
        color (tuple): BGR color for the box.
    """
    x_min, y_min, x_max, y_max = [int(val) for val in bbox]
    
    # Draw rectangle
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)
    
    # Draw label
    cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return image
    
def calculate_metrics(predictions, ground_truths):
    """
    Simulates calculation of dummy detection metrics.
    """
    print("Calculating dummy metrics...")
    
    # These are fake metric values
    precision = np.random.uniform(0.85, 0.95)
    recall = np.random.uniform(0.90, 0.98)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1_score:.4f}")
    
    return precision, recall, f1_score

if __name__ == "__main__":
    # Example usage of a dummy utility function
    dummy_image = np.zeros((200, 200, 3), dtype=np.uint8)
    dummy_bbox = [50, 50, 150, 150]
    
    image_with_box = visualize_bbox(dummy_image, dummy_bbox)
    print("Dummy image with bounding box created.")