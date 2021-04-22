# Assignment 5

This assignment was created using Python 3.8.



## Subtask 5.1 | Sending url requests

Packages required for this subtask
* requests: `pip install requests`

This subtask consist of `requesting_urls.py` script, with the following functions:
* get_html(url, params, output)

Run script with the command:
```python
py requestion_urls.py
```

After running the script, **5 files** should appear inside **requesting_urls** folder, with the url and contents of the requested url's.

The **get_html()** are by default called when script are runned. *params* and *output* parameters are optional.
See more about the arguments passed to **get_html()** inside `requesting_urls.py`, at the bottom of the script.

Script are by defualt runned with these url's:
* https://en.wikipedia.org/wiki/Studio_Ghibli
* https://en.wikipedia.org/wiki/Star_Wars
* https://en.wikipedia.org/wiki/Dungeons_%26_Dragons
* https://en.wikipedia.org/w/index.php?title=Main_Page&action=info
* https://en.wikipedia.org/w/index.php?title=Hurricane_Gonzalo&oldid=983056166

Output files should be:

* requesting_urls/studio_ghibli_output.txt
* requesting_urls/star_wars_output.txt
* requesting_urls/dungeons_dragons_output.txt
* requesting_urls/main_page_output.txt
* requesting_urls/hurricane_gonzalo_output.txt



## Subtask 5.2 | Regex for filtering URLs

Packages required for this subtask
* requests: `pip install requests`

This subtask consist of `filter_urls.py` script, with the following functions:
* find_urls(html, output, base_urls)
* find_articles(urls)

Run script with the command:
```python
py filter_urls.py
```

After running the script, **3 files** should appear inside **filter_urls** folder, with all urls and articles found in requested url.

The **find_urls()** are by default called when script are runned, this function calls **find_articles()** to get all the articles out of all the urls.
To first get the contents of a webpage, the **get_html()** are called from subtask 5.1.
See more about the arguments passed to **find_urls()** inside `filter_urls.py`, at the bottom of the script.

Script are by defualt runned with these url's:
* https://en.wikipedia.org/wiki/Nobel_Prize
* https://en.wikipedia.org/wiki/Bundesliga
* https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski

Output files should be:
* filter_urls/output_urls_Nobel_Prize.txt
* filter_urls/output_urls_Bundesliga.txt
* filter_urls/output_urls_FIS_Alpine_Ski.txt



## Subtask 5.3 | Regular Expressions for finding Dates

Packages required for this subtask
* requests: `pip install requests`

This subtask consist of `collect_dates.py` script, with the following functions:
* find_dates(html, output)
* format_mdy(m)
* format_dmy(m)
* format_ymd(m)
* format_mdy_dmy_short_dates(m)

Run script with the command:
```python
py collect_dates.py
```

After running the script, **5 files** should appear inside **filter_dates_regex** folder, with all formatted dates found in html content.

The **find_dates()** are by default called when script are runned, this function calls **format_mdy()**, **format_dmy()**, **format_ymd()**, **format_mdy_dmy_short_dates()** to format all the data formats.
To first get the contents of a webpage, the **get_html()** are called from subtask 5.1.
See more about the arguments passed to **find_dates()** inside `collect_dates.py`, at the bottom of the script.

Script are by defualt runned with these url's:
* https://en.wikipedia.org/wiki/Linus_Pauling
* https://en.wikipedia.org/wiki/Rafael_Nadal
* https://en.wikipedia.org/wiki/J._K._Rowling
* https://en.wikipedia.org/wiki/Richard_Feynman
* https://en.wikipedia.org/wiki/Hans_Rosling

Output files should be:
* filter_dates_regex/output_dates_Linus_Pauling.txt
* filter_dates_regex/output_dates_Rafael_Nadal.txt
* filter_dates_regex/output_dates_J_K_Rowling.txt
* filter_dates_regex/output_dates_Richard_Feynman.txt
* filter_dates_regex/output_dates_Hans_Rosling.txt



## Subtask 5.4 | Making your Life easier with Soup for filtering datetime objects

Packages required for this subtask
* requests: `pip install requests`
* BeautifulSoup: `pip install beautifulsoup4`

This subtask consist of `time_planner.py` script, with the following functions:
* extract_events(html, output)

Run script with the command:
```python
py time_planner.py
```

After running the script, **2 files** should appear inside **datetime_filter** folder, with betting slips season 2019-20 and 2020-21.

The **extract_events()** are by default called when script are runned, this function calls **get_html()** from subtask 5.1 to get html content of website.
See more about the arguments passed to **extract_events()** inside `time_planner.py`, at the bottom of the script.

Script are by defualt runned with these url's:
* https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup
* https://en.wikipedia.org/wiki/2020%E2%80%9321_FIS_Alpine_Ski_World_Cup

Output files should be:
* datetime_filter/betting_slip_2019-20_empty.md
* datetime_filter/betting_slip_2020-21_empty.md



## Subtask 5.5 | Making your Life easier with Soup for filtering datetime objects

Packages required for this subtask
* requests: `pip install requests`
* BeautifulSoup: `pip install beautifulsoup4`

This subtask consist of `fetch_playerstatistics.py` script, with the following functions:
* extract_url(url)
* team_players(team)
* get_player_points(player)
* plot_top_players(top_players, per_game)

Run script with the command:
```python
py fetch_playerstatistics.py
```

After running the script, **3 images** should appear inside **NBA_player_statistics** folder, with plot of points per game, rebounds per game, and blocks per game,
for top 24 player (3 from each team) from conference semifinals in NBA 2020.


The **extract_url()** are by default called when script are runned, this function calls **get_html()** from subtask 5.1 to get html content of website.
Then it calls **team_players()** to get all player for a given team, **get_player_points()** to get score of players in season 2019-20, and **plot_top_players()** to plot
scores, and save as images.
See more about the arguments passed to **extract_url()** inside `fetch_playerstatistics.py`, at the bottom of the script.

Script are by defualt runned with these url's:
* https://en.wikipedia.org/wiki/2020_NBA_playoffs

Output files should be:
* NBA_player_statistics/players_over_ppg.png
* NBA_player_statistics/players_over_rpg.png
* NBA_player_statistics/players_over_bpg.png

## Subtask 5.6 | Wiki Race with URLs

Packages required for this subtask
* requests: `pip install requests`
* BeautifulSoup: `pip install beautifulsoup4`

This subtask consist of `wiki_race_challenge.py` script, with the following functions:
* shortest_path(start, end)
* result(start, end, path)

Run script with the command:
```python
py wiki_race_challenge.py
```
After running the script, **1 text file** should appear inside **wiki_race_challenge** folder, with information about the path taken from start url to end url.
In the text file it shows the urls in the shortest path.

Script are by defualt runned with these url's:
* start: https://en.wikipedia.org/wiki/Nobel_Prize
*   end: https://en.wikipedia.org/wiki/Natural_science

This is not an advance path, but is default so user can se result in txt-file after a short time. 
If you wish to try an more advanced part, change the **end** variable in en of `wiki_race_challenge.py` script.
I've also print the url's visited in console as the program goes.

Output files should be:
* wiki_race_challenge/shortest_path.txt
