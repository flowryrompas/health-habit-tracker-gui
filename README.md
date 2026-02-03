# 🥗 Health Habits Tracker

This app is designed to allow users to log daily health metrics, including calorie intake, sleep duration, and mood. 
## Key Features
1. Daily Logging: Record sleep, exercise, mood, water intake, calorie intake, and screen time.
2. Visual Trends: Interactive charts to visualise correlations of habits with mood trends. 
3. Data validation: Real-time checking to ensure data integrity
4. Local Storage: All data is securely stored in a local SQLite database. 

## Technical Stack
- Frontend: Streamlit
- Database: SQLite3
- Data Analysis: Pandas
- Testing: Pytest (Unit & Integration)

## How to use
1. Run `pip install -r requirements.txt`
2. Run `streamlit run app.py`

## Testing
This project implements a two-tier testing suite:
* `test_validation.py`: Unit Tests - to test the logic for data entry
* `test_database.py`: Integration Tests - to verify the SQL connection and data flow using temporary test databases

To run the tests: `pytest`

## Installation & Setup
1. Clone the repository:
`https://github.com/flowryrompas/health-habit-tracker-gui.git`
2. Create and activate a virtual environment:
```
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate
```
3. Install dependencies:
`pip install -r requirements.txt`
4. Run the application: 
`streamlit run app.py`

## Project Structure
``` text
├── app.py              # Main Streamlit UI and application flow
├── database.py         # SQL database connection and queries
├── validation.py       # Independent logic for data validation
├── tests/              # Automated test suite
└── requirements.txt    # Project dependencies
```
