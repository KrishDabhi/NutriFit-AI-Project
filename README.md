# NutriFit AI 🥦📸  
*Your personal AI nutrition coach right from your food label.*

NutriFit AI is a that uses **computer vision**, **structured rule-based logic**, and a **local LLM** to help users—especially those with dietary restrictions like diabetes understand food labels, receive personalized health feedback, and discover healthier alternatives from the **Open Food Facts** open database.

Built entirely with **open-source, privacy-respecting tools**, this project demonstrates a full-stack AI pipeline aligned with **Azure AI engineering principles**: modular design, local inference, responsible data use, and user-centric empathy.

---

## 🌟 Overview

Users upload a photo of a packaged food label → NutriFit AI extracts and parses nutrition facts → applies health rules based on user profile → generates plain-language advice using a **locally run Mistral LLM** → suggests verified healthier swaps from **Open Food Facts**.

All processing happens **on-device**. No cloud APIs. No data leaks. Just smart, ethical AI for everyday health.

---

## 🗂️ Project Architecture (4-Week Phased Build)

### **First Step: Computer Vision + OCR Pipeline**
- Preprocess real-world food label images (OpenCV): resize, denoise, deskew, contrast enhancement.
- Extract text robustly using **EasyOCR** (supports multilingual labels).
- Output: Clean, raw text ready for structured parsing.

### **Second Step: Nutrition Parsing + Health Rule Engine**
- Parse unstructured OCR output into structured fields: *calories, total sugar, added sugar, saturated fat, sodium, serving size*, etc.
- Apply user-defined health rules:
  - Diabetic mode: flag if **added sugar > 5g/serving**
  - Hypertension mode: warn if **sodium > 140mg/serving**
  - Custom thresholds via UI input
- Validate consistency (e.g., total carbs ≥ sugar).

### **Third Step: Local LLM Advisor + Open Food Facts Integration**
- Use **Ollama** to run **Mistral 7B** locally—no internet or API keys required.
- Prompt engineering for empathetic, non-judgmental feedback (e.g., *“This snack has 12g of added sugar—more than two servings for someone managing diabetes. Would you like a lower-sugar option?”*).
- Query **Open Food Facts API** to fetch real, verified healthier alternatives by category or nutrient similarity.
- Fallback to cached/local logic if API is unreachable.

### **Fourth step: Streamlit Web Demo**
- Unified UI for:
  - Image upload
  - Health profile selection (diabetic, hypertensive, general wellness)
  - Real-time feedback panel
  - Alternative product cards with NOVA score, Nutri-Score, and ingredients
- Session state management for seamless UX.

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|-----------|
| **Image Processing** | OpenCV, Pillow |
| **OCR** | EasyOCR |
| **Data Parsing** | Python, Pandas, Regex |
| **Rule Engine** | Custom Python logic (extensible) |
| **LLM** | Mistral 7B via **Ollama** (local inference) |
| **Nutrition Database** | [Open Food Facts](https://world.openfoodfacts.org/data) (ODbL licensed) |
| **Frontend** | Streamlit |
| **Environment** | Python 3.10+, Conda/venv |
| **Deployment** | Local (demo-ready); Dockerizable |

> 🔐 **Privacy by Design**: All sensitive processing (OCR, parsing, LLM) runs on the user’s machine. Open Food Facts is only used for **public, non-personal product data**.

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running
- Git

### Steps

```bash
# 1. Clone repo
git clone https://github.com/your-username/nutrifit-ai.git
cd nutrifit-ai

# 2. Set up environment
conda create -n nutrifit python=3.10 -y
conda activate nutrifit

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull Mistral model (run once)
ollama pull mistral

# 5. Launch app
streamlit run app.py
