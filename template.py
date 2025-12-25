import os
import sys

def create_folder_structure():
    """Create the folder structure for NutriFit AI project."""
    directories = [
        "data/raw",
        "data/processed",
        "src/cv_ocr",
        "assets",
        "tests"
    ]
    
    files = [
        "src/cv_ocr/__init__.py",
        "src/cv_ocr/preprocess.py",
        "src/cv_ocr/extract_text.py",
        "src/cv_ocr/classify_item.py",
        "src/cv_ocr/main.py",
        "assets/imagenet_labels.txt",
        "tests/test_ocr_and_classify.py",
        "requirements.txt",
        "README.md"
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create files
    for file_path in files:
        with open(file_path, 'w') as f:
            if file_path == "src/cv_ocr/__init__.py":
                f.write('"""\nNutriFit AI - Computer Vision and OCR Package\n"""\n')
            elif file_path == "src/cv_ocr/preprocess.py":
                f.write('"""\nImage preprocessing for OCR module\n"""\nimport cv2\nimport numpy as np\n\ndef preprocess_image(image_path):\n    """Preprocess image for OCR."""\n    pass\n')
            elif file_path == "src/cv_ocr/extract_text.py":
                f.write('"""\nOCR text extraction module\n"""\nimport easyocr\n\ndef extract_text_from_image(image_path):\n    """Extract text from image using EasyOCR."""\n    pass\n')
            elif file_path == "src/cv_ocr/classify_item.py":
                f.write('"""\nGrocery item classification module\n"""\nimport cv2\nimport numpy as np\n\ndef classify_grocery_item(image_path):\n    """Classify grocery items in image."""\n    pass\n')
            elif file_path == "src/cv_ocr/main.py":
                f.write('"""\nMain module orchestrating OCR and classification\n"""\n\ndef main():\n    """Main function."""\n    pass\n\nif __name__ == "__main__":\n    main()\n')
            elif file_path == "assets/imagenet_labels.txt":
                f.write("# ImageNet class labels for grocery item classification\n")
            elif file_path == "tests/test_ocr_and_classify.py":
                f.write('"""\nTests for OCR and classification modules\n"""\nimport unittest\n\nclass TestOCRAndClassify(unittest.TestCase):\n    def test_ocr_extraction(self):\n        pass\n\nif __name__ == "__main__":\n    unittest.main()\n')
            elif file_path == "requirements.txt":
                f.write("opencv-python\nnumpy\neasyocr\nstreamlit\n")
            elif file_path == "README.md":
                f.write("# NutriFit AI\n\nComputer Vision and OCR based food recommendation system.\n")
        
        print(f"Created file: {file_path}")
    
    print("\nFolder structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()