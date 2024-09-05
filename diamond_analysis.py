import os
from enum import Enum
import pandas as pd

# Define menu options using Enum
class Task(Enum):
    HIGHEST_PRICE = 1
    AVERAGE_PRICE = 2
    IDEAL_COUNT = 3
    COLOR_INFO = 4
    MEDIAN_CARAT_PREMIUM = 5
    AVERAGE_CARAT_CUT = 6
    AVERAGE_PRICE_COLOR = 7
    EXIT = 8


# Load data from a CSV file into a DataFrame.
def load_data(filename='diamonds.csv'):
     return pd.read_csv(filename)


# Find the highest price of diamonds in the DataFrame.
def highest_diamond_price(df):
    return df['price'].max()


# Calculate the average price of diamonds in the DataFrame.
def average_diamond_price(df):
    return df['price'].mean()
   

# Count the number of diamonds classified as 'Ideal' in the DataFrame.
def ideal_diamonds_count(df):
   return df[df['cut'] == 'Ideal'].shape[0]

# Get information about diamond colors in the DataFrame.
def color_info(df):
    colors = df['color'].unique()  # Get unique colors
    num_colors = len(colors)  # Count the number of unique colors
    return num_colors, colors

 # Calculate the median carat weight of diamonds classified as 'Premium'.
def median_carat_premium(df):
    return df[df['cut'] == 'Premium']['carat'].median()

# Calculate the average carat weight for each type of cut.
def average_carat_by_cut(df):
  return df.groupby('cut')['carat'].mean()

# Calculate the average price for each color type.
def average_price_by_color(df):
    return df.groupby('color')['price'].mean()

# Clear command for Windows or Unix-based OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  


def menu():
    # Display the menu header
    print("Menu:")
    
    # Iterate over each item in the Task enumeration
    for item in Task:
        # Print each menu item with its number and formatted name
        # `item.value` is the number associated with the menu item
        # `item.name` is the name of the menu item (e.g., 'HIGHEST_PRICE')
        # `replace("_", " ").title()` formats the name for readability
        print(f'{item.value} - {item.name.replace("_", " ").title()}')
    
    try:
        # Prompt the user to input their selection
        selection = int(input('Your selection: '))
        
        # Check if the selection is a valid menu item
        # `Task._value2member_map_` maps values to corresponding Task members
        if selection in Task._value2member_map_:
            # Return the corresponding Task member
            return Task(selection)
        else:
            # Inform the user that their choice is invalid
            print("Invalid choice, please select a number between 1 and 8.")
            return None
    except ValueError:
        # Handle cases where input is not a number
        print("Invalid input, please enter a number.")
        return None
