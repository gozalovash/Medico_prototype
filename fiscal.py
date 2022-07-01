import json, csv, requests

url2 = "https://monitoring.e-kassa.gov.az/pks-portal/1.0.0/documents/"
url1 = "https://monitoring.e-kassa.gov.az/pks-portal/1.0.0/documents/FqqZ1pd59MYh"
url = "https://monitoring.e-kassa.gov.az/#/index?doc=FqqZ1pd59MYh"

def get_check(fiscal_id):
    page = requests.get(url2 + str(fiscal_id))
    return json.loads(page.content)

def get_list(fiscal_id):
    items = []
    data = get_check(fiscal_id)
    for item in data['cheque']["content"]["items"]:
        items.append(item['itemName'])
    return items

def get_order_value(fiscal_id):
    data = get_check(fiscal_id)
    return data['cheque']['content']['sum']

def database_check(item_list):
    marja_list = []
    for item in item_list:
        with open('items.csv') as csv_file:
            csv_reader =  csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if item == row[0]:
                    marja_list.append(int(row[2]))
    return marja_list

def backend(fiscal_id):
    list = get_list(fiscal_id)
    marja_list = database_check(list)
    return sum(marja_list)/len(marja_list)

# def main():
#     fiscal_id = input("Enter ur Fiscal id: \n")
#     cashback = backend(fiscal_id)
#     print(str(cashback)+"% cashback, order value" + str(get_order_value(fiscal_id)))
#
# if __name__ == '__main__':
#     main()

