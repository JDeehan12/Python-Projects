# The following script finds LinkedIn profiles for a list of contacts in csv.
# The contacts' LinkedIn profiles are found using their name and company name.
# The script utilises the pandas library to read and manipulate CSV data and the googlesearch library to perform Google searches.


import pandas as pd
from googlesearch import search

def google_search(name, company):
    # Create a search query by combining the name, company, and "LinkedIn"
    query = f"{name} {company} LinkedIn"
    
    try:
        # Using next() to get the first result from the Google search
        result = next(search(query, lang='en', num_results=1))
        return result
    except StopIteration:
        return "No results found"

def add_google_links(csv_file):
    # Read the CSV file into a DataFrame using pandas
    df = pd.read_csv(csv_file)

    # Add a new column 'Google_Link' to store the search results for each row
    df['Google_Link'] = df.apply(lambda row: google_search(row['Name'], row['Company']), axis=1)

    # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)

# 'if __name__ == "__main__":' Ensures that the script is executed only when run directly, not when imported as a module.
if __name__ == "__main__":
    # Replace 'contacts.csv' with the actual CSV file name and file path
    input_csv_file = '/path/to/your/contacts.csv'
    
    try:
        # Call the function to add Google links to the CSV file
        add_google_links(input_csv_file)
        
        # Display a success message if the operation is successful
        print(f"Google links added to '{input_csv_file}'.")
    except Exception as e:
        # Display an error message if an exception occurs during the process
        print(f"An error occurred: {e}")

