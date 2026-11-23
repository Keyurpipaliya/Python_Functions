

def user_profile(username, Education, birthdate, gender, skills):
    profile = {
        "username": username,
        "Education": Education,
        "birthdate": birthdate,
        "gender": gender,
        "skills": skills,
    }
    for key, value in profile.items():
        print(f"{key}: {value}")
        
print("User details")
