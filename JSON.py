import os
import json
import csv



def json_export(file_path = "sales_data.csv", json_output_path = "retail_sales_data.json"):

    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

    try:
            with open(json_output_path, mode="w") as json_file:
                json.dump(data, json_file, indent=3)
            print(f"Data converted and saved as JSON to {json_output_path}")
    except Exception as e:
        print(f"Parsing Error while writing JSON: {e}")



