import urllib.request
import json
import config

def retrieve_stations():
    query = """
    query GetAllEcoCounterSites {
        ecoCounterSites {
            siteId
            name
            userType
            channels {
            siteId
            name
            lat
            lon
            }
        }
    }
    """
    data = json.dumps({"query" : query}).encode("utf-8")
    req = urllib.request.Request(
        config.valuesForQuerying.get("URL"),
        data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
    
    stations = result["data"]["ecoCounterSites"]

    with open("stations.json", "w") as file:
        json.dump(stations, file, indent=2)

if __name__ == "__main__":
    retrieve_stations()