import enum
import os
import re

from requesting_urls import get_html

# Enum class to map month names to corresponding month number
class Month(enum.Enum):
   January = Jan = 1
   February = Feb = 2
   March = Mar = 3
   April = Apr = 4
   May = 5
   June = Jun = 6
   July = Jul = 7
   August = Aug = 8
   September = Sep = 9
   October = Oct = 10
   November = Nov = 11
   December = Dec = 12

def find_dates(html, output=None):
    """ Function that finds all dates in html content.

    Date formats:
        DMY: 13 October 2020  | 13 Oct 2020  | October 2020
        MDY: October 13, 2020 | Oct 13, 2020 | October, 2020
        YMD: 2020 October 13  | 2020 Oct 13
        ISO: 2020−10−13

    Regex used in this function:
        ([0123]?[0-9] ' + months + ' [0-9]{4})          Find dates in DMY format.
                                                        DMY dates: 13 October 2020 | 13 Oct 2020

        (' + months + ' [0123]?[0-9], [0-9]{4})         Find dates in MDY format.
                                                        MDY dates: October 13, 2020 | Oct 13, 2020

        ([0-9]{4} ' + months + ' [0123]?[0-9])          Find dates in YMD format.
                                                        YMD format: 2020 October 13 | 2020 Oct 13

        ([0-9]{4}-[012]?[0-9]-[012]?[0-9])              Find dates in ISO format.
                                                        ISO format: 2020-10-13

        ((?<![0-9] )' + months + ',? [0-9]{4})          Find short dates in MDY or DMY format.
                                                        Short MDY/DMY format: October 2020 | October, 2020


    :param html (str): Html content to search.
    :param output_filename (str): Output filename.

    :return: List of all formatted dates.
    """

    # Added explicit month names because regex found other words that matched, like "9 Masters 1000"
    months = '(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'  # ?: -> not match group

    dmy_regex = '([0123]?[0-9] ' + months + ' [0-9]{4})'
    mdy_regex = '(' + months + ' [0123]?[0-9], [0-9]{4})'
    ymd_regex = '([0-9]{4} ' + months + ' [0123]?[0-9])'
    iso_regex = '([0-9]{4}-[012]?[0-9]-[012]?[0-9])'
    dmy_mdy_short_regex = '((?<![0-9] )' + months + ',? [0-9]{4})' # ((?<![0-9] ) -> do not match already matched patterns

    # Format DMY
    dmy_dates = re.findall(dmy_regex, str(html))
    formatted_dmy_dates = [re.sub(dmy_regex, format_dmy, date) for date in dmy_dates]

    # Format MDY
    mdy_dates = re.findall(mdy_regex, str(html))
    formatted_mdy_dates = [re.sub(mdy_regex, format_mdy, date) for date in mdy_dates]

    # Format YMD
    ymd_dates = re.findall(ymd_regex, str(html))
    formatted_ymd_dates = [re.sub(ymd_regex, format_ymd, date) for date in ymd_dates]

    # Format ISO
    iso_dates = re.findall(iso_regex, str(html))
    formatted_iso_dates = [re.sub('-', '/', date) for date in iso_dates]

    # MDY or DMY
    mdy_dmy_short_dates = re.findall(dmy_mdy_short_regex, str(html))
    formatted_mdy_dmy_dates = [re.sub(dmy_mdy_short_regex, format_mdy_dmy_short_dates, date) for date in mdy_dmy_short_dates]

    # Add all formatted dates together in one list
    all_formatted_dates = formatted_iso_dates + formatted_mdy_dates + formatted_dmy_dates + formatted_ymd_dates + formatted_mdy_dmy_dates

    # Write to file
    if not os.path.exists('filter_dates_regex'):
        os.makedirs('filter_dates_regex')

    file = open('filter_dates_regex/{}.txt'.format(output), 'w')
    length = len(all_formatted_dates)
    for i in range(length):
        file.write(str(i+1) + ') ')
        file.write(all_formatted_dates[i])
        file.write("\n")
    file.close()

    return all_formatted_dates

def format_mdy(m):
    """ Function that format MDY date to format YEAR/MONTH/DAY

    :param m: String to format.

    :return: Formatted String.
    """

    mdy_date = re.split(', | ', m.group())
    month = mdy_date[0]
    mdy_date[0] = Month[month].value # convert month name to month number

    format_mdy_date = "{}/{}/{}".format(mdy_date[2], mdy_date[1], mdy_date[0])

    return format_mdy_date

def format_dmy(m):
    """ Function that format DMY date to format YEAR/MONTH/DAY

    :param m: String to format.

    :return: Formatted String.
    """

    dmy_date = re.split(' ', m.group())
    month = dmy_date[1]
    dmy_date[1] = Month[month].value # convert month name to month number

    format_mdy_date = "{}/{}/{}".format(dmy_date[2], dmy_date[1], dmy_date[0])

    return format_mdy_date

def format_ymd(m):
    """ Function that format YMD date to format YEAR/MONTH/DAY

    :param m: String to format.

    :return: Formatted String.
    """

    ymd_date = re.split(' ', m.group())
    month = ymd_date[1]
    ymd_date[1] = Month[month].value # convert month name to month number

    format_ymd_date = "{}/{}/{}".format(ymd_date[0], ymd_date[1], ymd_date[2])

    return format_ymd_date

def format_mdy_dmy_short_dates(m):
    """ Function that format short MDY/DMY date to format YEAR/MONTH

    :param m: String to format.

    :return: Formatted String.
    """

    mdy_dmy_short_date = re.split(', | ', m.group())
    month = mdy_dmy_short_date[0]
    mdy_dmy_short_date[0] = Month[month].value # convert month name to month number

    format_mdy_dmy_short_date = "{}/{}".format(mdy_dmy_short_date[1], mdy_dmy_short_date[0])

    return format_mdy_dmy_short_date


if __name__ == "__main__":
    source_code1 = get_html("https://en.wikipedia.org/wiki/Linus_Pauling")
    source_code2 = get_html("https://en.wikipedia.org/wiki/Rafael_Nadal")
    source_code3 = get_html("https://en.wikipedia.org/wiki/J._K._Rowling")
    source_code4 = get_html("https://en.wikipedia.org/wiki/Richard_Feynman")
    source_code5 = get_html("https://en.wikipedia.org/wiki/Hans_Rosling")

    find_dates(source_code1, "output_dates_Linus_Pauling")
    find_dates(source_code2, "output_dates_Rafael_Nadal")
    find_dates(source_code3, "output_dates_J_K_Rowling")
    find_dates(source_code4, "output_dates_Richard_Feynman")
    find_dates(source_code5, "output_dates_Hans_Rosling")

