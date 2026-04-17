import retrieveOuluData
import json
"""
Retireves traffic data from relevant example routes (see exampleroute.png) stations
starting from 01.01.2022.
Retireves daily, weekly and monthly counts.
"""

if __name__ == "__main__":

    filenames = ["trafficDaily", "trafficWeekly", "trafficMonthly"]
    stationId = ["raatti_", "pikisaarensilta_"]
    stationNumber = ["1", "2", "3", "4"]

    time = ["day", "week", "month"]

    for filename, step in zip(filenames, time):
        for station in stationId:
            for number in stationNumber:
                query = """
                    query GetRelevantStations {
                        ecoCounterSiteData(id: "STATIONID", domain: Oulu_Kapy, step: STEP, begin: "2022-01-01T00:00:00") {
                            date
                            counts
                        }
                    }
                    """
                query = query.replace("STATIONID", station + number)
                query = query.replace("STEP", step)
                result = retrieveOuluData.retrieve_data(query, "ecoCounterSiteData")
                for record in result:
                    record["station_id"] = station + number
                with open(filename + "_" + station + number + ".json", "w") as file:
                    json.dump(result, file, indent=2)
                