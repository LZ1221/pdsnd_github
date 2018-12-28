import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:  
        city = input("Please enter city name:").lower()
        if city in ['chicago','new york city', 'washington']:
            break
        else: 
            print("City Name Not Valid")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Please enter month name:").lower()
        if month in ['all','january','february','march','april','may','june']:
            break
    else:
        print("Month Name Not Valid")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day=input("please enter a day of week:").lower() 
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
    else:
        print("Day Name Not Valid")
        
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month 
    common_month = df['Month'].mode()[0]
    print('Most common month:',common_month) 
    # TO DO: display the most common day of week
    df['Day'] = df['Start Time'].dt.weekday
    common_day = df['Day'].mode()[0]
    print('Most common day:',common_day)
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('Most common start hour:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('Most Common Start Station:',common_start)

    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('Most Common End Station:',common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_station=df.groupby(['Start Station','End Station'],axis=0).size().nlargest(1)
    print('Most common station combination:',common_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime=df['Trip Duration'].sum(axis=0)
    print('Total Travel Time:',total_traveltime)
    # TO DO: display mean travel time
    mean_traveltime=df['Trip Duration'].mean(axis=0)
    print('Mean Travel Time:',mean_traveltime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertype=df['User Type'].value_counts()
    print('Count of user types:',count_usertype)
    # TO DO: Display counts of gender
    try:
        genders=df['Gender'].value_counts()
        print('Genders:')
        print(genders)
        print()
    except KeyError:
        print("There isn't a [Gender] column in this spreadsheet!")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birth=df['Birth Year'].min()
        max_birth=df['Birth Year'].max()
        common_birth=df['Birth Year'].mode()[0]
        print('Earliest birthyear:',min_birth)
        print('Most recent birthyear:',max_birth)
        print('Most common birthyear:',common_birth)
    except KeyError:
        print("There isn't a [Birth Year] column in this spreadsheet!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df): 
    display = input('Would you like to see raw data?\n') 
    counter = 0 
    while display.lower() == "yes": 
        print (df.iloc[counter:counter + 5]) 
        display = input('\n whether user want to see next 5 records of raw data? \n') 
        counter += 5
       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
