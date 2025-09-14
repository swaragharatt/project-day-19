# project-day-19
# Netflix Recommendation System

A **Python desktop app** that provides personalized Netflix movie recommendations based on **genre and language filters**.  
Built with a modern dark theme and interactive GUI, it makes exploring Netflix content **simple and intuitive**.  

---

## Features  

-  Recommend movies based on selected **genre** and **language (country)**  
-  Top 10 recommendations displayed in a **scrollable text box**  
-  Interactive **dropdown menus** for genres and languages  
-  Sleek modern dark-themed GUI inspired by Netflix interface  
-  Uses **cosine similarity** for content-based recommendations  
-  Lightweight and beginner-friendly  

---

## Technologies Used  

- **Python 3** – Core programming language  
- **pandas** – Data handling and preprocessing  
- **scikit-learn** – CountVectorizer & cosine similarity  
- **tkinter** – GUI framework  
- **Pillow (PIL)** – Image handling for background and logos  

---

## Project Structure  

netflix-recommender/  
│── netflix_recommender.py          # Main Python script  
│── netflix_data.csv.zip            # Dataset  
│── netflix-library-photo-scaled.jpg  # Background image  
│── README.md                       # Documentation  

---

## How to Run  

1. Clone the repository.  
2. Install dependencies:  
   ```bash
   pip install pandas scikit-learn pillow
Ensure the dataset and background image paths are correct in the script.

Run the script:

bash
Copy code
python netflix_recommender.py
Select a genre and language, then click Recommend to view top 10 recommendations.

Example Output
Genre Filter: Comedy

Language Filter: United States

vbnet
Copy code
Recommendations:

• The Office
• Friends
• Brooklyn Nine-Nine
• Parks and Recreation
• Arrested Development
• Schitt's Creek
• New Girl
• How I Met Your Mother
• The Good Place
• Community

## Output image

<img width="856" height="736" alt="image" src="https://github.com/user-attachments/assets/adf2f258-81ba-432d-b879-a3db7c5691ac" />

Author
Swara Gharat
