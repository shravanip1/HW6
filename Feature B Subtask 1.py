def collect_sprint_days():
    return int(input("Enter the number of Sprint Days: "))

def collect_team_member_details(num_members):
    team_member_details = []
    for i in range(num_members):
        print(f"Enter details for team member {i + 1}:")
        days_off = int(input("Number of days off: "))
        days_in_ceremonies = int(input("Number of days committed to Sprint ceremonies: "))
        hours_range = input("Number of Hours/Day available as a range (e.g., 6 8): ")
        team_member_details.append({
            'days_off': days_off,
            'days_in_ceremonies': days_in_ceremonies,
            'hours_range': hours_range
        })
    return team_member_details

def collect_team_members_count():
    return int(input("Enter the number of team members: "))
