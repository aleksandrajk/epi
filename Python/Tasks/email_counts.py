# Initialize an empty dictionary to store email address counts
email_counts = {}

# Open the mail log file (replace 'mail_log.txt' with your file name)
with open('mail_log.txt', 'r') as file:
    for line in file:
        if line.startswith('From '):
            # Split the line into words and get the email address
            words = line.split()
            email = words[1]

            # Update the count for the email address in the dictionary
            email_counts[email] = email_counts.get(email, 0) + 1

# Create a list of (count, email) tuples from the dictionary
count_email_tuples = [(count, email) for email, count in email_counts.items()]

# Sort the list in reverse order to find the person with the most commits
count_email_tuples.sort(reverse=True)

# Print out the person with the most commits
if count_email_tuples:
    most_commits = count_email_tuples[0]
    print(f"The person with the most commits is {most_commits[1]} with {most_commits[0]} commits.")
else:
    print("No 'From' lines found in the log.")
