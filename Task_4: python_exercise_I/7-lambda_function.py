"""
This program extracts the year, month, date, and time from a datetime string provided by the user.
The expected format is 'YYYY-MM-DD HH:mm:SS.ssssss'. If the input format is invalid, an error
message is displayed.
"""

# Lambda function to extract year, month, date, and time
result = lambda s: (
    s.split()[0].split('-')[0],  # Year
    s.split()[0].split('-')[1],  # Month
    s.split()[0].split('-')[2],  # Date
    s.split()[1]                 # Time
)

# Allow user to input a datetime string
input_str = input("Enter a datetime string in the format 'YYYY-MM-DD HH:mm:SS.ssssss': ").strip()

# Extract components using the lambda function
try:
    year, month, date, time = result(input_str)

    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"Date: {date}")
    print(f"Time: {time}")

except IndexError:
    print("Invalid input format. Please enter the datetime string in the correct format.")