

# Customer Retention and Revenue Insights 🚀

An end-to-end AI-powered solution that combines machine learning, business intelligence, and LLM-driven analytics to predict customer churn and optimize revenue performance.

![Power BI Dashboard Preview](https://github.com/KinsunDasK/Customer_Retension_and_Revenue_Insights/blob/main/dashboard_preview.png)

## 🔍 Project Overview
This project is designed to empower business stakeholders with:
- Predictive insights into customer churn
- Visual analytics via Power BI
- A sleek Streamlit web interface
- LLM-powered chatbot for real-time querying

## 📁 Repository Structure
```
├── churn/
│   ├── datasets/
│   │   ├── raw_dataset.csv
│   │   └── eda_cleaned_dataset.csv
│   └── pickles/
│       └── model.pkl
├── notebooks/
│   ├── 1_EDA.ipynb
│   └── 2_Model_Building_HPT.ipynb
├── Revenue_Insights_App.py  # Streamlit App with Chatbot + UI
├── dashboard.pbix            # Power BI report
└── README.md
```

## 🧠 Key Features
### ✅ Customer Churn Prediction
- EDA and feature engineering
- Hyperparameter-tuned ML models using Scikit-learn
- Binary classification with high accuracy

### 📊 Power BI Dashboard
- Churn by Contract, Tenure, and Services
- Revenue by Payment Method
- Interactive filters and slicers for executive insights

### 🗣️ Revenue Optimization Chatbot
- Powered by Langchain + Groq API (LLM)
- Supports natural language queries over the dataset
- In-browser chat interface inside Streamlit app

### 🌐 Full-Stack Deployment
- Stylish Streamlit app with HTML/CSS animated themes
- Sidebar navigation and dual-mode (predictor + chatbot)

## 🧰 Tech Stack
- **Python** (Pandas, Scikit-learn, Streamlit)
- **Power BI** (Data modeling + KPI dashboards)
- **Langchain** + **Groq API** (for chatbot)
- **HTML/CSS** (for advanced UI styling)
- **Pickle** (for model serialization)

## ▶️ Getting Started
1. Clone the repo:
```bash
git clone https://github.com/KinsunDasK/Customer_Retension_and_Revenue_Insights.git
cd Customer_Retension_and_Revenue_Insights
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file and add your Groq API key:
```bash
GROQ_API_KEY=your_api_key_here
```
4. Run the Streamlit app:
```bash
streamlit run Revenue_Insights_App.py
```

## 📸 Screenshots
| Customer Churn Predictor | LLM Revenue Chatbot |
|--------------------------|----------------------|
| ![](assets/predictor_ui.png) | ![](assets/chatbot_ui.png) |

## 📬 Connect
If you liked this project or have feedback, feel free to connect:
- GitHub: [KinsunDasK](https://github.com/KinsunDasK)
- LinkedIn: [Kinsun Das](https://www.linkedin.com/in/kinsundas)

---
**⭐ Star this repo** to support my work and follow for more end-to-end AI/ML projects!

> "Turning customer behavior into actionable insights with AI."
