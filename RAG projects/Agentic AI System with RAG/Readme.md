# 🤖 Agentic AI System with RAG

An **autonomous multi-agent system** built using **Streamlit**, integrating **ETL, Analysis, Forecasting, Retrieval-Augmented Generation (RAG), and Recommendation** agents.  
It enhances analytical reasoning — including *“why”* and open-ended strategic questions — using contextual retrieval and predictive modeling.

---

## 🚀 Key Features

### 🧩 Multi-Agent Framework
**Five autonomous agents working together:**
1. **ETL Agent** – Cleans and audits uploaded data (missing values, duplicates, etc.)
2. **Analysis Agent** – Answers *why*, *what*, and *which* type business questions automatically
3. **RAG Agent** – Retrieves relevant business context for enhanced interpretability
4. **Forecast Agent** – Predicts future sales/performance using ARIMA or Linear Regression
5. **Recommendation Agent** – Generates strategic business actions from insights

---

## 🧠 Intelligent “Why” Question Handler
- Handles analytical “why” and strategic queries (e.g., *“Why is Electronics performing best?”*)
- Automatically identifies performance drivers (sales, ratings, profit, etc.)
- Provides comparative metrics and insights across categories

---

## ⚙️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Language** | Python |
| **Frontend** | Streamlit |
| **Data Handling** | Pandas, NumPy |
| **Machine Learning** | scikit-learn, statsmodels |
| **Vector Database** | ChromaDB (for RAG) |
| **Forecasting Models** | ARIMA, Linear Regression |
| **Visualization/UI** | Streamlit custom CSS styling |

---

## How to Run the Project

1. Clone the repo
git clone then cd 

2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Linux/Mac
ou
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Launch the app (official method)
run the notebook

## Demo Video


https://github.com/user-attachments/assets/f0f1af35-d828-489f-86dc-49364e9359e3



## 🧩 Project Architecture

```plaintext
User Input (JSON data + Question)
        ↓
   [ ETL Agent ] → Data Cleaning
        ↓
   [ Analysis Agent ] → Insights & Why Analysis
        ↓
   [ RAG Agent ] → Contextual Enhancement from Documents
        ↓
   [ Forecast Agent ] → Predictive Trends
        ↓
   [ Recommendation Agent ] → Strategic Suggestions
        ↓
   Streamlit UI → Interactive Display & Download


