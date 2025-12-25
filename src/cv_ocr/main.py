from cv_ocr.preprocess import preprocess_image
from cv_ocr.extract_text import extract_text_from_image
from cv_ocr.classify_item import classify_grocery_item
import sys
import json

def analyze_food_item(image_path):
    # 1. Classify the item type
    categories = classify_grocery_item(image_path)
    predicted_type = categories[0][0]  # e.g., "potato chip"

    # 2. Extract text (nutrition info)
    processed_img = preprocess_image(image_path)
    nutrition_text = extract_text_from_image(processed_img)

    return {
        "item_category": predicted_type,
        "nutrition_text": nutrition_text,
        "top3_categories": categories
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/cv_ocr/main.py <image_path>")
        sys.exit(1)
    
    img_path = sys.argv[1]
    result = analyze_food_item(img_path)
    print(json.dumps(result, indent=2))