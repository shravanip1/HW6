def get_team_member_details(num_members):
    team_member_details = []
    for i in range(num_members):
        print(f"Enter details for team member {i + 1}:")
        days_off = int(input("Number of days off: "))
        days_in_ceremonies = int(input("Number of days committed to Sprint ceremonies: "))
        hours_per_day = tuple(map(int, input("Number of Hours/Day available as a range (e.g., 6 8): ").split()))
        team_member_details.append({'days_off': days_off, 'days_in_ceremonies': days_in_ceremonies, 'hours_per_day': hours_per_day})
    return team_member_details
