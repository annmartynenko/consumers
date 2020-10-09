import django_tables2 as tables
from .models import Balance


class BalanceTable(tables.Table):
    pocket_value = tables.Column()

    class Meta:
        model = Balance
        template_name = "django_tables2/bootstrap.html"

    def render_pocket_value(self, value):
        if value.is_integer():
            return '{:0.0f}'.format(value)
        else:
            return '{:0.2f}'.format(value)
