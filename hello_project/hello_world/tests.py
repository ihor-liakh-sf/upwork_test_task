from django.test import TestCase
from django.db import connection
from .models import Table1, Table2


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.db_cursor = connection.cursor()
        self.table1 = Table1._meta.db_table
        self.table1_text_field = 'field_1'
        self.table1_pk = Table1._meta.pk.name

        self.table2 = Table2._meta.db_table
        self.table2_text_field = 'field_2'
        self.table2_fk_field = 'table_1_id'

    def tearDown(self):
        self.db_cursor.close()

    def test_data_displays(self):
        header_text = 'The table'

        self.db_cursor.execute(
            f"INSERT INTO {self.table1} ({self.table1_text_field}) "
            f"VALUES (%s)",
            [header_text]
        )
        list_items_set = [[self.db_cursor.lastrowid, f'List Item {n}'] for n in range(1, 11)]

        self.db_cursor.executemany(
            f"INSERT INTO {self.table2} ({self.table2_fk_field}, {self.table2_text_field}) "
            f"VALUES (%s, %s)",
            list_items_set
        )

        response = self.client.get('/hello-world')
        table_context = response.context['table']

        page_header = getattr(table_context, self.table1_text_field)
        self.assertEqual(header_text, page_header)

        list_items = tuple(table_context.related_items.all().values_list(self.table2_text_field, flat=True))
        self.assertEqual(list_items, tuple(li[1] for li in list_items_set))
