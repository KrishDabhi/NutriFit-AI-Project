import torch
from torchvision import models, transforms
from PIL import Image

# Load model once (do this in main.py in practice to avoid reloading)
_model = models.mobilenet_v3_small(weights='IMAGENET1K_V1')
_model.eval()

# ImageNet preprocessing pipeline
_preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load class labels (optional)
with open('../../assets/imagenet_labels.txt') as f:
    _labels = [line.strip() for line in f.readlines()]

def classify_grocery_item(image_path):
    """
    Takes an image path, returns top-3 predicted ImageNet classes.
    Example output: [('potato chip', 0.82), ('corn chip', 0.12), ('pretzel', 0.03)]
    """
    img = Image.open(image_path).convert("RGB")
    input_tensor = _preprocess(img)
    input_batch = input_tensor.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = _model(input_batch)

    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top3_prob, top3_catid = torch.topk(probabilities, 3)
    
    results = []
    for i in range(3):
        label = _labels[top3_catid[i]]
        prob = top3_prob[i].item()
        results.append((label, prob))
    return results