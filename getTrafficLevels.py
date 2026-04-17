import retrieveOuluData
"""
Retireves traffic data from relevant example routes (see exampleroute.png) stations
starting from 01.01.2022.
Retireves daily, weekly and monthly counts.
"""

if __name__ == "__main__":
    query = """
    query GetRelevantStations {
        raatti_1: ecoCounterSiteData(id: "raatti_1", domain: Oulu_Kapy, step: STEP, begin: "2022-01-01T00:00:00") {
            date
            counts
        }
        raatti_2: ecoCounterSiteData(id: "raatti_2", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        raatti_3: ecoCounterSiteData(id: "raatti_3", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        raatti_4: ecoCounterSiteData(id: "raatti_4", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        pikisaarensilta_1: ecoCounterSiteData(id: "pikisaarensilta_1", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        pikisaarensilta_2: ecoCounterSiteData(id: "pikisaarensilta_2", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        pikisaarensilta_3: ecoCounterSiteData(id: "pikisaarensilta_3", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        pikisaarensilta_4: ecoCounterSiteData(id: "pikisaarensilta_4", domain: Oulu_Kapy, step: STEP, begin: "2019-01-01T00:00:00") {
            date
            counts
        }
        }
    """
    filenames = ["trafficDaily", "trafficWeekly", "trafficMothly"]
    i = 0
    for step in ["day", "week", "month"]:
        retrieveOuluData.retrieve_data(query.replace("STEP", step), filenames[i])
        i += 1