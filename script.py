import requests
import json

def strava_activities_to_csv():

    # See steps in readme.md for the steps to get a bearer token
    token = "<<Your bearer token>>"

    # selected columns, more columns can be added when required
    columns = ["name","distance","moving_time","elapsed_time","total_elevation_gain","type","workout_type","start_date_local","visibility","average_speed","max_speed","average_heartrate","max_heartrate"]
    
    # create header as first row of csv
    separator = '|'
    datacsv = separator.join(columns)

    page=1
    while True:
        # retrieve array with next 100 activities from Strava
        stravaActivities = get_strava_activities(page, token)
        if stravaActivities == None:
            break

        # get all data from single activity and create csv record
        for activitiy in stravaActivities:
            datacsv += "\n"
            for column in columns:
                if column in activitiy:
                    datacsv += str(activitiy[column]).replace(separator, ' ') + str(separator)
                else:
                    datacsv += " " + str(separator)
            datacsv = datacsv[:-1]
        print("page %s retrieved and processed" % (page))

        # increment page number to retrieve next batch of activities
        page +=1

    # Finally, write csv file to your local disk
    with open("stava_activities_csv.csv", "w") as outfile:
        outfile.write(datacsv)

def get_strava_activities(page, token):

    # Retrieve activities from Strava using REST, 100 activities per call
    response = requests.get(
            'https://www.strava.com/api/v3/athlete/activities?page=%s&per_page=%s' % (page, 100),
            headers={'Authorization': "Bearer " + token}
    )
    # Check if no errors occurred
    if response.status_code != 200:
        print("Error retrieving Strava activities. %s:  %s" % (response.json()["message"], response.json()["errors"]))
        return None

    # Check if no empty array is returned
    if response.json() == []:
        if page == 1:
            print("No data to be retrieved")
        else:
            print("All data retrieved")          
        return None

    # Return array
    return response.json()

if __name__ == "__main__":
    strava_activities_to_csv()