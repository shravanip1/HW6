def calculate_effort_hours(num_sprint_days, team_member_details):
    total_team_effort_hours = 0
    effort_hours_per_person = []

    for member in team_member_details:
        available_days = num_sprint_days - member['days_off'] - member['days_in_ceremonies']
        average_hours_per_day = sum(member['hours_per_day']) / 2
        member_effort_hours = available_days * average_hours_per_day
        effort_hours_per_person.append(member_effort_hours)
        total_team_effort_hours += member_effort_hours

    return effort_hours_per_person, total_team_effort_hours
