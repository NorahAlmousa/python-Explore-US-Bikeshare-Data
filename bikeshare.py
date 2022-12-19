import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#*arrays for the months and days 
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


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
    city = str.lower(input('----Choose one of the cities > chicago, new york city , washington:').strip())
    while city not in CITY_DATA:
        city = str.lower(input('Invalid,please choose again : ').strip())
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str.lower(input('----Choose one month or "all" > january,february,march,april,may,june:').strip())
    while month not in months:
        month = str.lower(input('Invalid,please choose again : ').strip())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str.lower(input('----Choose one day or "all" >monday,tuesday,wednesday,thursday,friday,saturday,sunday:').strip)
    while day not in days:
        day = str.lower(input('Invalid,please choose again : ').strip)

    print('-'*45)
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
    
    # Loading data file into a dataframe.
    df = pd.read_csv(CITY_DATA[city])
    
    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # Extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filtering by month if applicable
    if month != 'all':
        # Useing the index of the months list to get corresponding integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filtering by month to create new dataframe
        df = df[df['month'] == month]
        
    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    

        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    Most_Common_Month = months[df['month'].mode()[0]]  
    print('The most common month :{}'.format(Most_Common_Month))
        
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    Most_Common_Day = days[df['day_of_week'].mode()[0]] 
    print('The most common day :{}'.format(Most_Common_Day))
        
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_Common_hour = df['hour'].mode()[0] 
    print('The most common hour :{}'.format(Most_Common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    # create new column then use mode method on it
    df['start_end_station'] = 'start >'+ df['Start Station'] + ',' + 'end >' + df['End Station']
    Combination_Station  = df['start_end_station'].mode()[0]
    print('The most frequent combination of start station and end station trip:\n{}'.format(Combination_Station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total of the travel time : {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean of the travel time : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types :\n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
     print('The counts of user types :\n{}'.format(df['Gender'].value_counts()))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
     print('The earliest year of birth : {}\nThe most recent year of birth : {}\nThe most common year of birth:{}'.format(df['Birth Year'].max(),df['Birth Year'].min(),df['Birth Year'].mode()[0]) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
 #Display Data 
        Display_Data = str.lower(input('\nWould you like to see the 5 lines of raw data? Enter yes or no .'))
        index = 0
         
         
        if (Display_Data!='yes') and  (Display_Data!= 'no'):
           Display_Data = str.lower(input('Invalid,please enter yes or no again : '))
        elif Display_Data == 'yes':          
            print(df.head())
            
            while True :  
                
              Display_Data = str.lower(input('\nWould you like to see the next 5 lines of raw data? Enter yes or no .'))
          
              while (Display_Data!='yes') and  (Display_Data!= 'no'):
                Display_Data = str.lower(input('Invalid,please enter yes or no again : '))
                
              index += 5  
              if Display_Data == 'yes' :
                   
                    if (index+5) < (len(df)) :
                      print(df.iloc[index:index+5])
                    else :
                        print('No more raw data to display!')
                
              else :
                   break
        else :
              break 
      

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
