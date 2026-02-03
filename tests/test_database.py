import pytest
import os
from database import initialize_db, add_entry_to_db, fetch_all_data

@pytest.fixture
def temporary_db():
    """Fixture to create and destroy a temporary database for testing."""
    db_name = "test_temp.db"
    initialize_db(db_name) # create the tables in the new temp db
    yield db_name # provide the temp db name to the tests
    if os.path.exists(db_name): # if the temp db file exists
        os.remove(db_name) # clean up the temp db file after tests

def test_db_integration(temporary_db):
    # 1. Create a sample entry
    sample_entry = {
        'date': '2024-01-01',
        'sleep_hours': 7.0,
        'mood_score': 8,
        'exercise_minutes': 30,
        'water_intake_liters': 2.0,
        'calories_consumed': 2200,
        'screen_time_hours': 5.0
    }
    # 2. Save/add entry
    add_entry_to_db(sample_entry, db_name=temporary_db)

    # 3. Fetch all data and check it 
    df = fetch_all_data(db_name=temporary_db)
    assert not df.empty, "Database should contain at least one entry."
    assert len(df) == 1, "Database should contain exactly one entry."
    # Check that the data matches
    assert df.iloc[0]['date'] == sample_entry['date'], "Date should match the inserted entry."
    assert df.iloc[0]['mood_score'] == 8, "Mood score should match the inserted entry."
