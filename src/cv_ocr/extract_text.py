import easyocr

def extract_text_from_image(image):
    """
    Takes a preprocessed image (numpy array) and returns OCR text.
    Uses EasyOCR with English (add 'hi' or 'gu' later if needed).
    """
    reader = easyocr.Reader(['en'], gpu=False)  # Set to True if you have a GPU later
    results = reader.readtext(image, detail=0)  # Just text, no bounding boxes
    return " ".join(results)