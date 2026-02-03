import numpy as np
import pandas as pd
from database import add_entry_to_db
from datetime import datetime, timedelta

def generate_sample_data(num_days=30):
    print(f"Generating {num_days} days of sample health data...")
    # start date is today minus num_days (30 days ago)
    start_date = datetime.now() - timedelta(days=num_days) # timedelta makes num_days into a time duration
    
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        current_date = current_date.strftime("%Y-%m-%d") # convert to string format because we're feeding data to SQL database

        # generate realistic patterns
        
        # 1. sleep: average around 7 hours, with some variation
        sleep = round(np.random.normal(7, 1.2), 1) # mean=7, std=1.2, rounded to 1 decimal
        sleep = max(4, min(10, sleep)) # clamp between 4 and 10 hours

        # 2. mood: correlated with sleep (better sleep, better mood)
        life_factor = np.random.randint(-2, 3) # random life events affecting mood
        # np.random is to access the module random, and randint is the actual function 
        mood = int(np.clip((sleep * 0.8) + life_factor, 1, 10)) # mood between 1 and 10
        # np.clip(value, min, max) is like min/max but for arrays (physical boundary)

        # 3. exercise: random but with a slight positive correlation to mood
        exercise = 0 if np.random.rand() < 0.4 else int(np.random.randint(20,80) + (mood - 5)*2)
        # 40% chance of no exercise, otherwise random between 20-80 mins + mood influence 
        # rand() generates a float between 0 and 1 

        # 4. water intake: average around 2 liters, with some variation 
        water = round(np.random.uniform(1.5, 3.5), 1) # uniform distribution between 1.5 and 3.5 liters; 1 decimal
        # 5. calories: average around 2000, with variation based on exercise
        calories = np.random.randint(1800, 2600) + (exercise // 10) * 35 # exercise divided by 10, times 35 calories
        screen = round(np.random.normal(6, 2), 1) # average 6 hours screen time, stddev 2 hours, 1 decimal
        screen = max(1, min(12, screen)) # clamp between 1 and 12 hours

        # create the dictionary to insert
        data_dict = {
            'date': current_date,
            'sleep_hours': sleep,
            'mood_score': mood,
            'exercise_minutes': exercise,
            'water_intake_liters': water,
            'calories_consumed': calories,
            'screen_time_hours': screen
        }
        add_entry_to_db(data_dict) # add to database

    print("✅ Sample data generation complete.")

if __name__ == "__main__":
    generate_sample_data(30)  # generate 30 days of sample data
        
    