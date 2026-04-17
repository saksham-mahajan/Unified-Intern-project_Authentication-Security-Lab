import hashlib
import time
import math
import re

print("\n=== Authentication Security Lab (Final Version) ===\n")

# ---------------- STEP 1: USER INPUT ----------------
username = input("Enter username: ")

# ---------------- STEP 2: STRONG PASSWORD CREATION ----------------
while True:
    password = input("Create a strong password: ")

    errors = []

    if len(password) < 10:
        errors.append("Min length 10 required")

    if not any(c.isupper() for c in password):
        errors.append("Add uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Add lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Add number")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Add special character")

    if username.lower() in password.lower():
        errors.append("Password should not contain username")

    common = ["1234567890", "password123", "admin123", "qwerty123"]
    if password.lower() in common:
        errors.append("Too common password")

    if len(errors) == 0:
        print("Strong Password Accepted ✔\n")
        break
    else:
        print("\nWeak Password ❌ Fix:")
        for e in errors:
            print("-", e)
        print()

# ---------------- HASHING ----------------
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# ---------------- STEP 3: LOGIN SIMULATION ----------------
print("\n=== Login System ===")

max_attempts = 3
attempts = 0
login_success = False

while attempts < max_attempts:
    login_user = input("Enter username: ")
    login_pass = input("Enter password: ")

    if login_user == username and hashlib.sha256(login_pass.encode()).hexdigest() == hashed_password:
        print("Login Successful ✔")
        login_success = True
        break
    else:
        attempts += 1
        print(f"Login Failed ❌ ({attempts}/{max_attempts})")

if not login_success:
    print("Account Locked 🔒 due to too many attempts")

# ---------------- STEP 4: LOAD WORDLIST ----------------
def load_wordlist():
    try:
        with open("worldlistp.txt", "r") as f:
            return [w.strip() for w in f.readlines()]
    except:
        print("worldlistp.txt not found!")
        return []

wordlist = load_wordlist()

# ---------------- STEP 5: BRUTE FORCE SIMULATION ----------------
print("\n=== Brute Force Simulation ===\n")

start_time = time.time()
cracked = False

for word in wordlist:
    print("Trying:", word)
    time.sleep(0.1)

    if hashlib.sha256(word.encode()).hexdigest() == hashed_password:
        end_time = time.time()
        print("\nPassword Cracked ✔:", word)
        print("Time Taken:", round(end_time - start_time, 4), "seconds")
        cracked = True
        break

if not cracked:
    end_time = time.time()
    print("\nPassword NOT cracked ❌")

# ---------------- STEP 6: PASSWORD STRENGTH ANALYSIS ----------------
print("\n=== Password Strength Analysis ===")

entropy = len(password) * math.log2(94)

if entropy < 40:
    strength = "WEAK"
elif entropy < 60:
    strength = "MEDIUM"
else:
    strength = "STRONG"

if strength == "WEAK":
    print("Strength: ███░░ (Weak)")
elif strength == "MEDIUM":
    print("Strength: █████░ (Medium)")
else:
    print("Strength: ██████ (Strong)")

print("Entropy:", round(entropy, 2))

# ---------------- STEP 7: REPORT GENERATION ----------------
print("\nGenerating Report...\n")

with open("report.txt", "w") as f:
    f.write("=== Security Report ===\n")
    f.write(f"Username: {username}\n")
    f.write(f"Password Strength: {strength}\n")
    f.write(f"Entropy: {round(entropy,2)}\n")
    f.write(f"Password Hash: {hashed_password}\n")

    if strength == "WEAK":
        f.write("Risk: HIGH\n")
    elif strength == "MEDIUM":
        f.write("Risk: MEDIUM\n")
    else:
        f.write("Risk: LOW\n")

    f.write(f"Login Attempts Used: {attempts}\n")
    f.write(f"Attack Time: {round(end_time - start_time,4)} sec\n")

print("Report generated ✔ (check report.txt)")
