from .models import Balance
import json
from .tables import BalanceTable
from django_tables2 import SingleTableView


def insert_data():
    with open("testdata.json", "r") as read_file:
        data = json.load(read_file)
    for x in data['msg']['balances']:
        for y in x['pockets']:
            start = y['start']
            end = y['end']
            if y['start'] == "":
                start = None
            if y['end'] == "":
                end = None
            new = Balance.objects.create(balance_name=x['name'],
                                         pocket_value=y['value'],
                                         pocket_label=y['label'],
                                         pocket_start_date=start,
                                         pocket_end_date=end)
            new.save()


class MainView(SingleTableView):
    model = Balance
    template_name = 'table.html'
    table_class = BalanceTable

    def get_table_data(self):
        data = Balance.objects.exclude(pocket_value=0)
        if not data:
            insert_data()
        return data
