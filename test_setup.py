import cv2
import easyocr
import torch
import torchvision
from PIL import Image
import numpy as np

print("✅ OpenCV version:", cv2.__version__)
print("✅ EasyOCR loaded")
print("✅ PyTorch version:", torch.__version__)
print("✅ TorchVision version:", torchvision.__version__)
print("✅ Pillow version:", Image.__version__)
print("✅ NumPy version:", np.__version__)

# Test EasyOCR initialization
reader = easyocr.Reader(['en'])
print("✅ EasyOCR initialized successfully")

# Test PyTorch model loading
model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
print("✅ PyTorch model loaded successfully")