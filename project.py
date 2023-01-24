#GDP Finder Final Project for CS50 Python
import sys
from pandas_datareader import wb

def main():
    print('Welcome to GDP Finder')
    #input country
    countries = input('Input countries of interest in its initials: ').upper()
    countries = countries.split(" ")
    check_countries(countries)
    #input the years
    year1, year2 = input('Years to check gdp(seperate by space): ').split()
    df = gdp(countries, year1, year2)
    print(df)
    csv_print(df)



def check_countries(countries):
    #check if countries follows the initial guideline
    try:
        for i in range(len(countries)):
            check_len(countries[i])
    except ValueError:
        sys.exit('Input the countries initials. i.e USA')

def check_len(country):
    #checking the length of the initials to comfirm
    if len(country) <= 3 and len(country) > 1:
        return country
    else:
        raise ValueError

def gdp(countries, year1, year2):
    wb_gdp = "NY.GDP.MKTP.CD"
    #get gdp data
    df = wb.download(indicator=wb_gdp, country=countries, start=year1, end=year2)
    return df

def csv_print(df):
    #ask user if they want to print
    while True:
        ans = input('Export data to csv file? Y/N: ').upper()
        if ans == 'Y':
            create_csv(df)
            break
        elif ans == 'N':
            sys.exit()
        else:
            print("Y or N: ")

def create_csv(df):
    filename = input("Name of file: ")
    df.to_csv(f'{filename}.csv')

if __name__ == "__main__":
    main()