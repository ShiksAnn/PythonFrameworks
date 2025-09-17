# PythonFrameworks
# Python-Frameworks

# 📊 CORD-19 Data Explorer

A beginner-friendly project analyzing the [CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) dataset.  
This project explores COVID-19 research publications metadata and provides an **interactive Streamlit web app** for visualization.  

---

## 🎯 Objectives
- Load and clean real-world datasets.  
- Explore publication patterns (by year, journal, source).  
- Create meaningful visualizations with **matplotlib/seaborn**.  
- Build an interactive web application with **Streamlit**.  

---

## 🛠️ Tools Used
- Python 3.7+  
- pandas (data cleaning & manipulation)  
- matplotlib & seaborn (visualizations)  
- streamlit (web app)  

Install everything with:  
```bash
pip install -r requirements.txt
📂 Project Structure
bash
Copy code
Frameworks_Assignment/
│
├── app.py               # Streamlit application
├── metadata.csv         # CORD-19 metadata (or sample file)
├── notebooks/           # Jupyter notebooks (exploration)
└── README.md            # Project documentation


📈 Data Insights
1. Publications by Year
Shows how research output grew over time.

2. Top Journals
Top 10 journals publishing COVID-19 research.

3. Word Cloud of Titles
Most frequent words appearing in paper titles.

4. Distribution by Source
Counts of papers by repository/source.

🚀 Running the App Locally
Clone this repository:

bash
Copy code
git clone https://github.com/ShiksAnn/PythonFrameworks.git
cd Frameworks_Assignment
Install dependencies:

bash
Copy code
Run the app:

bash
Copy code
streamlit run app.py
Then open http://localhost:8501 in your browser.

🌍 Optional: Deploy Online
You can deploy for free using Streamlit Cloud:

Push your repo to GitHub.

Log in to Streamlit Cloud → New app → select your repo.

Choose app.py as the main file.

Done ✅ — you’ll get a public link to share your app.


🤔 Reflection
Challenges: Handling missing data (many rows lacked publication dates/journals), reducing dataset size for testing.

Learnings: Improved skills in pandas cleaning, plotting, and basic Streamlit development.

Next steps: Add NLP analysis of abstracts, author collaboration networks, and deploy app online for public access.


✅ Deliverables:

Jupyter notebook / Python scripts for analysis

Visualizations (charts, word cloud, trends)

Interactive Streamlit application

links
Local URL: http://localhost:8501
Network URL: http://192.168.8.79:8501
