from django.db import models


class Table1(models.Model):
    table_1_id = models.AutoField(primary_key=True)
    field_1 = models.TextField(null=True, blank=True)


class Table2(models.Model):
    table_2_id = models.AutoField(primary_key=True)
    field_2 = models.TextField(null=True, blank=True)
    table_1 = models.ForeignKey(
        Table1, related_name="related_items", on_delete=models.CASCADE, null=True, blank=True
    )
