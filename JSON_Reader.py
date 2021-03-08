import json
import pdb
import datetime
import requests

url = "https://gist.githubusercontent.com/jfmyers/16f784e4add6410aff8f2e3c54d4a12a/raw" \
      "/4f0a906cf9b496c749ad32d95be2d6a6fe70cee3/json"

# Dictionary to store desired info

output = []

response = requests.get(url)

d = response.json()

data = d['data'][0]
status = d["status"]
transactions = data["transactions"]
timestamp = data["timestamp"]

for idx, dic in enumerate(transactions):
    print("At current idx {}".format(idx))
    # Create a new empty dictionary entry
    d = {}
    # Formatting the blockTime
    dt = datetime.datetime.fromtimestamp(timestamp)
    yr = dt.strftime("%Y")
    month = dt.strftime("%m")
    day = dt.strftime("%d")
    hr = dt.strftime("%H")
    min = dt.strftime("%M")
    sec = dt.strftime("%S")

    fmt_time = "{}-{}-{}T{}:{}:{}Z".format(yr, month, day, hr, min, sec)
    print("timestamp:".format(timestamp))

    # adding block ID to d
    block_id = dic["block_number"]
    d["block_id"] = block_id

    # Adding timestamp to d
    d["timestamp"] = fmt_time
    print("block_id: {}".format(block_id))

    # check if logs is empty
    try:
        tx_hash = dic["receipt"]["logs"][0]["transactionHash"]
        d["tx_hash"] = tx_hash
        print("tx_hash: {}".format(tx_hash))

        # address
        address = dic["receipt"]["logs"][0]["address"]
        print("address: {}".format(address))
        d["address"] = address

    except IndexError:
        d['tx_hash'] = None

    # append d onto output
    output.append(d)



with open("output.json", "w") as json_file:
    jsn = json.dumps(output, indent=4)
    json_file.write(jsn)