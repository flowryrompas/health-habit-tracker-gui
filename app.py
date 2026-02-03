import streamlit as st
from database import add_entry_to_db, fetch_all_data, clear_data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# set the page title
st.set_page_config(page_title="Personal Health Tracker and Analytics", layout="wide")
st.title("📊 Personal Health Tracker Dashboard")

# create a sidebar for the data entry section
with st.sidebar:
    st.header("Add New Entry")
    input_date = st.date_input("Date")
    sleep = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.5)
    mood = st.select_slider("Mood Score", options=range(1,11), value=5) # value=5 means the default selected value is 5
    exercise = st.number_input("Exercise Minutes", min_value=0, max_value=300, step=5) 
    water = st.number_input("Water Intake (Liters)", min_value=0.0, max_value=10.0, step=0.1)
    calories = st.number_input("Calories Consumed", min_value=0, max_value=10000, step=50)
    screen = st.number_input("Screen Time (Hours)", min_value=0.0, max_value=24.0, step=0.5)

    if st.button("Add Entry to Database"): # if the button is clicked
        new_entry = {
            'date': input_date.strftime("%Y-%m-%d"), # convert date to string because SQL stores dates as strings 
            'sleep_hours': sleep,
            'mood_score': mood,
            'exercise_minutes': exercise,
            'water_intake_liters': water,
            'calories_consumed': calories,
            'screen_time_hours': screen
        }
        add_entry_to_db(new_entry)
        st.success(f"Entry for {input_date} added to database!") # show a success message


if st.sidebar.button("Clear All Data"):
    clear_data()
    st.success("Data Cleared!")
    st.rerun() # forces app to restart 


df = fetch_all_data()  # Fetch data from database

if df.empty:
    st.warning("No data available in the database. Please add entries using the sidebar.")
else:
    # statistics summary at the top
    c1, c2, c3, c4 = st.columns(4)
    st.subheader("Key Metrics Overview")
    c1.metric("Avg Sleep Hours", f"{df['sleep_hours'].mean():.2f}")
    c2.metric("Avg Mood Score", f"{df['mood_score'].mean():.2f}")
    c3.metric("Avg Exercise Minutes", f"{df['exercise_minutes'].mean():.2f}")
    c4.metric("Total Logs", len(df))

    st.divider() # horizontal line to separate sections

    # grid of graphs (2x2)
    df['date'] = pd.to_datetime(df['date']).dt.date  # ensure date column is datetime because we previously stored it as string for SQL
    # ^ only keep the date part (no time) 
    df = df.sort_values('date')  # sort by date ascending for better time series plots
    r1c1, r1c2 = st.columns(2) # row 1 
    r2c1, r2c2 = st.columns(2) # row 2

    with r1c1:
        st.subheader("Sleep Hours Over Time")
        st.line_chart(data=df, x='date', y='sleep_hours')

    with r1c2:
        st.subheader("Exercise Minutes Over Time")
        st.line_chart(data=df, x='date', y='exercise_minutes')

    with r2c1:
        st.subheader("Sleep vs Mood Correlation")
        fig1, ax1 = plt.subplots()
        sns.regplot(data=df, x='sleep_hours', y='mood_score', ax=ax1)
        st.pyplot(fig1)

    with r2c2:
        st.subheader("Exercise vs Mood Correlation")
        fig2, ax2 = plt.subplots()
        sns.regplot(data=df, x='exercise_minutes', y='mood_score', ax=ax2) #ax=ax2 to specify which subplot to use
        st.pyplot(fig2)

    st.divider()

    # detailed data table at the bottom
    st.subheader("Detailed Health Logs")
    with st.expander("View All Entries"):
        st.write("Below is the complete table of your health logs:")
        st.dataframe(
            df.sort_values(by='date', ascending=False).reset_index(drop=True), # sort by date descending for latest first and drop the old index prior to sorting
            width='stretch', # make the table use the full width of the container
            hide_index=True # hide the index column
        )


