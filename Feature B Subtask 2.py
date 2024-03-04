def validate_member_details(team_member_details):
    validated_details = []
    for member in team_member_details:
        try:
            hours_per_day = tuple(map(int, member['hours_range'].split()))
            if len(hours_per_day) != 2 or any(hour < 0 for hour in hours_per_day):
                raise ValueError("Hours per day must be a range with two non-negative integers.")
        except ValueError as e:
            raise ValueError(f"Invalid input for hours per day: {e}")
        validated_details.append({
            'days_off': member['days_off'],
            'days_in_ceremonies': member['days_in_ceremonies'],
            'hours_per_day': hours_per_day
        })
    return validated_details
