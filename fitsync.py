import streamlit as st
import os
from datetime import datetime
import random

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return "\n".join(str(workout) for workout in self.workouts) if self.workouts else "No workouts recorded yet."

    def save_data(self, filename):
        try:
            with open(filename, "w") as file:
                for workout in self.workouts:
                    file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")
            return "Data saved successfully!"
        except Exception as e:
            return f"Error saving data: {e}"

    def load_data(self, filename):
        try:
            if not os.path.exists(filename):
                return "File not found!"
            self.workouts.clear()
            with open(filename, "r") as file:
                for line in file:
                    date, exercise_type, duration, calories_burned = line.strip().split(",")
                    self.workouts.append(Workout(date, exercise_type, int(duration), int(calories_burned)))
            return "Data loaded successfully!"
        except Exception as e:
            return f"Error loading data: {e}"

# Add motivational quotes
MOTIVATIONAL_QUOTES = [
    "The only bad workout is the one that didn't happen. - Unknown",
    "No pain, no gain. - Jane Fonda",
    "Your body can stand almost anything. It's your mind you have to convince.",
    "The hard days are the best because that's when champions are made.",
    "Success isn't always about greatness. It's about consistency.",
]

def add_bg_and_styles():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                            url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?ixlib=rb-4.0.3");
            background-size: cover;
            background-attachment: fixed;
        }}
        
        .css-1d391kg {{
            background-color: rgba(28, 28, 28, 0.92) !important;
        }}
        
        .workout-card {{
            background-color: rgba(28, 28, 28, 0.95);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            border: 2px solid #FF5733;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }}
        
        .quote-card {{
            background: linear-gradient(135deg, rgba(255, 87, 51, 0.9), rgba(255, 195, 0, 0.9));
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
            color: white;
            font-style: italic;
            font-weight: 500;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        }}
        
        .stTextInput>div>div>input,
        .stNumberInput>div>div>input,
        .stDateInput>div>div>input {{
            background-color: rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 5px !important;
            border: 1px solid #FF5733 !important;
            font-weight: 500 !important;
        }}

        .stSelectbox>div>div>div {{
            background-color: rgba(28, 28, 28, 0.95) !important;
            color: white !important;
            border: 1px solid #FF5733 !important;
        }}
        
        /* Improve text contrast */
        .stMarkdown, .stText {{
            color: white !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }}
        
        h1, h2, h3 {{
            color: #FF5733 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            font-weight: 600 !important;
        }}

        /* Style info/success/error messages */
        .stSuccess, .stInfo, .stWarning, .stError {{
            text-shadow: none !important;
            padding: 15px !important;
            border-radius: 10px !important;
            font-weight: 500 !important;
        }}

        /* Labels and text */
        label, .stMarkdown p {{
            color: #FFFFFF !important;
            font-weight: 500 !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }}

        /* Button improvements */
        .stButton>button {{
            background-color: #2ECC71 !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 12px 24px !important;
            font-weight: 600 !important;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3) !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2) !important;
        }}
        
        .stButton>button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important;
            background-color: #27AE60 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Update the main app code
def main():
    add_bg_and_styles()
    st.title("🏋️‍♂️ Workout Tracker")

    # Sidebar with enhanced styling
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; color: #FF5733;'>👤 User Profile</h2>", unsafe_allow_html=True)
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, step=1)
        weight = st.number_input("Weight (kg)", min_value=1, step=1)
        if st.button("Create Profile"):
            st.session_state.user = User(name, age, weight)
            st.success(f"Welcome aboard, {name}! 🎉")
        
        # Add motivational quote
        st.markdown("---")
        quote = random.choice(MOTIVATIONAL_QUOTES)
        st.markdown(f"""
            <div class='quote-card'>
                ✨ {quote}
            </div>
        """, unsafe_allow_html=True)

    # Main content
    st.markdown("<div class='workout-card'>", unsafe_allow_html=True)
    st.subheader("📝 Add Workout")
    date = st.date_input("Date", datetime.today())
    exercise_type = st.selectbox("Exercise Type", 
                               ["Weight Training", "Cardio", "HIIT", "Yoga", "Swimming", "Running", "Cycling", "Other"])
    duration = st.number_input("Duration (minutes)", min_value=1, step=5)
    calories_burned = st.number_input("Calories Burned", min_value=1, step=10)
    
    if st.button("Add Workout 💪"):
        if st.session_state.user:
            workout = Workout(date.strftime("%Y-%m-%d"), exercise_type, duration, calories_burned)
            st.session_state.user.add_workout(workout)
            st.success("Great job! Workout added successfully! 🎯")
        else:
            st.error("Please create your profile first! 🚫")
    st.markdown("</div>", unsafe_allow_html=True)

    # View Workouts Section
    st.markdown("<div class='workout-card'>", unsafe_allow_html=True)
    st.subheader("📊 Workout History")
    if st.button("Show My Workouts 📈"):
        if st.session_state.user:
            workouts = st.session_state.user.view_workouts()
            if workouts != "No workouts recorded yet.":
                for workout in workouts.split("\n"):
                    st.info(workout)
            else:
                st.warning("No workouts recorded yet. Time to get moving! 💪")
        else:
            st.error("Please create your profile first! 🚫")
    st.markdown("</div>", unsafe_allow_html=True)

    # Save/Load Section
    st.markdown("<div class='workout-card'>", unsafe_allow_html=True)
    st.subheader("💾 Save/Load Progress")
    filename = st.text_input("Filename (e.g., my_workouts.txt)")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save Progress 📥"):
            if st.session_state.user and filename:
                st.success(st.session_state.user.save_data(filename))
            else:
                st.error("Please create a profile and provide a filename! 🚫")
    with col2:
        if st.button("Load Progress 📤"):
            if st.session_state.user and filename:
                st.success(st.session_state.user.load_data(filename))
            else:
                st.error("Please create a profile and provide a filename! 🚫")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    if "user" not in st.session_state:
        st.session_state.user = None
    main()
