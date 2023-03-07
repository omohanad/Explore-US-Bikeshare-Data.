import time

from pandas import Series, DataFrame
import pandas as pd

import calendar
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """This function gets the user input for city, month, and day, and validates the inputs."""
    while True:
        try:
            city = input("Please choose a city between Chicago, New York City, or Washington:\n")
            if city.lower() not in CITY_DATA:
                print("Invalid input. Please enter Chicago, New York City, or Washington.\n")
            else:
                break 
        except:
            pass
       
    while True:
        try:
            month = input('Enter the month as an integer (1=January, 2=February, 3=March, 4=April, 5=May, 6=June, or all): ')

            if month.lower() == 'all':
                break

            month_int = int(month)
            if month_int not in range(1, 7):
                print("Invalid input. Please enter a valid month or 'all'.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid month or 'all'.\n")

      
    while True:
        try:
            day = input("Please choose a day of the week or 'all': 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday, or all\n") 
            if day.lower() == 'all':
                break

            day_int = int(day)
            if day_int not in range(1, 8):
                print("Invalid input. Please enter a valid day or 'all'.\n")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid day or 'all'.\n")

##Using t
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


           
            # using while to make sure that the input matches the data i aready have
     ## using try and except to avoid any invalid inputs of the user  
           
          
          
          
          
    
    print("Please choose your city: ")
    print("\n1. Chicago 2. New York City 3. Washington")
   
    print("\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).\nFull name in title case (e.g. Chicago).")
    




    print('-'*40)
    return city, month, day



def load_data(city, month, day):  
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        try:
            month_int = int(month)
            if month_int not in range(1, 7):
                print("Invalid input. Please enter a valid month or 'all'.\n")
                return pd.DataFrame()
        except ValueError:
            print("Invalid input. Please enter a valid month or 'all'.\n")
            return pd.DataFrame()

        # filter by month to create the new dataframe
        df = df[df['month'] == month_int]

    # filter by day of week if applicable
    if day != 'all':
        try:
            day_int = int(day)
            if day_int not in range(1, 8):
                print("Invalid input. Please enter a valid day or 'all'.\n")
                return pd.DataFrame()
        except ValueError:
            print("Invalid input. Please enter a valid day or 'all'.\n")
            return pd.DataFrame()

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day_int]

    return df
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (df) Pandas DataFrame containing city data filtered by month and day
    Returns:
        None
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: ", common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df):
    """Displays rows of the DataFrame based on user preference."""
    pd.set_option('display.max_columns', None)
    i = 0
    while True:
        answer = input("Would you like to display the next 5 rows of data? Enter 'yes' or 'no': ").lower()
        if answer not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        if answer == 'no':
            break
        print(df[i:i+5])
        i += 5
        if i >= len(df):
            print("End of data.")
            break

                    
def station_stats(df): 
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    # display most frequent combination of start station and end station trip
    most_start_end = df['Start Station'] + " " + df['End Station'].mode()[0]
    
    print("The Most Crowded  Start Station is",most_used_start)
    print("The Most Crowded End Station is",most_used_end)
    print("The Most Common between both",most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    
    

    # display mean travel time
    averg_travel_time = df['Trip Duration'].mean()

    print('The Total Travel Time is', total_time/3600 ,'hours' )##Totla time in hours
    print('The Average Time of Travel is', averg_travel_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_users = df['User Type'].value_counts()
    print('Counts of user type', count_users)

    try:
        # Display counts of gender
        print(df['Gender'].value_counts())
    except KeyError:
        print("Gender data is not available.")

    # Display earliest, most recent, and most common year of birth
    try:
        print("Earliest year of birth:", df['Birth Year'].min())
        print("Most recent year of birth:", df['Birth Year'].max())
        print("Most common year of birth:", df['Birth Year'].mode()[0])
    except KeyError:
        print("Birth year data is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        display_rows(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 main()

    
