import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Basic preprocessing to improve OCR accuracy:
    - Read image
    - Convert to grayscale
    - Apply Gaussian blur to reduce noise
    - Enhance contrast (optional: CLAHE)
    - Return preprocessed image (numpy array)
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Optional: Denoise
    denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
    
    # Optional: Contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)
    
    return enhanced