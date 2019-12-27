import requests
import json


def main():
    # See readme.md how to get a bearer token
    token = "<<Your bearer token>>"
    
    # Selected fields in Strava activitiy to be put as column in csv
    # More fields can be added, for field names refer to https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities
    columns = ["name","distance","moving_time","elapsed_time","total_elevation_gain","type","workout_type","start_date_local","visibility","average_speed","max_speed","average_heartrate","max_heartrate"]
    
    # Create header as first row of csv
    delimiter = ',' # | or ; can be used as delimiter as well
    data_csv = delimiter.join(columns)

    # Process activities from Strava in batches (Strava limits number of activities to be downloaded at once)
    batch=1
    while True:
        # Retrieve batch with 100 activities from Strava. Break loop when no activities are returned
        activities = get_strava_activities(batch, token)
        if activities == None:
            break
        
        # Get all data from single activity and append csv record to data_csv. Repeat this for all 100 activities in batch
        for activity in activities:
            data_csv += "\n"
            for column in columns:
                if column in activity:
                    data_csv += str(activity[column]).replace(delimiter, ' ') + str(delimiter)
                else:
                    data_csv += " " + str(delimiter)
            data_csv = data_csv[:-1]
        print("Activities of batch %s processed" % (batch))
        
        # Increment batch number to retrieve next batch of 100 activities
        batch +=1
    
    # Finally, write data_csv as file to your local disk
    if batch > 1:
        print("Start writing data to stava_activities_csv.csv")
        with open("stava_activities_csv.csv", "w") as outfile:
            outfile.write(data_csv)
        print("Finished writing data to stava_activities_csv.csv")


def get_strava_activities(batch, token):
    # Retrieve activities from Strava using REST, 100 activities per call
    response = requests.get(
            'https://www.strava.com/api/v3/athlete/activities?page=%s&per_page=%s' % (batch, 100),
            headers={'Authorization': "Bearer " + token}
    )

    # Check if no errors occurred
    if response.status_code != 200:
        print("Error retrieving Strava activities. %s:  %s" % (response.json()["message"], response.json()["errors"]))
        return None

    # Check if no empty array is returned
    if response.json() == []:
        if batch == 1:
            print("No activities to be retrieved")
        else:
            print("All activities retrieved")          
        return None

    # Return array
    return response.json()


if __name__ == "__main__":
    main()