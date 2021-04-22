import os
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from requesting_urls import get_html
from bs4 import BeautifulSoup

def extract_url(url):
    """ Function that extracts urls for all teams in NBA conference semifinals.

    :param url (str):    The url to send get-request to.
    """

    html_content = get_html(url)

    # Get table in bracket section
    document = BeautifulSoup(html_content[1], 'html.parser')  # Parse html content at index 1 (url on index 0) from get_html()
    title = document.find(id="Bracket")                       # Find 'Bracket' section
    tables = title.find_all_next("table")                     # Find tables in 'Bracket' section
    bracket_table = tables[0]                                 # Get first table (Conference)

    # Extract teams that made it to the conference semifinals (4th column)
    # Rows 5, 7, 17, 19, 29, 31, 41, 43 (extracting 4th column of all rows could also select teams from 'Conference Finals')
    rows = []
    row = bracket_table.find_all("tr")

    rows.append(row[4])
    rows.append(row[6])
    rows.append(row[16])
    rows.append(row[18])
    rows.append(row[28])
    rows.append(row[30])
    rows.append(row[40])
    rows.append(row[42])

    teams_semifinals = []

    # Go through rows for conference semifinals
    for row in rows:
        cells = row.find_all("td")
        team_name = cells[3].get_text(strip=True)    # Team name is in 4th column
        team_name = re.sub(r'[^\w]', '', team_name)  # Remove unwanted symbols
        team_url = cells[3].a['href']                # Gets the team url from href-attribute

        team = [team_name, team_url]
        teams_semifinals.append(team)                # Add to multidim-list with teams that made it to conference semifinals

    top_players = []

    # Go through every team that made it to conference semifinals
    for team in teams_semifinals:
        team.append(team_players(team))  # Add all team players to the team as a list inside team list

        top_players_team = [['', '', 0, 0, 0], ['', '', 0, 0, 0], ['', '', 0, 0, 0]] # Should hold top team players (name, team, rpg, bpg, ppg)

        # Go through every player in team (team[2] is the list of players inside team list)
        for player in team[2]:
            player.append(get_player_points(player))  # Get player score for season 2019-20

            # Remove unwanted symbols
            player_points = re.sub(r'\*', '', str(player[2][2]))
            top_players_team[0][4] = re.sub(r'\*', '', str(top_players_team[0][4]))
            top_players_team[1][4] = re.sub(r'\*', '', str(top_players_team[1][4]))
            top_players_team[2][4] = re.sub(r'\*', '', str(top_players_team[2][4]))

            # Check if player is in top 3 at current team
            if float(player_points) > float(top_players_team[0][4]):  # Higher Points Per Game than first player
                top_players_team[2] = list(top_players_team[1])       # Place second player in third
                top_players_team[1] = list(top_players_team[0])       # Place first player in second

                top_players_team[0][0] = player[0]      # Set player name
                top_players_team[0][1] = team[0]        # Set player's team
                top_players_team[0][2] = player[2][0]   # Set rpg
                top_players_team[0][3] = player[2][1]   # Set bpg
                top_players_team[0][4] = player[2][2]   # Set ppg
            elif float(player_points) > float(top_players_team[1][4]):  # Higher Points Per Game than second player
                top_players_team[2] = list(top_players_team[1])         # Place second player in third

                top_players_team[1][0] = player[0]      # Set player name
                top_players_team[1][1] = team[0]        # Set player's team
                top_players_team[1][2] = player[2][0]   # Set rpg
                top_players_team[1][3] = player[2][1]   # Set bpg
                top_players_team[1][4] = player[2][2]   # Set ppg
            elif float(player_points) > float(top_players_team[2][4]):
                top_players_team[2][0] = player[0]      # Set player name
                top_players_team[2][1] = team[0]        # Set player's team
                top_players_team[2][2] = player[2][0]   # Set rpg
                top_players_team[2][3] = player[2][1]   # Set bpg
                top_players_team[2][4] = player[2][2]   # Set ppg

        top_players.append(top_players_team)

    # Create plot image for Points Per Game, Blocks Per Game, and Rebounds Per Game
    plot_top_players(top_players, 'ppg')
    plot_top_players(top_players, 'bpg')
    plot_top_players(top_players, 'rpg')


# Get all team players for that season (table: team roster)
def team_players(team_url):
    """ Function gets all player on a team.

    :param team_url (list): Team info [name, relative url].

    :return: All players on team.
    """

    # Get html
    html_content = get_html('https://en.wikipedia.org{}'.format(team_url[1]))

    document = BeautifulSoup(html_content[1], 'html.parser')  # Parse html content at index 1 (url on index 0) from get_html()
    player_table = document.find_all("table", class_='toccolours')[0].find("table")  # Gets inner table containing players of 2019-20 team table

    rows = player_table.find_all("tr")

    players = []

    # Go through each row except first (th-tags)
    for row in rows[1:]:
        cells = row.find_all("td")
        player_name = cells[2].get_text(strip=True)
        player_url = cells[2].a['href']

        player = [player_name, player_url]

        players.append(player)

    return players

