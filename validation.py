def validate_health_data(data):
    # should return True if data is valid, else raises ValueError

    # Edge case: sleep can't be negative or above 24h
    if data['sleep_hours'] < 0 or data['sleep_hours'] > 24:
        return False
    # Edge case: mood score between 1 and 10
    if data['mood_score'] < 1 or data['mood_score'] > 10:
        return False
    # Edge case: exercise minutes can't be negative or above 1440 (24h)
    if data['exercise_minutes'] < 0 or data['exercise_minutes'] > 1440:
        return False
    # Edge case: water intake can't be negative or above 10L
    if data['water_intake_liters'] < 0 or data['water_intake_liters'] > 10:
        return False
    # Edge case: calories consumed can't be negative or above 10000
    if data['calories_consumed'] < 0 or data['calories_consumed'] > 10000:
        return False
    # Edge case: screen time can't be negative or above 24h
    if data['screen_time_hours'] < 0 or data['screen_time_hours'] > 24:
        return False
   
    return True
