# Euros 2024 Shot Map

## 📌 Project Overview
This project is a **Streamlit-based web app** that visualizes **shot maps** for the **UEFA Euros 2024** tournament. It allows users to filter shots by **team** and **player** and displays shot locations on a half-pitch using **mplsoccer**.

## 🚀 Features
- 📊 **Filter shots by team and player**
- ⚽ **Visualize all shots taken** on a half-pitch
- 🎯 **Highlight goals** (green) vs. **missed shots** (red)
- 🔄 **Show shot trajectories** (if available)
- 📌 **Interactive UI** using Streamlit

## 🛠️ Tech Stack
- **Python** (Pandas, JSON, Matplotlib, Streamlit)
- **mplsoccer** (for plotting the pitch)
- **Streamlit** (for the web interface)

## 📂 Dataset
The app reads data from a CSV file (`euros_2024_shot_map.csv`), which contains:
- `team` - Team name
- `player` - Player name
- `type` - Event type (filtered to "Shot")
- `location` - Shot start location (as JSON array)
- `shot_outcome` - Whether the shot was a **Goal** or **Missed**
- `shot_end_location` (Optional) - Where the shot ended (for trajectory plotting)

## 🎮 How to Run
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/euros-2024-shot-map.git
   cd euros-2024-shot-map
   ```
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Streamlit App**:
   ```sh
   streamlit run app.py
   ```

## 📸 Screenshot
![Shot Map Screenshot](screenshot.png)

## 📌 Future Enhancements
- 🔥 Add xG (Expected Goals) visualization
- 📍 Allow filtering by match date
- 📊 Add shot statistics (total shots, conversion rate, etc.)

## 🤝 Contributing
Feel free to **fork** this repo and submit a **pull request** if you have improvements!

## 🏆 Author
**Ammar Shahid**

---
⭐ *If you like this project, give it a star!* ⭐

