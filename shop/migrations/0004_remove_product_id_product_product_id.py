# Generated by Django 4.1.7 on 2023-04-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_product_brand"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="product_id",
            field=models.AutoField(default="no id", primary_key=True, serialize=False),
        ),
    ]
