# Generated by Django 4.2 on 2024-01-29 13:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('websockets', '0002_alter_graphqlsubscription_relay_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websocketconnection',
            name='user',
        ),
        migrations.DeleteModel(
            name='GraphQLSubscription',
        ),
        migrations.DeleteModel(
            name='WebSocketConnection',
        ),
    ]
