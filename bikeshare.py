## Add first comment for the refactoring

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_day = 'none'
city = 'none'

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
    city_filter = False
    
    while city_filter == False:
        global city
        city = str(input('\nWould you like to see data for Chicago, New York City, or Washington?\n'))
        city = city.lower()

        for i in CITY_DATA.keys():
            if city == i:
                city_filter = True
                break
        
        if city_filter == False:
            print('\nCity not recognized, please enter valied city from the list provided\n\n')
        
        
                
    #filter by Month - day
    month_day_filter = False
    
    while month_day_filter == False:
        global month_day
        month_day = str(input('\nWould you like to filter the data by month, day, both or not at all? Type "none" for no time filter.\n'))

        for i in ['month','day','both','none']:
            if month_day == i:
                month_day_filter = True
                break
        
        if month_day_filter == False:
            print('\nNot a valid option, please enter valied option from the list provided\n')
        
    # get user input for month (all, january, february, ... , june)
    
    if month_day == 'month' or month_day == 'both':
    
        month_filter = False
    
        while month_filter == False:

            month = str(input('\nWhich month? January, February, March, April, May, or June?\n'))

            for i in ['January','February','March','April','May','June']:
                if month == i:
                    month_filter = True
                    break
        
            if month_filter == False:
                print('\nNot a valid month, please enter valied month from the list provided\n')
    else:
        month = 'all'
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if month_day == 'day' or month_day == 'both':
    
        day_filter = False
    
        while day_filter == False:

            day = str(input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday?\n'))

            for i in ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']:
                if day == i:
                    day_filter = True
                    break
        
            if day_filter == False:
                print('\nNot a valid day, please enter valied day from the list provided\n')
    else:
        day = 'all'



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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    if month_day != 'month' and month_day != 'both':
        df['month'] = df['Start Time'].dt.month
    
        popular_month = df['month'].mode()[0]
        
        print('Most Frequent Start Month:', popular_month)
    
    
    # TO DO: display the most common day of week
    if month_day != 'day' and month_day != 'both':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
    
        popular_day = df['day_of_week'].mode()[0]
            
        print('Most Frequent Start Day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
            
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + '  ----  ' + df['End Station']
    
    popular_trip =  df['Trip'].mode()[0]
    
    print('Most Frequent Trip: ( ', popular_trip, ' )')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    
    print('Total Travel Time:', total_trip)

    # TO DO: display mean travel time
    avg_trip = df['Trip Duration'].mean()
    
    print('Average Travel Time:', avg_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('> User Types Count:\n')
    print(df['User Type'].value_counts().to_string())
    
    
    if city != 'washington':
        print('\n\n')
    
        # TO DO: Display counts of gender
        print('> Gender Count:\n')
        print(df['Gender'].value_counts().to_string())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\n\n')
        
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        
        print('Earliest year of birth:', earliest_year)
        print('Recent year of birth:', recent_year)
        print('Common year of birth:', common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data == 'yes':
            
            start_loc = 0
            view_display = 'yes'
            
            while view_display == 'yes':
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                view_display = 'no'
                view_display = input("Do you wish to continue?: ").lower()
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

