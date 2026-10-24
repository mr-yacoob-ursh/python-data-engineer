candidate_id = int(input("Enter your ID : "))
name = input("Enter your name : ")
age = int(input("Enter your age : "))
degree = input("Enter your degree : ")
expected_salary = float(input("Enter your expected salary : "))
experience_years = int(input("Enter your years of experience : "))
monthly_salary = expected_salary / 12
is_fresher = experience_years == 0

print("========== CANDIDATE PROFILE ==========")
print(f"Candidate ID : {candidate_id}")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Degree : {degree}")
print(f"Expected monthly salary : ₹{monthly_salary}")
print(f"Expected annual income : ₹{expected_salary}")
print(f"Experience : {experience_years}")
print(f"Fresher : {is_fresher}")

