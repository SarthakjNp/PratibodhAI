# PratibodhAI (प्रतिबोधAI)

**PratibodhAI** is an academic, ML-based reflective system inspired by the *Bhagavad Gita*.  
It is designed to help users reflect on their internal dilemmas by surfacing contextually relevant verses and explaining their philosophical setting in a calm, neutral tone.

> ⚠️ **Important Disclaimer**:  
> This system does **not** provide religious, moral, medical, or psychological advice.  
> It is a contextual reflection and learning tool only.

---

## 🎯 Project Objective

The objective of PratibodhAI is to demonstrate:

- **Contextual Semantic Retrieval** using Machine Learning (NLP).
- **Ethical AI Design** regarding religious/philosophical material.
- **UI/UX Implementation** aligned with reflective, non-intrusive interaction.

Instead of a standard keyword search, the system retrieves verses based on **semantic similarity** between the user's emotional state and the philosophical context of the verse.

---

## 🧠 Core Architecture

Most religious apps use simple keyword matching or direct translation. **PratibodhAI takes a semantic approach**:

1.  **Vector Embeddings**: The system uses `sentence-transformers` to create high-dimensional vector representations of the Gita's verses (based on meaning and context).
2.  **Cosine Similarity**: User input is converted into a vector and compared against the verse database to find the closest semantic match.
3.  **No Generative Hallucinations**: The system strictly retrieves existing verses and definitions; it does not generate new religious text, ensuring academic safety.

---

## 🏗️ Project Structure

```text
PratibodhAI/
│
├── app.py              # Main Streamlit application logic & UI
├── data/
│   └── Geeta.json      # Preprocessed verse dataset (JSON format)
├── assets/
│   └── logo.jpeg       # Project logo (used in UI & background watermark)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
## 📚 Dataset Description
1. Source: Publicly available Bhagavad Gita dataset (JSON).
2. Data Points Used:
3. Sanskrit Shloka
4. English Transliteration
5. Word-for-Word Meanings
6. English Translation (for embedding context)
7. Chapter & Verse Reference

## 🧪 Machine Learning Approach
> Model: sentence-transformers/all-MiniLM-L6-v2
> Why this model? It offers a balance of speed and semantic accuracy, perfect for local deployment without heavy GPU requirements.
> Technique: Semantic Search / Dense Vector Retrieval.
> Metric: Cosine Similarity.

## 🚀 Running the Project Locally
1️⃣ Clone the Repository
```
git clone <your-repo-url>
cd PratibodhAI
```

2️⃣ Create a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the Application
```
streamlit run app.py
```
The application will automatically open in your default web browser at http://localhost:8501.

## Sample Prompts to TestTo verify that the semantic retrieval is working correctly
```
"I am constantly worried about the results of my exams and can't focus on studying."
"I feel confused and don't know which path to take in life."
"My mind is very restless and I cannot control my anger."
"I feel like giving up because the task is too difficult."
```
### 👤 Author
**Sarthak Jain**
