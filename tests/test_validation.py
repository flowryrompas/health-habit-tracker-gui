from validation import validate_health_data

def test_valid_data():
    # Test with valid data
    sample = {
        'sleep_hours': 7.5,
        'mood_score': 8,
        'exercise_minutes': 45,
        'water_intake_liters': 2.5,
        'calories_consumed': 2200,
        'screen_time_hours': 5.0
    }
    assert validate_health_data(sample) is True # valid data should return True

def test_invalid_sleep():
    # Test with invalid sleep hours
    sample = {
        'sleep_hours': -3, # invalid
        'mood_score': 5,
        'exercise_minutes': 30,
        'water_intake_liters': 2.0,
        'calories_consumed': 2000,
        'screen_time_hours': 4.0
    }
    assert validate_health_data(sample) is False # should return False

def test_invalid_mood():
    # Test with invalid mood score
    sample = {
        'sleep_hours': 6,
        'mood_score': 15, # invalid
        'exercise_minutes': 30,
        'water_intake_liters': 2.0,
        'calories_consumed': 2000,
        'screen_time_hours': 4.0
    }
    assert validate_health_data(sample) is False # should return False

def test_invalid_exercise():
    # Test with invalid exercise minutes (out of range)
    sample = {
        'sleep_hours': 6,
        'mood_score': 5,
        'exercise_minutes': 2000, # invalid
        'water_intake_liters': 2.0,
        'calories_consumed': 2000,
        'screen_time_hours': 4.0
    }
    assert validate_health_data(sample) is False # should return False

def test_invalid_water_intake():
    # Test with invalid water intake 
    sample = {
        'sleep_hours': 6,
        'mood_score': 5,
        'exercise_minutes': 30,
        'water_intake_liters': -1.0, # invalid
        'calories_consumed': 2000,
        'screen_time_hours': 4.0
    }
    assert validate_health_data(sample) is False # should return False