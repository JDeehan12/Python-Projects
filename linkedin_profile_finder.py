import pandas as pd
from googlesearch import search
import time
import random

def google_search(name, company):
    # Create a search query by combining the name, company, and "LinkedIn"
    query = f"{name} {company} LinkedIn"
    
    try:
        # Using next() to get the first result URL from the Google search
        results = search(query, lang='en')
        first_result = next(results)
        return first_result
    except StopIteration:
        return "No results found"
    except Exception as e:
        return f"Error: {e}"

def add_google_links(csv_file):
    # Read the CSV file into a DataFrame using pandas
    df = pd.read_csv(csv_file)

    # Add a new column 'Google_Link' to store the search results for each row
    df['Google_Link'] = df.apply(lambda row: google_search(row['Name'], row['Company']), axis=1)

    # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)
    
    # Add a delay between each search request
    time.sleep(random.uniform(1, 3))

    return df

# 'if __name__ == "__main__":' Ensures that the script is executed only when run directly, not when imported as a module.
if __name__ == "__main__":
    # Replace 'contacts.csv' with the actual CSV file name and file path
    input_csv_file = 'contacts.csv'
    
    df = pd.DataFrame()  # Initialize an empty DataFrame
    
    try:
        # Call the function to add Google links to the CSV file
        df = add_google_links(input_csv_file)
        
        # Display a success message if the operation is successful
        print(f"Google links added to '{input_csv_file}'.")
    except Exception as e:
        # Display an error message if an exception occurs during the process
        print(f"An error occurred: {e}")
    finally:
        # Save the DataFrame even if an error occurred
        df.to_csv(input_csv_file, index=False)