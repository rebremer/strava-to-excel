import requests
import json


def main():
    # See steps in readme.md for the steps to get a bearer token
    token = "<<Your bearer token>>"
    
    # Selected fields in Strava activitiy to be put as column in csv
    # More fields can be added, for field names refer to https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities
    columns = ["name","distance","moving_time","elapsed_time","total_elevation_gain","type","workout_type","start_date_local","visibility","average_speed","max_speed","average_heartrate","max_heartrate"]
    
    # Create header as first row of csv
    separator = '|'
    data_csv = separator.join(columns)
    page=1
    while True:
        # Retrieve array with next 100 activities from Strava. Break loop when no activities are returned
        activities = get_strava_activities(page, token)
        if activities == None:
            break
        
        # Get all data from single activity and create csv record
        for activity in activities:
            data_csv += "\n"
            for column in columns:
                if column in activity:
                    data_csv += str(activity[column]).replace(separator, ' ') + str(separator)
                else:
                    data_csv += " " + str(separator)
            data_csv = data_csv[:-1]
        print("page %s retrieved and processed" % (page))
        
        # Increment page number to retrieve next batch of activities
        page +=1
    
    # Finally, write csv file to your local disk
    with open("stava_activities_csv.csv", "w") as outfile:
        outfile.write(data_csv)


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
    main()