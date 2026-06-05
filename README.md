# UnderwriteAI 🏦
> RAG-Based Insurance Underwriting Assistant powered by LLMs, LangChain & FAISS

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red) ![LangChain](https://img.shields.io/badge/LangChain-RAG-green) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📌 Overview
UnderwriteAI automates insurance policy underwriting by extracting risk insights from PDF documents using a Retrieval-Augmented Generation (RAG) pipeline — similar to enterprise underwriting platforms used in InsurTech.

---

## 🖥️ Demo

| App Interface | Risk Assessment |
|---|---|
| <img width="960" height="540" alt="App" src="https://github.com/user-attachments/assets/bf7d2bcb-91d3-4f93-a4eb-a458c41099d8" /> | <img width="960" height="540" alt="Risk" src="https://github.com/user-attachments/assets/df269494-4ba2-4920-8285-87fda9787c07" /> |

| Underwriting Report | RAG Q&A |
|---|---|
| <img width="960" height="540" alt="Report" src="https://github.com/user-attachments/assets/291c49ec-81b9-48ed-9c17-9126a3ea1ff1" /> | <img width="173" height="443" alt="QA" src="https://github.com/user-attachments/assets/1691b693-3b71-485f-99e3-3dd5d5b6c955" /> |

---

## ✨ Features
| Feature | Description |
|---|---|
| 📄 PDF Processing | Upload & parse insurance policy documents |
| 📊 Risk Assessment | Automated risk scoring (0-10) with identified risks |
| ✅ Approval Recommendation | Decision + Confidence Score + Reasoning |
| 🔍 Missing Information Detection | Flags incomplete policy data |
| 📝 Underwriting Report | Full structured report generation |
| 💬 RAG Q&A | Ask natural language questions about the policy |

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM Framework:** LangChain
- **Vector Store:** FAISS
- **LLM:** Gemini / OpenAI
- **PDF Parsing:** PyPDF2
- **Language:** Python 3.10+

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Sneha8271/UnderwriteAI.git
cd UnderwriteAI

# Install dependencies
pip install -r requirements.txt

# Add your API key in .env
GOOGLE_API_KEY=your_key_here

# Run the app
streamlit run app.py
```

---

## 👩‍💻 Author
**Sneha Singh** — [GitHub](https://github.com/Sneha8271) | [LinkedIn](https://linkedin.com/in/your-profile)