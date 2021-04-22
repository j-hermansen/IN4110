
import pandas as pd
import altair as alt
import datetime

from flask import Flask, request
from flask import render_template
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='/', static_folder='docs/_build/html/')  # static folder to render documentations index.html


def plot_reported_cases(from_date, to_date, time, county='all_counties'):
    """ Plotting a bar plot (using Altair) of reported covid cases in selected county.

    :param from_date: date to start plotting from.
    :param to_date: date to end plotting data.
    :param time: define time frame (daily/weekly)
    :param county: define county to plot from.

    :return: a bar plot of selected county, time, and time frame.
    """

    if time == 'daily':
        covid_data = pd.read_csv('resources/' + county + '.csv', sep=';')

        # convert Dato to datetime
        covid_data['Dato'] = pd.to_datetime(covid_data['Dato'])
    else:
        covid_data = pd.read_csv('resources/' + county + '_week.csv', sep=';')

        if str(from_date) != 'NaT':
            from_date = pd.to_datetime(from_date.strftime('%Y-%W-1'), format='%Y-%W-%w')
            to_date = pd.to_datetime(to_date.strftime('%Y-%W-1'), format='%Y-%W-%w')

        # convert Dato to datetime
        covid_data['Dato'] = pd.to_datetime(covid_data['Dato'] + '-1', format='%Y-%W-%w')

    if from_date is not None and to_date is not None:
        if str(from_date) != 'NaT' and str(to_date) != 'NaT':
            # find dates between start_date and end_date
            mask = (covid_data['Dato'] > from_date) & (covid_data['Dato'] <= to_date)

            # get only rows with date in range
            covid_data = covid_data.loc[mask]

    covid_chart = alt.Chart(covid_data).mark_bar(size=10).encode(
        x=alt.X('Dato:T', axis=alt.Axis(format="%d-%b-%Y", labelOverlap=False, labelAngle=-45)),
        y='Nye tilfeller',
        tooltip=['Dato', 'Nye tilfeller']
    )

    return covid_chart


def plot_cumulative_cases(from_date, to_date, time, county='all_counties'):
    """ Plotting a line plot (using Altair) of cumulative covid cases in selected county.

    :param from_date: date to start plotting from.
    :param to_date: date to end plotting data.
    :param time: define time frame (daily/weekly)
    :param county: define county to plot from.

    :return: a line plot of selected county, time, and time frame.
    """

    if time == 'daily':
        covid_data = pd.read_csv('resources/' + county + '.csv', sep=';')

        # convert Dato to datetime
        covid_data['Dato'] = pd.to_datetime(covid_data['Dato'])
    else:
        covid_data = pd.read_csv('resources/' + county + '_week.csv', sep=';')

        if str(from_date) != 'NaT':
            from_date = pd.to_datetime(from_date.strftime('%Y-%W-1'), format='%Y-%W-%w')
            to_date = pd.to_datetime(to_date.strftime('%Y-%W-1'), format='%Y-%W-%w')

        # convert Dato to datetime
        covid_data['Dato'] = pd.to_datetime(covid_data['Dato'] + '-1', format='%Y-%W-%w')

    if from_date is not None and to_date is not None:
        if str(from_date) != 'NaT' and str(to_date) != 'NaT':
            # find dates between start_date and end_date
            mask = (covid_data['Dato'] > from_date) & (covid_data['Dato'] <= to_date)

            # get only rows with date in range
            covid_data = covid_data.loc[mask]

    covid_chart = alt.Chart(covid_data).mark_line().encode(
        x='Dato:T',
        y='Kumulativt antall',
        tooltip=['Dato', 'Kumulativt antall']
    )

    return covid_chart

