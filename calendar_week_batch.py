#!/usr/bin/env python3

# Python 3.9.5

# calendar_week_batch.py

def batch_prod_weeks(path, file, out_file):

    if os.path.isfile(path + "\\" + out_file):
        os.remove(out_file)
        output_file = open('calendar_week_result.txt', 'wt', encoding='UTF-8')
    else:
        output_file = open('calendar_week_result.txt', 'wt', encoding='UTF-8')

    with open(file, 'rt', encoding='UTF-8') as input_file:
        dates = input_file.readlines()
        dates = [date.replace('\r', '').replace('\n', '')for date in dates]
        date_counter = 0

        for date in dates:
            date_counter += 1
            date = calendar_week.convert_date(date)
            if date_counter < len(dates):
                output_file.write(date + '\n')
            else:
                output_file.write(date)

    output_file.close()
    return

if __name__ == '__main__':
    # calendar_week.py and calendar_week_batch.py are supposed to be in the same directory.
    # Create the TXT file calendar_week.txt and fill in the dates which have to be converted.
    # Use the format dd.mm.yyyy or %d.%m.%Y
    import os
    path = "/home/user"
    os.chdir(path)
    import calendar_week
    file = 'calendar_week.txt'
    out_file = 'calendar_week_result.txt'
    batch_prod_weeks(path, file, out_file)
