import json 
import requests
import random
import pprint
import csv

template_link = "https://monitoring.e-kassa.gov.az/pks-portal/1.0.0/documents/"

with open("fiscal_ids.txt", "r") as fiscal_ids:
    fiscal_id_list = fiscal_ids.readlines()
    fiscal_id_list = [i.strip() for i in fiscal_id_list]

def get_medicines(fiscal_id):
    link_builder = lambda x: f"{template_link}{fiscal_id}"

    receipt_json = requests.get(link_builder(fiscal_id)).json()

    medicines_list = receipt_json["cheque"]["content"]["items"]

    name_price_list = [(i["itemName"], i["itemPrice"]) for i in medicines_list]

    return name_price_list

rows = []

for fiscal_id in fiscal_id_list:
    rows.extend(get_medicines(fiscal_id))

rows_prepared = []

for row in rows:
    row_prepared=", ".join([str(i) for i in row])
    rows_prepared.append(row_prepared)

rows_prepared = list(set(rows_prepared))

rows_prepared = [f"{i}, {random.randint(3,10)}, None\n" for i in rows_prepared]


with open("items.csv", 'a', encoding="utf-8") as csvfile:
    csvfile.writelines(rows_prepared)