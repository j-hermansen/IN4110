# Assignment 6

This assignment was about adding more functionality to same script throughout all subtasks. The script in this assignment
will plot covid data for Norway, and all counties separately. 

This script is developed in Python 3.8.

To run this script, the following packages are required:
- pandas
- altair
- flask
- beautifulsoup4

Install packages:
```python
pip install pandas altair flask beautifulsoup4
```

To run the script:
```python
py web_visualization.py
```
When runned the script has the following endpoints:

| path | explanation | methods |
| ---- | ----------- | ------- |
| `/plot` | shows the main page with plots and a form.| POST, GET |
| `/help` | the documentation page.| GET |
| `/map` | shows an interactive map.| GET |

Type http://127.0.0.1:5000/plot to visit main page. 
This will show reported and cumulative cases of covid-19 for all counties. To show for a specific county, select county in
the form, and choose between daily and weekly data. You can also select from and to dates, to show data for a specific period - 
the default is all data from .csv file.

At the bottom om the main page it is links to the interactive map (`/map`) and the documentation page (`/help`).

