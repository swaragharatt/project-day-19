import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

df = pd.read_csv(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\netflix_data.csv.zip")
for feature in ['director', 'cast', 'listed_in', 'description']:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return f"{row['director']} {row['cast']} {row['listed_in']} {row['description']}"

df['combined_features'] = df.apply(combine_features, axis=1)
vectorizer = CountVectorizer(stop_words='english')
count_matrix = vectorizer.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)

def recommend_movies(genre_filter=None, lang_filter=None, num_recommendations=10):
    recommendations = []
    for idx, row in df.iterrows():
        if genre_filter and genre_filter.lower() not in row['listed_in'].lower():
            continue
        if lang_filter and lang_filter.lower() not in str(row['country']).lower():
            continue
        recommendations.append(row['title'])
        if len(recommendations) >= num_recommendations:
            break
    return recommendations if recommendations else ["No recommendations match the filters."]

root = tk.Tk()
root.title("Netflix Recommendation System")
root.geometry("700x600")

# Define simple font for all widgets except logo
simple_font = ("Arial", 13)

bg_image_path = r"C:\Users\USER\OneDrive\New folder\New folder\netflx\netflix-library-photo-scaled.jpg"
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((700, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

style = ttk.Style()
style.configure("TLabel", background="#141414", foreground="white", font=simple_font)
style.configure("TButton", background="#E50914", foreground="white", font=("Arial", 13, "bold"))
style.configure("TCombobox", font=simple_font)

logo_space = tk.Label(root, text="NETFLIX", font=("Impact", 34, "bold"), fg="#E50914", bg="#141414")
logo_space.pack(pady=20)

genre_label = ttk.Label(root, text="Select Genre:", font=simple_font)
genre_label.pack(pady=8)
genres = sorted(set(g for sub in df['listed_in'].dropna().str.split(",") for g in sub))
genre_combo = ttk.Combobox(root, values=[""] + genres, width=50, font=simple_font)
genre_combo.pack(pady=6)

lang_label = ttk.Label(root, text="Select Language (Country):", font=simple_font)
lang_label.pack(pady=8)
langs = sorted(set(df['country'].dropna().str.split(",").sum()))
lang_combo = ttk.Combobox(root, values=[""] + langs, width=50, font=simple_font)
lang_combo.pack(pady=6)

def show_recommendations():
    genre_filter = genre_combo.get().strip()
    lang_filter = lang_combo.get().strip()
    recommendations = recommend_movies(genre_filter, lang_filter, num_recommendations=10)
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "Recommendations:\n\n")
    for rec in recommendations:
        result_box.insert(tk.END, f"• {rec}\n")

recommend_btn = tk.Button(root, text="Recommend", command=show_recommendations,
                          bg="#E50914", fg="white", font=("Arial", 13, "bold"), relief="flat")
recommend_btn.pack(pady=18)

result_box = tk.Text(root, wrap="word", height=15, width=72, bg="#1c1c1c", fg="white",
                     font=simple_font, relief="flat", spacing3=5)
result_box.pack(pady=12)

scrollbar = ttk.Scrollbar(root, command=result_box.yview)
scrollbar.pack(side="right", fill="y")
result_box.config(yscrollcommand=scrollbar.set)

root.mainloop()
