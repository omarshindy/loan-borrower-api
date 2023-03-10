# Generated by Django 4.1.4 on 2022-12-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_alter_loan_status_alter_loanpayments_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanpayments',
            name='status',
            field=models.IntegerField(choices=[(1, 'Paid'), (2, 'Scheduled'), (3, 'Default')], default=2),
        ),
    ]
