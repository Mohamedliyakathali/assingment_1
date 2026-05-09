# =========================
# SaaS Customer Data Project
# =========================

# Task 0 – Dataset

saas_data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107],
    "name": ["Rahul Sharma", "Meena Nair", None, "A. Kumar", "David", "Priya", "Rahul Sharma"],
    "signup_date": ["2023-01-10", "2023/02/15", "03-01-2023", "15-04-2023", "2023-05-10",
                    "20230520", "2023-01-10"],
    "plan": ["Pro", "Basic", "Pro", "Enterprise", "Pro", "", "Pro"],
    "monthly_fee": ["49.99", "19.99", "forty-nine", "99.99", "49.99", "49.99", "49.99"],
    "usage_hours": ["120", "45", "88", None, "NULL", "200", "120"]
}

print("Original Dataset")
print(saas_data)

# ======================================================
# Task 1 – Display the Dataset Using a For Loop
# ======================================================

print("\n================ Customer Records ================\n")

for i in range(len(saas_data["customer_id"])):
    print(
        f"ID: {saas_data['customer_id'][i]} | "
        f"Name: {saas_data['name'][i]} | "
        f"Signup Date: {saas_data['signup_date'][i]} | "
        f"Plan: {saas_data['plan'][i]} | "
        f"Monthly Fee: {saas_data['monthly_fee'][i]} | "
        f"Usage Hours: {saas_data['usage_hours'][i]}"
    )

# ======================================================
# Task 2 – Add New Customer Records
# ======================================================

num_customers = int(input("\nHow many customers do you want to add? "))

max_id = max(saas_data["customer_id"])

for i in range(num_customers):

    print(f"\nEnter details for Customer {i+1}")

    name = input("Enter name: ")
    signup_date = input("Enter signup date: ")
    plan = input("Enter plan: ")
    monthly_fee = input("Enter monthly fee: ")
    usage_hours = input("Enter usage hours: ")

    max_id += 1

    saas_data["customer_id"].append(max_id)
    saas_data["name"].append(name)
    saas_data["signup_date"].append(signup_date)
    saas_data["plan"].append(plan)
    saas_data["monthly_fee"].append(monthly_fee)
    saas_data["usage_hours"].append(usage_hours)

print("\nUpdated Dataset")
print(saas_data)

# ======================================================
# Task 3 – Create SaaS Customer Class (OOP)
# ======================================================

class SaaSCustomer:

    def __init__(self, customer_id, name, signup_date,
                 plan, monthly_fee, usage_hours):

        self.customer_id = customer_id
        self.name = name
        self.signup_date = signup_date
        self.plan = plan
        self.monthly_fee = monthly_fee
        self.usage_hours = usage_hours

    def validate_data(self):

        # Handle missing name
        if self.name is None or self.name == "":
            self.name = "Unknown Customer"

        # Standardize plan names
        if self.plan is None or self.plan.strip() == "":
            self.plan = "Unknown"
        else:
            self.plan = self.plan.title()

        # Convert monthly_fee to float
        try:
            self.monthly_fee = float(self.monthly_fee)
        except:
            self.monthly_fee = None

        # Convert usage_hours to int
        try:
            if self.usage_hours == "NULL" or self.usage_hours is None:
                self.usage_hours = 0
            else:
                self.usage_hours = int(self.usage_hours)

        except:
            self.usage_hours = 0

    def display_customer(self):

        print(f"Customer Name: {self.name}")


# Example object creation
customer1 = SaaSCustomer(
    101,
    "Rahul Sharma",
    "2023-01-10",
    "Pro",
    "49.99",
    "120"
)

customer1.validate_data()
customer1.display_customer()

# ======================================================
# Task 4 – Data Cleaning Pipeline
# ======================================================

from datetime import datetime

# ------------------------------------------------------
# Function 1 – Handle Missing Values
# ------------------------------------------------------

def handle_missing_values(data):

    for i in range(len(data["customer_id"])):

        # Missing name
        if data["name"][i] is None or data["name"][i] == "":
            data["name"][i] = "Unknown Customer"

        # Missing usage hours
        if data["usage_hours"][i] == "NULL" or data["usage_hours"][i] is None:
            data["usage_hours"][i] = 0

        # Invalid monthly fee
        try:
            data["monthly_fee"][i] = float(data["monthly_fee"][i])
        except:
            data["monthly_fee"][i] = None

    return data


# ------------------------------------------------------
# Function 2 – Remove Duplicate Records
# ------------------------------------------------------

def remove_duplicates(data):

    unique_ids = set()

    cleaned_data = {
        "customer_id": [],
        "name": [],
        "signup_date": [],
        "plan": [],
        "monthly_fee": [],
        "usage_hours": []
    }

    for i in range(len(data["customer_id"])):

        customer_id = data["customer_id"][i]

        if customer_id not in unique_ids:

            unique_ids.add(customer_id)

            cleaned_data["customer_id"].append(data["customer_id"][i])
            cleaned_data["name"].append(data["name"][i])
            cleaned_data["signup_date"].append(data["signup_date"][i])
            cleaned_data["plan"].append(data["plan"][i])
            cleaned_data["monthly_fee"].append(data["monthly_fee"][i])
            cleaned_data["usage_hours"].append(data["usage_hours"][i])

    return cleaned_data


