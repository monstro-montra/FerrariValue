def get_input():
    while True:  # start a while loop
        try:  # try to execute the following block
            print("Input a year between 1962 and 2014.")
            year = int(input())
            if 1962 <= year <= 2014:
                return year
            else:
                raise ValueError
        except ValueError:  # if exception occurs, execute this block. restart the loop
            print("Invalid input, please input a year between 1962 and 2014.")


def main():
    year = get_input()
    car_price = 0
    if 1962 <= year <= 1964:
        car_price = 18500
    elif 1965 <= year <= 1968:
        car_price = 6000
    elif 1969 <= year <= 1971:
        car_price = 12000
    elif 1972 <= year <= 1975:
        car_price = 48000
    elif 1976 <= year <= 1980:
        car_price = 200000
    elif 1981 <= year <= 1985:
        car_price = 650000
    elif 1986 <= year <= 2012:
        car_price = 35000000
    else:
        car_price = 52000000

    print(f"During the year of {year}, the price of a Ferrari was ${car_price}.")


if __name__ == "__main__":  # declare which function is the main function
    main()