def get_player_points(player_url):
    """ Function that gets player stats for Rebounds Per Game, Blocks Per Game, and Points Per Game, for last season.

    :param player_url (list): Player info [name, relative url].

    :return: Player stats (rpg, bpg, and ppg) for last season.
    """

    # Get html
    html_content = get_html('https://en.wikipedia.org{}'.format(player_url[1]))

    # Get table of NBA regular season
    document = BeautifulSoup(html_content[1], 'html.parser')
    regular_season_section = document.find('span', id='Regular_season')  # Find section for 'Regular season'
    if regular_season_section is None:                                   # Some player sites do not include span with id 'Regular_season'
        regular_season_section = document.find('span', id='NBA')         # Instead, find section for 'NBA'

        if regular_season_section is None:  # Return if no section for a season in NBA was found
            return [0, 0, 0]                # Return zero list

    table = regular_season_section.find_next('table').tbody  # Get the tbody section of table, where the player seasons are

    rows = table.find_all("tr")

    last_season = ''

    # Go through each season
    for row in rows:

        cells = row.find_all(["td", "th"])
        cells_text = [cell.get_text(strip=True) for cell in cells]

        # Get year 2019-20
        if re.match('2019[^\w]20',
                    str(cells_text[0])):  # No match with regular '-' symbol in 2019-20, so checked with regex
            last_season = cells_text      # Save season 2019-20
            break

    # Get players rpg, bpg, and ppg, for last season (2019-20), or set to zeros if no score are presented.
    if last_season != '':
        rpg = last_season[8]
        bpg = last_season[11]
        ppg = last_season[12]
        player_stats = [rpg, bpg, ppg]
    else:
        player_stats = [0, 0, 0]

    return player_stats


def plot_top_players(top_players, per_game):
    """ Function thats plots stats (rpg, bpg, and ppg) for top 3 player of each team.

    :param top_players (list): List of top players with [name, team, rpg, bpg, ppg]
    :param per_game (str):     Type of stat to plot (could be rpg, bpg, or ppg)
    """

    num = np.array(top_players)

    plt.figure(figsize=[17, 7])
    players = num[:, :, 0].flatten()  # Get all players as list

    info = ''

    #  Get score for given per_game argument passed to function (can be ppg, bpg, or rpg)
    if per_game == 'ppg':
        score = num[:, :, 4].flatten().astype(np.float)
        info = 'Point Per Game'
    elif per_game == 'bpg':
        score = num[:, :, 3].flatten().astype(np.float)
        info = 'Blocks Per Game'
    elif per_game == 'rpg':
        score = num[:, :, 2].flatten().astype(np.float)
        info = 'Rebounds Per Game'
    else:
        print('Unknown per game score type')
        return

    colors = ['green', 'red', 'yellow', 'blue', 'pink', 'purple', 'orange', 'lightblue']  # Colors for teams in plot

    color_counter = 0  # Should increase when new team gets plotted

    milwaukee = mpatches.Patch(color='green', label='Milwaukee')
    miami = mpatches.Patch(color='red', label='Miami')
    boston = mpatches.Patch(color='yellow', label='Boston')
    toronto = mpatches.Patch(color='blue', label='Toronto')
    la_lakers = mpatches.Patch(color='pink', label='LA Lakers')
    houston = mpatches.Patch(color='purple', label='Houston')
    denver = mpatches.Patch(color='orange', label='Denver')
    la_clippers = mpatches.Patch(color='lightblue', label='LA Clippers')

    # Plot player stats in horizontal bar
    for i in range(len(players)):
        if i > 0 and (i % 3 == 0):
            color_counter += 1
        plt.barh(players[i], score[i], color=colors[color_counter])

    plt.legend(handles=[milwaukee, miami, boston, toronto, la_lakers, houston, denver, la_clippers])  # Show color-labels of each team

    # Giving the title for the plot
    plt.title("Bar plot representing top players from NBA conference semi finals by {}".format(info))

    # Naming the x and y axis
    plt.xlabel(info)
    plt.ylabel('Top Players')

    # Saving the plot as a 'png'
    if not os.path.exists('NBA_player_statistics'):
        os.makedirs('NBA_player_statistics')

    plt.savefig('NBA_player_statistics/players_over_{}.png'.format(per_game))


if __name__ == '__main__':
    extract_url('https://en.wikipedia.org/wiki/2020_NBA_playoffs')
