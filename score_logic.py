def get_badge(score):
    if score >=200:
        return "Gold 🏅"
    elif score >= 100:
        return "Silver 🥈"
    else:
        return "Bronze 🥉"
    

# Check result
my_score = 250
print(f"Your badge is: {get_badge(my_score)}")