# ------------------------------------------------------
# Function 3 – Standardize Date Formats
# ------------------------------------------------------

def standardize_dates(data):

    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%Y%m%d"
    ]

    for i in range(len(data["signup_date"])):

        date_str = data["signup_date"][i]

        for fmt in formats:

            try:
                parsed_date = datetime.strptime(date_str, fmt)

                data["signup_date"][i] = parsed_date.strftime("%Y-%m-%d")

                break

            except:
                pass

    return data


# ------------------------------------------------------
# Function 4 – Standardize Plan Names
# ------------------------------------------------------

def standardize_plan_names(data):

    for i in range(len(data["plan"])):

        if data["plan"][i] == "" or data["plan"][i] is None:
            data["plan"][i] = "Unknown"

        else:
            data["plan"][i] = data["plan"][i].title()

    return data


# ------------------------------------------------------
# Apply Cleaning Functions
# ------------------------------------------------------

saas_data = handle_missing_values(saas_data)

saas_data = remove_duplicates(saas_data)

saas_data = standardize_dates(saas_data)

saas_data = standardize_plan_names(saas_data)

# Convert usage_hours to integers

for i in range(len(saas_data["usage_hours"])):

    try:
        saas_data["usage_hours"][i] = int(saas_data["usage_hours"][i])
    except:
        saas_data["usage_hours"][i] = 0

print("\n================ Cleaned Dataset ================\n")

for i in range(len(saas_data["customer_id"])):

    print(
        f"ID: {saas_data['customer_id'][i]} | "
        f"Name: {saas_data['name'][i]} | "
        f"Signup Date: {saas_data['signup_date'][i]} | "
        f"Plan: {saas_data['plan'][i]} | "
        f"Monthly Fee: {saas_data['monthly_fee'][i]} | "
        f"Usage Hours: {saas_data['usage_hours'][i]}"
    )

# ======================================================
# Task 5 – Summary Statistics and Insights
# ======================================================

total_customers = len(saas_data["customer_id"])

# Average monthly fee

valid_fees = []

for fee in saas_data["monthly_fee"]:

    if fee is not None:
        valid_fees.append(fee)

average_monthly_fee = sum(valid_fees) / len(valid_fees)

# Total usage hours

total_usage_hours = sum(saas_data["usage_hours"])

# Number of customers per plan

plan_count = {}

for plan in saas_data["plan"]:

    if plan in plan_count:
        plan_count[plan] += 1
    else:
        plan_count[plan] = 1

print("\n================ Summary Statistics ================\n")

print(f"Total Customers: {total_customers}")

print(f"Average Monthly Fee: {round(average_monthly_fee, 2)}")

print(f"Total Usage Hours: {total_usage_hours}")

print("\nPlan Distribution")

for plan, count in plan_count.items():
    print(plan, "-", count)

# ======================================================
# Task 6 – Identify Low Usage Customers
# ======================================================

def find_low_usage_customers(data):

    print("\n================ Low Usage Customers ================\n")

    for i in range(len(data["customer_id"])):

        if data["usage_hours"][i] < 50:

            print(
                f"ID: {data['customer_id'][i]} | "
                f"Name: {data['name'][i]} | "
                f"Plan: {data['plan'][i]} | "
                f"Usage Hours: {data['usage_hours'][i]}"
            )

find_low_usage_customers(saas_data)

# ======================================================
# Task 7 – Unique Plan Types
# ======================================================

unique_plans = sorted(set(saas_data["plan"]))

print("\n================ Available Plans ================\n")

print(unique_plans)

# ======================================================
# Task 8 – Save Cleaned Data to File
# ======================================================

# ------------------------------------------------------
# Save CSV File
# ------------------------------------------------------

try:

    file = open("saas_customers_cleaned.csv", "w")

    # Header
    file.write("customer_id,name,signup_date,plan,monthly_fee,usage_hours\n")

    # Data rows
    for i in range(len(saas_data["customer_id"])):

        row = (
            f"{saas_data['customer_id'][i]},"
            f"{saas_data['name'][i]},"
            f"{saas_data['signup_date'][i]},"
            f"{saas_data['plan'][i]},"
            f"{saas_data['monthly_fee'][i]},"
            f"{saas_data['usage_hours'][i]}\n"
        )

        file.write(row)

except Exception as e:

    print("Error while writing CSV file:", e)

else:

    print("\nCSV file created successfully.")

finally:

    try:
        file.close()
    except:
        pass


# ------------------------------------------------------
# Save Plan Summary File
# ------------------------------------------------------

try:

    summary_file = open("plan_summary.txt", "w")

    for plan, count in plan_count.items():

        summary_file.write(f"{plan} : {count}\n")

except Exception as e:

    print("Error while writing summary file:", e)

else:

    print("Plan summary file created successfully.")

finally:

    try:
        summary_file.close()
    except:
        pass

print("\nAll tasks completed successfully.")