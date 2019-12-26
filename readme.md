## Python script to download all your Strava activities to a local csv file ##

### Steps to be executed to get token needed to retrieve your data : ###

1. Go to https://www.strava.com/settings/api, create a new app, make sure you use "developers.strava.com" as callback URI
2. Go to https://developers.strava.com/playground/, click authorize
3. Fill in the client_id and client_secret of the app you just created. Make sure that "activity:read_all" is checked and then authorize. Then a popup windows appears that shall be accepted.
4. Go to /athlete/activities in the playground environment, click "Try it out" and then Execute. Copy bearer token from the playground environment (see screenshot below).
5. Clone this repository, fill in the bearer token in strava_activities_csv.py
6. Install [python](https://www.python.org/downloads/), open python command line and then run `python strava_activities_csv.py`. A strava_activities_csv.csv file will be created with your data that can be opened in Excel

Playground with bearer token is depicted below.

![Bearer token](https://github.com/rebremer/strava-to-excel/blob/master/images/strava_bearer_token.png "Bearer Token")

End result in which Strava data can be viewed in Excel

![Strava activities in Excel](https://github.com/rebremer/strava-to-excel/blob/master/images/strava_activities_excel.png "Strava activities in Excel")