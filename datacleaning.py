#python program that accept user input and cleaned the duplicate raw data:

def clean_user_data(raw_input):
    
    raw_list = raw_input.split(',')

    cleaned = [item.strip().lower() for item in raw_list]

    cleaned = list(set(cleaned))
    cleaned = [item for item in cleaned if len(item) > 2]

    return cleaned

user_input = input("Enter your raw data (comma-separated):\n")

cleaned_data = clean_user_data(user_input)


print("\n Cleaned Data:")
print(cleaned_data)
