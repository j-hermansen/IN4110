import os
import re

from bs4 import BeautifulSoup

from requesting_urls import get_html


def extract_events(url, output='betting_slip_empty'):
    """ Function to get ski events, and create an betting slip for all the races.

     Regex used in this function:
        ([0123]?[0-9] [A-Z][a-z]{2,8} [0-9]{4})         Find dates in DMY format.
                                                        DMY format: 13 October 2020

        ([DSGAP][HLSGC])                                Type of race.
                                                        Types: GS | SL | DH | SG | PG | AC




    :param url (str):       The url to send get-request to.
    :param output (str):    Name of output txt file.
    """

    html_content = get_html(url)

    soup = BeautifulSoup(html_content[1], "html.parser")  # html content is as index 1 (url on index 0)
    soup_table = soup.find('table', {"class": 'wikitable plainrowheaders'})
    soup_table_rows = soup_table.findAll('tr')

    events = []

    dmy_regex = '([0123]?[0-9] [A-Z][a-z]{2,8} [0-9]{4})'
    type_regex = '([DSGAP][HLSGC])'

    venue = ""

    # Search each row in table (tr)
    for i in range(len(soup_table_rows)):
        soup_table_row = soup_table_rows[i].findAll('td')  # gets rows with relevant data, e.g. td-tags

        # Search each cell in row (td)
        for j in range(len(soup_table_row)):

            cell = soup_table_row[j]

            # Check if current cell is a date
            is_date = re.search(dmy_regex, cell.getText())

            if is_date is not None:
                event = []
                event.append(is_date.group(0))

                next_cell = soup_table_row[j + 1]

                # Check if next cell (after date) is type (if previous rows is using rowspan > 1)
                is_type = re.match(type_regex, next_cell.getText())

                if is_type is None:

                    # Get a-element that contains Venue
                    a_element = next_cell.findAll('a', recursive=False)

                    venue = a_element[0].text
                    type = re.match(type_regex, soup_table_row[j + 2].getText()).group(0)

                    event.append(venue)
                    event.append(type)

                else:

                    # Set Venue from last row, that spans multiple rows
                    event.append(venue)
                    event.append(is_type.group(0))

                events.append(event)


    # Create betting slip
    if not os.path.exists('datetime_filter'):
        os.makedirs('datetime_filter')

    betting_slip_file = open('datetime_filter/{}.md'.format(output), 'w', encoding='utf-8')

    betting_slip_file.write('BETTING SLIP\n\n')
    betting_slip_file.write('Name: \n\n')

    betting_slip_file.write('|DATE|VANUE|DISCIPLINE|Who Wins?|\n')
    betting_slip_file.write('|-----|-----|-----|-----|\n')

    for event in events:
        betting_slip_file.write('|{}|{}|{}||\n'.format(event[0], event[1], event[2]))

    betting_slip_file.close()


if __name__ == "__main__":
    extract_events("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup", "betting_slip_2019-20_empty")
    extract_events("https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup", "betting_slip_2020-21_empty")