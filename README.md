# 🏅 Olympic Data Analysis Dashboard

An interactive web application built using **Streamlit** that visualizes Olympic Games data. It allows users to explore medal tallies, country-wise performance, athlete statistics, and overall historical trends in an engaging way.

---

## 📊 Features

- 📈 **Medal Tally**  
  ##### Track the number of **gold, silver, and bronze medals** won by countries.
  ![image](https://github.com/user-attachments/assets/7094791e-bfd3-4a18-ab30-275b928166a5)
  
  ##### Filter by **year** or **country** to view performance in specific Olympic editions.
  ![image](https://github.com/user-attachments/assets/4f01c52e-d480-4426-89d6-f6c39b43671b)
  
 ##### Identify which countries dominated particular years or events.
  ![image](https://github.com/user-attachments/assets/1e3f7919-5298-47a9-ba17-f5277356e581)




- 🌍 **Overall Analysis**  
  Visualize the **growth of the Olympics** over time in terms of:  
  → Number of athletes  
  → Participating countries  
  → Sports and events  
  Understand how global events shaped Olympic history.

- 🇮🇳 **Country-wise Performance**  
  Explore any country’s Olympic journey:  
  → Medal trends across years  
  → Most successful sports  
  → Top-performing athletes  
  Especially useful to analyze progress of countries like India, USA, China, etc.

- 🧑‍🤝‍🧑 **Athlete-wise Analysis**  
  Discover trends across individual athletes:  
  → Top medal winners  
  → Gold medals by sport  
  → Male vs female participation  
  → Age distributions by event/sport

- 📌 **Interactive Visualizations**  
  Built with **Plotly**, **Matplotlib**, and **Seaborn**:  
  → Zoomable, filterable, and interactive charts  
  → Hover to view insights  
  → Rich graphs to make data exploration intuitive and fun

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: Pandas
- **Visualizations**: Plotly, Seaborn, Matplotlib
- **Languages**: Python
- **Data Source**:
  - `athlete_events.csv`
  - `noc_regions.csv`

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/manuraj23/Olympic-Data-Analysis.git
cd olympics-dashboard
```

### 2.Install Dependencies
```bash
pip install -r requirements.txt
```
### 3.Add Dataset
 Place the following files inside the project directory:

 - `athlete_events.csv`

 - `noc_regions.csv`

### 4. Run the Application
 ```bash
 streamlit run app.py
```

It will automatically open a new tab in your browser. If it doesn’t, open http://localhost:8501 manually.


## 📁 Project Structure
```bash
olympics-dashboard/
│
├── app.py                  
├── helper.py              
├── preprocessor.py        
├── requirements.txt      
├── athlete_events.csv      
├── noc_regions.csv        
└── README.md             
```
## 🤝 Contributing
#### Contributions are welcome! Feel free to open issues or submit a pull request.
```bash
# Fork the repository
# Create a new branch
git checkout -b feature-branch

# Make your changes and commit
git commit -m "Add some feature"

# Push to your fork
git push origin feature-branch

# Open a Pull Request on GitHub
```

## 🧾 License

This project is licensed under the **MIT License**.


## 📬 Contact

**Made with ❤️ by Manu Raj**

- 🔗 [LinkedIn](https://www.linkedin.com/in/manu-raj-dev)  
- 📧 Email: [manuraj082004@gmail.com](mailto:manuraj082004@gmail.com)  
- 💻 [GitHub](https://github.com/manuraj23)


