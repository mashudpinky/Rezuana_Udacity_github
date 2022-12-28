import time
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

city_dic = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def user_input():
    while True:
        city = input("Which city you want to show its data ? ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
        
            break
        else:
            print("{} is not in our list. Please enter city from these : Chicago-New York City-Washington  ".format(city))
        
    


    while True:
    
        month=input("Enter month from january to june you want to show its data  or all for all months :  ")
        month=month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            
            break
        else:
            print("{} is not in our list. Please enter month from january to June ".format(month))     
 
               
            
            
    
    while True:
    
        day=input("Enter weekday to show its data or all for all weekday data : ")
        day=day.lower()
        if day in ['saturday','sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
            break
        else:
            print("{} is not in weekday. Please enter weekday from saturday to friday :  ".format(day))
            
            
    return city,month,day       
        

    


def pass_user_input(city,month,day):
    df=pd.read_csv(city_dic[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.day_name()
    if month!='all':
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    if day!='all':
        df = df[df['Weekday'] == day.title()]
        
    return df



def user_data(city,df):
    user_type=df['User Type'].value_counts()
    print("Users Types is... \n{}".format(user_type))
    if city!="washington":
        gender=df['Gender'].value_counts()
        print("Users Gender Are \n{}".format(gender))
        
        oldest_year=df['Birth Year'].min()
        oldest_year=int(oldest_year)
        current_year=datetime.now().year
        oldest_age=current_year-int(oldest_year)
        print("Oldest User Born in {} and now his/her age is {} years".format(oldest_year,oldest_age))
        latest_year=df['Birth Year'].max()
        latest_year=int(latest_year)
        youngest_age=current_year-int(latest_year)
        print("Youngest User Born in {} and now his/her age is {} years".format(latest_year,youngest_age))
        frequent_year=df['Birth Year'].mode()[0]
        frequent_year=int( frequent_year)
        print("Common User Birth Year is {}".format(frequent_year))
        print('-'*40)
        
        
        
def station_data(df):
    start_time = time.time()
    Popular_start_station=df['Start Station'].mode()[0]
    print("Most Popular Start Stations is {}".format(Popular_start_station))
    popular_end_station = df['End Station'].mode()[0]
    print("Most Popular End Stations is {}".format(popular_end_station))
    
    strt_to_fnsh=df.groupby(['Start Station','End Station'])
    pop_strt_to_fnsh = strt_to_fnsh.size().sort_values(ascending=False).head(1)
    print("Most Popular Trip is\n {}".format(pop_strt_to_fnsh))
    print("\nThis took %s seconds." % (time.time() - start_time))
    #pop_strt_to_fnsh=sorted_strt_to_fnsh.mode()[0]        

    
    
    
def Time_data(df):
    start_time = time.time()
    df['Hour']=df['Start Time'].dt.strftime('%H:%M')
    freq_hour=df['Hour'].mode()[0]
    print("{}  is the most frequent start time".format(freq_hour))
    freq_weekday=df['Weekday'].mode()[0]
    print("{}  is the most frequent weekday".format(freq_weekday))
    freq_month=df['Month'].mode()[0]
    freq_month_name=calendar.month_name[freq_month]
    print("{} is the most frequent month".format(freq_month_name))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
def Trip_data(df):
    start_time = time.time()
    travel_time=df['Trip Duration'].sum()
    travel_time_mins=round(travel_time/60,2)
    travel_time_hrs=round(travel_time/360,2)
    print("Total travel time of all the trips is {} seconds==> {} minutes ==> {} hours".format(travel_time,travel_time_mins,travel_time_hrs))
    travel_time_avg=df['Trip Duration'].mean()
    travel_time_avg=round(travel_time_avg,2)
    travel_time_avg_mins=round(travel_time_avg/60,2)
    print("Total trip average time is {} seconds ==> {} minutes".format(travel_time_avg,travel_time_avg_mins))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  
    

    
    
def display_data(df):
    
    row=0
    fst_input=input("Do you want to view the first five rows in raw data? ")
    fst_input=fst_input.lower()
    if fst_input=="yes":
        print(df.head())
    elif fst_input!="no":
        print("wrong input only yes or no")
    while fst_input=="yes":
        row+=5
        fst_input=input("do you want to view next 5 rows  ? ")
        if fst_input=="yes":
            print(df[row:row+5])
        elif fst_input!="yes":
            break
    
    
    
    
    
def main():
    while True:
        city, month, day = user_input()
        df = pass_user_input(city, month, day)
        user_data(city,df)
        print('*'*40)
        station_data(df)
        print('*'*40)
        Time_data(df)
        print('*'*40)
        Trip_data(df)
        print('*'*40)
        display_data(df)
        
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
               main()    
