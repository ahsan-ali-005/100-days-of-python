# Analyze large log file

def analyze_log(file_name):
    error = 0
    info = 0
    warning = 0
    total = 0

    error_logs = []

    with open(file_name, "r") as f:
        for line in f:
            parts = line.split()

            if len(parts) < 3:
                continue

            total += 1
            log_type = parts[2]

            if log_type == "INFO":
                info += 1
            elif log_type == "WARNING":
                warning += 1
            elif log_type == "ERROR":
                error += 1
                error_logs.append(line.strip())

    return total, info, warning, error, error_logs


def filter_by_date(file_name, date):
    results = []

    with open(file_name, "r") as f:
        for line in f:
            if line.startswith(date):
                results.append(line.strip())
        
        if not results:
            print("No activity on this date.")

    return results


def search_keyword(file_name, keyword):
    results = []

    with open(file_name, "r") as f:
        for line in f:
            if keyword.lower() in line.lower():
                results.append(line.strip())

    return results


def generate_report(total, info, warning, error):
    print("\n📊 LOG REPORT")
    print("-" * 30)
    print(f"Total Logs   : {total}")
    print(f"INFO Logs    : {info}")
    print(f"WARNING Logs : {warning}")
    print(f"ERROR Logs   : {error}")

    if total > 0:
        print(f"\nError %   : {(error/total)*100:.2f}%")
        print(f"Warning % : {(warning/total)*100:.2f}%")
    print("-" * 30)


# -------- MAIN PROGRAM --------

file_name = "logfile.txt"

total, info, warning, error, error_logs = analyze_log(file_name)

generate_report(total, info, warning, error)

# Show first 5 errors
print("\n❌ Sample ERROR Logs:")
for e in error_logs:
    print(e)


# Filter by date
date = input("\nEnter date to filter (YYYY-MM-DD): ")
filtered_logs = filter_by_date(file_name, date)

print(f"\n📅 Logs on {date}:")
for log in filtered_logs[:5]:
    print(log)


# Search keyword
keyword = input("\nEnter keyword to search: ")
results = search_keyword(file_name, keyword)

print(f"\n🔍 Results for '{keyword}':")
for r in results:
    print(r)