""" This is the Module 1 homework that works Python fundamentals
P1: Create a New Python Module (Company Byline) - 44-608: Working Group 2
Coding completed using course resources, LinkedinLearning, and ChatGPT4 to work out the errors
Jason Ballard
"""
# import math #coded out because the statistic module handles the code- be effieicnt 
import statistics
# Byline function
def byline():
    return "Created by Jason Ballard for Stellar Analytics Inc."

def main():
# Display all output 
    company_name = "Stellar Analytics Inc."
    count_active_projects = 5
    has_international_presence = False
    average_client_satisfaction = 4.7
    services_offered_string = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
    satisfaction_scores = [4.8, 4.6, 4.9, 5.0, 4.7]
    active_projects_string = f"Active Projects: {count_active_projects}"
    international_presence_string = f"International Presence: {has_international_presence}"
    client_satisfaction_string = f"Average Client Satisfaction: {average_client_satisfaction}"
# Calculating statistics
    smallest = min(satisfaction_scores)
    largest = max(satisfaction_scores)
    total = round(sum(satisfaction_scores))  # Rounding the total
    count = len(satisfaction_scores)
    mean = statistics.mean(satisfaction_scores)
    median = statistics.median(satisfaction_scores)
    standard_deviation = statistics.stdev(satisfaction_scores)
 # Handling mode with exception- this fixes the Mode error
    try:
        mode = statistics.mode(satisfaction_scores)
    except statistics.StatisticsError:
        mode = "No unique mode"

 # Printing information
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print("Services Offered:", ", ".join(services_offered_string))
    print("Statistics:")
    print(f"Smallest Satisfaction Score: {smallest}")
    print(f"Largest Satisfaction Score: {largest}")
    print(f"Total of Scores (Rounded): {total}")
    print(f"Number of Scores: {count}")
    print(f"Mean Satisfaction Score: {mean:.2f}")
    print(f"Mode of Satisfaction Scores: {mode}")
    print(f"Median Satisfaction Score: {median}")
    print(f"Standard Deviation of Scores: {standard_deviation:.2f}")
    print(byline())

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

print()
print("Module 1 homework by Jason Ballard")
