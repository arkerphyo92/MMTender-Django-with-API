# Generated by Django 5.0.6 on 2024-05-26 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StateOrRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.ministry')),
            ],
        ),
        migrations.CreateModel(
            name='ListingTender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('source_company', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('open', 'Open Tender'), ('closed', 'Closed Tender')], default='open', max_length=6)),
                ('opendate', models.DateTimeField()),
                ('closedate', models.DateTimeField()),
                ('attpdf', models.FileField(upload_to='tenders/pdfs/')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.city')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.department')),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.fields')),
                ('source_ministry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.ministry')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.stateorregion')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='stateorregion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.stateorregion'),
        ),
    ]
