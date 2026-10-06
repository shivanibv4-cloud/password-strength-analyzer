import re

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search("[a-z]", password):
    score += 1

if re.search("[A-Z]", password):
    score += 1

if re.search("[0-9]", password):
    score += 1

if re.search("[!@#$%^&*]", password):
    score += 1

print("\nPassword Analysis:")

if len(password) < 8:
    print("❌ Password should have at least 8 characters.")
else:
    print("✅ Good password length.")

if score <= 2:
    print("🔴 Strength: Weak")
    print("Suggestion: Add uppercase letters, numbers and special characters.")

elif score <= 4:
    print("🟡 Strength: Medium")
    print("Suggestion: Make the password more complex.")

else:
    print("🟢 Strength: Strong")