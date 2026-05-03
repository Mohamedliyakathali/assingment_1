job_data = {
    "Job_ID": [1, 2, 3, 4, 5],
    "Role": ["Data Analyst", "Data Scientist", "Business Analyst", "Data Engineer", "ML Engineer"],
    "Company": ["ABC Corp", "XyZ Ltd", "DataWorks", "InfraTech", "AI Labs"],
    "Skills": [
        "Excel SQL Python",
        "Python ML Statistics",
        "Excel SQL PowerBI",
        "Python SQL Spark",
        "Python ML DeepLearning"
    ]
}

print(job_data)


# =========================
# 1) Print job postings
# =========================
print("\n--- Job Listings ---")
for i in range(len(job_data["Job_ID"])):
    print(f"ID: {job_data['Job_ID'][i]} | Role: {job_data['Role'][i]} | Company: {job_data['Company'][i]} | Skills: {job_data['Skills'][i]}")


# =========================
# 2) Add new job postings
# =========================
n = int(input("\nHow many job postings do you want to add? "))
current_max_id = max(job_data["Job_ID"])

for i in range(n):
    print(f"\nEnter details for Job {i+1}")
    role = input("Enter role: ")
    company = input("Enter company: ")
    skills = input("Enter skills (space/comma separated): ")

    skills = skills.replace(",", " ")

    current_max_id += 1

    job_data["Job_ID"].append(current_max_id)
    job_data["Role"].append(role)
    job_data["Company"].append(company)
    job_data["Skills"].append(skills)


# =========================
# 3) Clean & Normalize Skills
# =========================
def clean_skills(skill_text):
    skill_text = skill_text.lower()
    skill_text = skill_text.replace(",", " ")
    skill_text = " ".join(skill_text.split())   # remove extra spaces
    return skill_text

# Apply cleaning
job_data["Skills"] = [clean_skills(s) for s in job_data["Skills"]]


# =========================
# 4) Skill Extraction & Frequency
# =========================
all_skills = []

for skill_string in job_data["Skills"]:
    tokens = skill_string.split()
    all_skills.extend(tokens)

# Count frequency
skill_count = {}
for skill in all_skills:
    skill_count[skill] = skill_count.get(skill, 0) + 1

# Top 5 skills
sorted_skills = sorted(skill_count.items(), key=lambda x: x[1], reverse=True)

print("\nTop skills by frequency:")
for skill, count in sorted_skills[:5]:
    print(f"{skill}: {count}")


# =========================
# 5) Basic Statistics
# =========================
total_jobs = len(job_data["Job_ID"])
unique_skills = len(set(all_skills))

python_jobs = []
for i in range(len(job_data["Job_ID"])):
    if "python" in job_data["Skills"][i]:
        python_jobs.append(job_data["Role"][i])

print("\n--- Statistics ---")
print("Total Jobs:", total_jobs)
print("Unique skills:", unique_skills)
print("Jobs mentioning Python:", python_jobs)


# =========================
# 6) Skill Search Function
# =========================
def find_jobs_by_skill(skill_query):
    skill_query = skill_query.lower().strip()
    results = []

    for i in range(len(job_data["Job_ID"])):
        if skill_query in job_data["Skills"][i]:
            results.append((
                job_data["Job_ID"][i],
                job_data["Role"][i],
                job_data["Company"][i]
            ))

    return results

# Example usage
print("\nSearch Results for 'sql':")
print(find_jobs_by_skill("sql"))


# =========================
# 7) Lambda Filtering
# =========================
common_roles = [
    job_data["Role"][i]
    for i in range(len(job_data["Job_ID"]))
    if any(skill_count.get(skill, 0) >= 2 for skill in job_data["Skills"][i].split())
]

print("\nRoles with at least one common skill:", common_roles)


# =========================
# 8) Unique Skill Set
# =========================
unique_skill_list = sorted(set(all_skills))

print("\nUnique skills:")
print(unique_skill_list)


# =========================
# 9) Save to Files
# =========================
try:
    # Save CSV
    with open("job_skills.csv", "w") as f:
        f.write("Job_ID,Role,Company,Skills\n")
        for i in range(len(job_data["Job_ID"])):
            f.write(f"{job_data['Job_ID'][i]},{job_data['Role'][i]},{job_data['Company'][i]},{job_data['Skills'][i]}\n")

    # Save top skills
    with open("top_skills.txt", "w") as f:
        for skill, count in sorted_skills[:5]:
            f.write(f"{skill}: {count}\n")

except Exception as e:
    print("Error while writing file:", e)

else:
    print("\nFiles saved successfully!")

finally:
    print("File operation completed.")