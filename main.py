from diamond_analysis import Task, load_data, highest_diamond_price, average_diamond_price, ideal_diamonds_count, color_info, median_carat_premium, average_carat_by_cut, average_price_by_color, clear_screen, menu

def main():
    # Load data from CSV file into a DataFrame
    df = load_data()  
    
    while True:
        # Display the menu and get the user's choice
        user_selection = menu()  

       
            # Handle the selection for highest diamond price
        if user_selection == Task.HIGHEST_PRICE:
                # Calculate and print the highest diamond price
                print("Highest diamond price:", highest_diamond_price(df))

            # Handle the selection for average diamond price
        elif user_selection == Task.AVERAGE_PRICE:
                # Calculate and print the average diamond price
                print("Average diamond price:", average_diamond_price(df))

            # Handle the selection for count of Ideal diamonds
        elif user_selection == Task.IDEAL_COUNT:
                # Calculate and print the number of diamonds classified as 'Ideal'
                print("Number of Ideal diamonds:", ideal_diamonds_count(df))

            # Handle the selection for color information
        elif user_selection == Task.COLOR_INFO:
                # Get the number of different colors and the list of colors
                num_colors, colors = color_info(df)
                # Print the number of colors and the list of colors
                print(f"Number of different colors: {num_colors}")
                print("Colors:", colors)

            # Handle the selection for median carat of Premium diamonds
        elif user_selection == Task.MEDIAN_CARAT_PREMIUM:
                # Calculate and print the median carat of Premium diamonds
                print("Median carat of Premium diamonds:", median_carat_premium(df))

            # Handle the selection for average carat by cut type
        elif user_selection == Task.AVERAGE_CARAT_CUT:
                # Calculate average carat for each cut type and print results
                average_carat = average_carat_by_cut(df)
                print("Average carat for each cut type:")
                for cut, carat in average_carat.items():
                    # Print each cut type with its corresponding average carat, formatted to 2 decimal places
                    print(f"{cut}: {carat:.2f}")  

            # Handle the selection for average price by color type
        elif user_selection == Task.AVERAGE_PRICE_COLOR:
                # Calculate average price for each color type and print results
                average_price = average_price_by_color(df)
                print("Average price for each color type:")
                for color, price in average_price.items():
                    # Print each color type with its corresponding average price, formatted to 2 decimal places
                    print(f"{color}: {price:.2f}")  

            # Handle the selection to exit the program
        elif user_selection == Task.EXIT:
                # Clear the screen and print a goodbye message
                clear_screen()
                print("Exiting the program. Goodbye!")
                break  # Exit the loop and end the program




if __name__ == "__main__":
    main()
