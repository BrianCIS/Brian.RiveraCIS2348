# Brian Rivera
# 1922712

import csv
from datetime import datetime
#class used to output inventory based on input csv

class OutputInventory:
#Createlist for new files
    def __init__(self, item_list):

        self.item_list = item_list
#output for all inventory sorted by manufacturer
    def full(self):

        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            # get order of keys to write to file based on manufacturer
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
            man_name = items[item]['manufacturer']
            item_type = items[item]['item_type']
            price = items[item]['price']
            service_date = items[item]['service_date']
            damaged = items[item]['damaged']
            file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))
#outpput csv file for goods by type sorted by item ID
    def by_type(self):

        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))
#output file for goods past service date sorted from age
    def past_service(self):

        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse=True)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

#output file for damged goods and sorts it by price
    def damaged(self):

        items = self.item_list

        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))


if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date
#Create output files
inventory = OutputInventory(items)
inventory.full()
inventory.by_type()
inventory.past_service()
inventory.damaged()