@app.route("/plot", methods=['POST', 'GET'])
def plot_both(county='all_counties'):
    """ Plotting a line plots (using Altair) of cumulative and reported covid cases in selected county.

    This function is executed when url with /plot is called. It also reads
    from and to dates, so that user can select the period that are beeing plotted.

    :param county: the county to plot.

    :return: the html file showing all plots.
    """

    global covid_data, from_date, to_date

    counties = ['all_counties', 'agder', 'innlandet', 'more-romsdal', 'nordland', 'oslo', 'rogaland', 'troms-finnmark', 'trondelag', 'vestfold-telemark', 'vestland', 'viken']
    times = ['daily', 'weekly']
    time_frame = 'daily'

    if request.method == 'POST':
        time_frame = request.form.getlist('time_select')[0]
        county = request.form['county']

        from_date = pd.to_datetime(request.form.get('from_date_pick'))
        to_date = pd.to_datetime(request.form.get('to_date_pick'))
        if time_frame == 'daily':
            covid_data = pd.read_csv('resources/' + county + '.csv', sep=';')

            # convert Dato to datetime
            covid_data['Dato'] = pd.to_datetime(covid_data['Dato'])
        else:
            covid_data = pd.read_csv('resources/' + county + '_week.csv', sep=';')

            if str(from_date) != 'NaT':
                from_date = pd.to_datetime(from_date.strftime('%Y-%W-1'), format='%Y-%W-%w')
                to_date = pd.to_datetime(to_date.strftime('%Y-%W-1'), format='%Y-%W-%w')

            # convert Dato to datetime
            covid_data['Dato'] = pd.to_datetime(covid_data['Dato'] + '-1', format='%Y-%W-%w')

    else:
        covid_data = pd.read_csv('resources/' + county + '.csv', sep=';')
        from_date = pd.to_datetime(request.form.get('from_date_pick'))
        to_date = pd.to_datetime(request.form.get('to_date_pick'))

        # convert Dato to datetime
        covid_data['Dato'] = pd.to_datetime(covid_data['Dato'])

    if from_date is not None and to_date is not None:
        if str(from_date) != 'NaT' and str(to_date) != 'NaT':

            # find dates between start_date and end_date
            mask = (covid_data['Dato'] > from_date) & (covid_data['Dato'] <= to_date)

            # get only rows with date in range
            covid_data = covid_data.loc[mask]

    base = alt.Chart(covid_data).encode(
        alt.X('Dato:T', axis=alt.Axis(title=None))
    )

    cumulative = base.mark_line(stroke='#FF5733', interpolate='monotone').encode(
        alt.Y('Kumulativt antall', axis=alt.Axis(title='Kumulative', titleColor='#FF5733'))
    )

    reported = base.mark_line(stroke='#5DADE2', interpolate='monotone').encode(
        alt.Y('Nye tilfeller', axis=alt.Axis(title='Nye tilfeller', titleColor='#5DADE2'))
    )

    cumulative_and_reported = alt.layer(cumulative, reported).resolve_scale(
        y = 'independent'
    )

    cumulative_cases = plot_cumulative_cases(from_date, to_date, time=time_frame, county=county)
    reported_cases = plot_reported_cases(from_date, to_date, time=time_frame, county=county)

    all = cumulative_and_reported | cumulative_cases | reported_cases

    all.save("templates/cumulative_and_reported.html")

    soup = BeautifulSoup(open("templates/cumulative_and_reported.html"), 'html.parser')

    head = soup.find('head')
    body = soup.find('body')
    script = soup.find('body').find('script')

    if from_date is not None:
        from_date = from_date.date()
        to_date = to_date.date()



    return render_template('plotting.html',
                           head=head,
                           body=body,
                           script=script,
                           from_date=from_date,
                           to_date=to_date,
                           current_county=county,
                           current_time=time_frame,
                           counties=counties,
                           times=times)


@app.route("/help")
def help_page():
    """ Function to render main documentation html page.

    :return: the html file showing documentation.
    """

    return app.send_static_file("index.html")

@app.route("/map")
def plot_norway():
    """ Makes a interactive geomap of norway with number of cases per 100k in every county.

    :return: the html file showing interactive geomap.
    """

    data = pd.read_csv("resources/covid_rate_per_100000.csv", sep=';', index_col=False)
    county_list = data["Category"].to_list()
    insidens_list = [float(i.replace(',', '.')) for i in data["Insidens"].to_list()]

    data_as_dict = {"Category": county_list, "Insidens":  insidens_list}
    df = pd.DataFrame.from_dict(data_as_dict)

    counties = alt.topo_feature("https://raw.githubusercontent.com/deldersveld/topojson/master/countries/norway/norway-new-counties.json", "Fylker")

    nearest = alt.selection(type="single", on="mouseover", fields=["properties.navn"], empty="none")

    fig = alt.Chart(counties).mark_geoshape().encode(
        tooltip=[
            alt.Tooltip("properties.navn:N", title="County"),
            alt.Tooltip("Insidens:Q", title="Cases per 100k capita"),
        ],
        color=alt.Color("Insidens:Q", scale=alt.Scale(scheme="reds"),
                        legend=alt.Legend(title="Cases per 100k capita")),
        stroke=alt.condition(nearest, alt.value("gray"), alt.value(None)),
        opacity=alt.condition(nearest, alt.value(1), alt.value(0.8)),

    ).transform_lookup(
        lookup="properties.navn",
        from_=alt.LookupData(df, "Category", ["Insidens"])
    ).properties(
        width=700,
        height=800,
        title="Number of cases per 100k in every county",
    ).add_selection(
        nearest
    )

    fig.save("templates/interactive_map.html")

    soup = BeautifulSoup(open("templates/interactive_map.html"), 'html.parser')

    head = soup.find('head')
    body = soup.find('body')
    script = soup.find('body').find('script')

    return render_template("map.html",
                           head=head,
                           body=body,
                           script=script,
                           from_date=from_date,
                           to_date=to_date,
                       )


if __name__ == '__main__':
    app.run()
