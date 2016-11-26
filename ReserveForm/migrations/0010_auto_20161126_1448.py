# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-26 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReserveForm', '0009_auto_20161125_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chap',
            options={'verbose_name_plural': '5. چاپ'},
        ),
        migrations.AlterModelOptions(
            name='dookht',
            options={'verbose_name_plural': '3. دوخت'},
        ),
        migrations.AlterModelOptions(
            name='parche',
            options={'verbose_name_plural': '2. پارچه'},
        ),
        migrations.AlterModelOptions(
            name='process',
            options={'verbose_name_plural': '6. فرایند'},
        ),
        migrations.AlterModelOptions(
            name='processformkargar',
            options={'verbose_name_plural': 'وضعیت سفارش'},
        ),
        migrations.AlterModelOptions(
            name='reserveform',
            options={'verbose_name_plural': '1. سفارش ها'},
        ),
        migrations.AlterModelOptions(
            name='servicetarh',
            options={'verbose_name_plural': '4. خدمات مربوط به طرح'},
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='endDay',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], null=True, verbose_name='روز اتمام'),
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='endMonth',
            field=models.IntegerField(blank=True, choices=[(1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'), (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'), (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند')], null=True, verbose_name='ماه اتمام'),
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='endYear',
            field=models.IntegerField(blank=True, choices=[(1395, '۱۳۹۵'), (1396, '۱۳۹۶'), (1397, '۱۹۳۷'), (1398, '۱۳۹۸'), (1399, '۱۳۹۹'), (1400, '۱۴۰۰'), (1401, '۱۴۰۱'), (1402, '۱۴۰۲'), (1403, '۱۴۰۳'), (1404, '۱۴۰۴'), (1405, '۱۴۰۵')], null=True, verbose_name='سال اتمام'),
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='startDay',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], null=True, verbose_name='روز شروع'),
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='startMonth',
            field=models.IntegerField(blank=True, choices=[(1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'), (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'), (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند')], null=True, verbose_name='ماه شروع'),
        ),
        migrations.AlterField(
            model_name='processformkargar',
            name='startYear',
            field=models.IntegerField(blank=True, choices=[(1395, '۱۳۹۵'), (1396, '۱۳۹۶'), (1397, '۱۹۳۷'), (1398, '۱۳۹۸'), (1399, '۱۳۹۹'), (1400, '۱۴۰۰'), (1401, '۱۴۰۱'), (1402, '۱۴۰۲'), (1403, '۱۴۰۳'), (1404, '۱۴۰۴'), (1405, '۱۴۰۵')], null=True, verbose_name='سال شروع'),
        ),
        migrations.AlterField(
            model_name='reserveform',
            name='serviceTarh',
            field=models.ManyToManyField(blank=True, to='ReserveForm.ServiceTarh', verbose_name='خدمات طرح'),
        ),
    ]