import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
Days = ['all', 'monday', 'tuesday', 'wednesday', 'thurday', 'friday', 'saturday', 'sunday']

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
        city = input('Which city do you want to explore Chicago, New York City or Washington? ').lower()
        if city not in CITY_DATA:
            print('Invalid input! Please choose either Chicago, New York City or Washington')
        elif city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to see? \n(NOTE: you can type all to see all months) ').lower()
        if month not in Months:
            print('Sorry either you typed it wrong or we do not have data from this month, Please try again!')
        elif month in Months:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input('Last thing! could you type the day of the week that you want to see? \n(NOTE: you can type all to see all days) ').lower()
        if day not in Days: 
            print('Invalid input! Please check your spelling')
        elif day in Days: 
            break
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = Months.index(month) 
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: '+ Months[common_month].title())

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: '+ common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour of the day is: '+ str(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start staion is: ', common_start_station)
            
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    start_end_combination = (df['Start Station'] + '||' + df['End Station']).mode()[0]
    print('The most frequent combination of start and end station trip is: ' + str(start_end_combination.split('||')))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types is: ', user_types)

    # TO DO: Display counts of gender
# NOTE that gender and birth year are only in chicago and new yourk city data
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print('Counts of gender is: ', gender) 
       # TO DO: Display earliest, most recent, and most common year of birth 
        earliest_birth = df['Birth Year'].min()
        print('The earliest birth year is: ', earliest_birth)
        
        recent_birth = df['Birth Year'].max()
        print('The most recent birth year is: ', recent_birth)
        
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', common_birth_year)
    

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    next = 0
    while True:
        view_data = input('Would you like to view five rows of individual trip data?\n (NOTE: Please enter yes or no) ')
        if view_data == 'yes':
            print(df.iloc[next:next+5])
        elif view_data == 'no':
            return
        else:
            print('Invalid input, please try again')
        while (view_data.lower() == 'yes'):
            cont_data = input ('Would you like to continue? ').lower()
            if cont_data == 'yes':
                next += 5
                print(df.iloc[next:next+5])
            elif cont_data == 'no':
                return
            else:
                print('Invalid input, please try again')
    

def main():
	 """Main body of program"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
