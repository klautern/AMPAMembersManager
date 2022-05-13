# Generated by Django 4.0.3 on 2022-04-01 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0020_add_membership'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_for_member', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_for_no_member', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_type', models.IntegerField(choices=[(1, 'Single'), (2, 'Per Day')])),
            ],
        ),
        migrations.CreateModel(
            name='UniqueActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('assignment', models.IntegerField(choices=[(1, 'Familiar'), (2, 'Individual')])),
                ('funding', models.IntegerField(choices=[(1, 'No Funding'), (2, 'Cultural'), (3, 'Sport')])),
                ('academic_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.academiccourse')),
                ('single_activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.singleactivity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepetitiveActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('assignment', models.IntegerField(choices=[(1, 'Familiar'), (2, 'Individual')])),
                ('funding', models.IntegerField(choices=[(1, 'No Funding'), (2, 'Cultural'), (3, 'Sport')])),
                ('academic_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.academiccourse')),
                ('single_activities', models.ManyToManyField(to='ampa_members_manager.singleactivity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]