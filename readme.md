## Python script to download all your Strava activities to a local csv file ##

The following resources are required to run script:
1. Bearer token to retrieve your data from Strava
2. Python 3.x to run script that creates csv file

### 1. Bearer token to retrieve your data from Strava ###

The following steps need to be executed:
- Go to https://www.strava.com/settings/api, create a new app, make sure you use "developers.strava.com" as callback URI
- Go to https://developers.strava.com/playground/, click authorize
- Fill in the client_id and client_secret of the app you just created. Make sure that "activity:read_all" is checked and then authorize. Then a popup windows appears that shall be accepted.
- Go to /athlete/activities in the playground environment, click "Try it out" and then Execute. Copy bearer token from the playground environment (see screenshot below).

![Bearer token](https://github.com/rebremer/strava-to-excel/blob/master/images/strava_bearer_token.png "Bearer Token")

### 2. Python 3.x to run script that creates csv file ###

The following steps need to be executed:
- Clone or download this repository, fill in the bearer token in strava_activities_csv.py
- Install [Python](https://www.python.org/downloads/). Open a terminal session and check that Python is correctly install by running `python --version` 
- Finally, run `python strava_activities_csv.py` that will downloads all your activities to a new csv file strava_activities_csv.csv that can be opened in Excel (see screenshot below)

![Strava activities in Excel](https://github.com/rebremer/strava-to-excel/blob/master/images/strava_activities_excel.png "Strava activities in Excel")