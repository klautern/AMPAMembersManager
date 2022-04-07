# Generated by Django 4.0.3 on 2022-04-07 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0021_add_activities'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('bank_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ampa_members_manager.bankaccount')),
                ('registered_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.child')),
                ('registered_family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.family')),
                ('single_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.singleactivity')),
            ],
        ),
        migrations.AddConstraint(
            model_name='activityregistration',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('registered_child__isnull', True), ('registered_family__isnull', False)), models.Q(('registered_child__isnull', False), ('registered_family__isnull', True)), _connector='OR'), name='only one registered'),
        ),
    ]
