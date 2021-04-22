import os
import re

import requests as req


def get_html(url, params=None, output=None):
    """ Function that sends get-request to url specified.

    :param url (str):       The url to send get-request to.
    :param params (dict):   Params to be passed with url.
    :param output (str):    Name of output txt file.

    :return:
        output is not None: No return, writes to txt-file with name specified from output parameter.
        output is None:     List with base url of requested url at index 0, and html content of page at index 1.

                            Example returned list:
                                request[0] = 'https://en.wikipedia.org/wiki/Studio_Ghibli'
                                request[1] = '<!DOCTYPE html><html> ..... </body></html>'

    """

    if params is not None:
        response = req.get(url, params=params)  # get-request with params
    else:
        response = req.get(url)  # get-request without params

    if output is not None:
        if not os.path.exists('requesting_urls'):
            os.makedirs('requesting_urls')

        output_file = open("requesting_urls/{}.txt".format(output), 'w')
        output_file.write("URL:\n")
        output_file.write("-------------------------\n")
        output_file.write(response.url)
        output_file.write("\n\nHTML:\n")
        output_file.write("-------------------------\n")
        output_file.write(response.text.encode('utf8').decode('ascii', 'ignore'))
        output_file.close()
    else:
        base_url = re.match('http.+\.[a-z]{2,3}', response.url).group()
        site = [base_url, response.text]

        return site

# Runned with these urls that was specified in subtask 5.1
if __name__ == '__main__':
    get_html("https://en.wikipedia.org/wiki/Studio_Ghibli", output="studio_ghibli_output")
    get_html("https://en.wikipedia.org/wiki/Star_Wars", output="star_wars_output")
    get_html("https://en.wikipedia.org/wiki/Dungeons_%26_Dragons", output="dungeons_dragons_output")
    get_html("https://en.wikipedia.org/w/index.php", {'title': 'Main_Page', 'action': 'info'}, "main_page_output")
    get_html("https://en.wikipedia.org/w/index.php", {'title': 'Hurricane_Gonzalo', 'oldid': '983056166'},
             "hurricane_gonzalo_output")
