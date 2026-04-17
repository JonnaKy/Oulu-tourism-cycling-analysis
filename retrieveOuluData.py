import urllib.request
import json
import config


def retrieve_data(query: str,  filename: str, resultname: str = None):
    """
    Function to retrives data from oulunliikenne.fi graphQL api
    https://wp.oulunliikenne.fi/avoin-data/pyorailykavely/graphql-rajapinnat/
    Creates a json file from created data. See above documentation for more information
    ...
    resultname: Optional. The top-level field name to extract from the response data.
                Only needed when the query contains a single, non-alaised field.
                If omitted, the entire data objects is saved.
    """
    data = json.dumps({"query" : query}).encode("utf-8")
    req = urllib.request.Request(
        config.valuesForQuerying.get("URL"),
        data=data,
        headers={"Content-Type":"application/json"}
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

    content = result["data"][resultname] if resultname else result["data"]

    with open(filename + ".json", "w") as file:
        json.dump(content, file, indent=2)