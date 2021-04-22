import os
import re

from requesting_urls import get_html

def find_urls(html, output=None, base_url=None):
    """ Function find all urls inside anchor-elements in html content.

    Regex used in this function:
        <a.*href=\".*\".*>                      Finds anchor-tags in html content.
        (?<=href=\")[/h].+?(?=[\"#])            Finds urls inside href-attribute in anchor-tags.
                                                Using look-behind and look-ahead to not include href="".
        https?:\/\/[a-z]{2}\.wikipedia\..+      Finds all urls that are articles in any language.


    :param html (str):      The html source code to look for urls.
    :param output (str):    Output filename.
    :param base_url (str):  Base url for html content.

    :return: Urls found in html content.
    """

    a_elements = re.findall("<a.*href=\".*\".*>", html)
    urls = re.findall("(?<=href=\")[/h].+?(?=[\"#])", "\n".join(a_elements))

    # Adds base_url to relative paths
    if base_url:
        for i in range(len(urls)):
            if urls[i][0] == "/" and urls[i][1] == "/":
                try:
                    protocol = base_url.index("/", 0, 7) # throws ValueError if string is not found
                    urls[i] = "{}{}".format(base_url[0:protocol], urls[i])
                except ValueError:
                    print("not found")
            elif urls[i][0] == "/":
                urls[i] = "{}{}".format(base_url, urls[i])

    if output is not None:

        # Write to file
        if not os.path.exists('filter_urls'):
            os.makedirs('filter_urls')

        file = open("filter_urls/{}.txt".format(output), 'w', encoding='utf-8')
        file.write("Url's in source code:\n")
        file.write("---------------------\n")
        file.write("\n".join(urls))

        articles = find_articles(urls)

        file.write("\n\n\n\n")
        file.write("Articles's in source code:\n")
        file.write("---------------------\n")
        file.write("\n".join(articles))

        file.close()
    else:
        return urls


def find_articles(urls, language='all'):

    # Assume that articles are with url path '/wiki/', and without ':'
    if language == 'all':
        return re.findall(r'^https?:\/\/[a-z]{2}\.wikipedia\.[a-z]{2,3}/wiki/[^:]+$', "\n".join(urls), flags=re.MULTILINE)
    else:
        return re.findall(r'^https?:\/\/' + language + '\.wikipedia\.[a-z]{2,3}/wiki/[^:]+$', "\n".join(urls),flags=re.MULTILINE)


if __name__ == '__main__':
    source_code1 = get_html("https://en.wikipedia.org/wiki/Nobel_Prize")
    source_code2 = get_html("https://en.wikipedia.org/wiki/Bundesliga")
    source_code3 = get_html("https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski")

    find_urls(source_code1[1], output="output_urls_Nobel_Prize", base_url=source_code1[0])
    find_urls(source_code2[1], output="output_urls_Bundesliga", base_url=source_code2[0])
    find_urls(source_code3[1], output="output_urls_FIS_Alpine_Ski", base_url=source_code3[0])
