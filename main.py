# Noah Shuldberg
# Video Game Reccomendation System
import pandas as pd
print("Welcome to video game catalog manager")
while True:
    try:
        # Read CSV and create cleaned dataframe
        video_games = pd.read_csv("Level11Assignment/video_games_raw.csv")
        video_games_cleaned = pd.DataFrame(video_games)

        # Get desired  row from user and standardize row numbers to begin at 1.
        user_row = int(input("Which row would you like to inspect?: "))
        if user_row not in range(1,16):
            raise ValueError("Invalid row input. Please try again.")
        user_row -=1

        # Print user's desired row information
        print("\n",video_games.iloc[user_row])

        # Prompt the user to update game's status
        print(f"\nUpdate the status for {video_games.loc[user_row, 'Title']}")
        print("==========")

        # Let user change the status of the game.
        while True:
            try:
                print("OPTIONS:")
                print("1. Backlog\n2. Playing\n3. Completed\n4. Dropped")
                selection = int(input("\nSelect an option (1-4): "))
                if selection not in range(1,5):
                    raise ValueError("Invalid input. Try again.")
                if selection == 1:
                    video_games_cleaned.at[user_row, "Status"] = "Backlog"
                elif selection == 2:
                    video_games_cleaned.at[user_row, "Status"] = "Playing"
                elif selection == 3:
                    video_games_cleaned.at[user_row, "Status"] = "Completed"
                elif selection == 4:
                    video_games_cleaned.at[user_row, "Status"] = "Dropped"
                print("Status updated.")
                break

            except ValueError as e:
                print(e)

        # Create recommendation column and assign the games that meet the criteria as "Yes".
        video_games_cleaned["Recommended"] = "No"

        video_games_cleaned.loc[
            (video_games_cleaned["Rating"] >= 8) &
            (video_games_cleaned["Price"] <= 40.00),
            "Recommended"] = "Yes"

        recommended = video_games_cleaned.query("Recommended == 'Yes'")
        # Save new data to new cleaned games file, and remove the index that would cause a duplicate index column to be created.
        video_games_cleaned.to_csv("video_games_cleaned.csv", index=False)
        print("\nRecommended games:")
        print(recommended)

        # Inform user that new data is saved to new csv file.
        print("New data saved in video_games_cleaned.csv")
        break
    except ValueError as ve:
        print(ve)