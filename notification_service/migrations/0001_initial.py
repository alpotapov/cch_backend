# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CCIEntry'
        db.create_table(u'notification_service_ccientry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recorded_at', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('MDI_OBD_MILEAGE', self.gf('django.db.models.fields.IntegerField')()),
            ('MDI_OBD_FUEL', self.gf('django.db.models.fields.IntegerField')()),
            ('GPS_DIR', self.gf('django.db.models.fields.FloatField')()),
            ('GPS_SPEED', self.gf('django.db.models.fields.IntegerField')()),
            ('IGNITION', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'notification_service', ['CCIEntry'])


    def backwards(self, orm):
        # Deleting model 'CCIEntry'
        db.delete_table(u'notification_service_ccientry')


    models = {
        u'notification_service.ccientry': {
            'GPS_DIR': ('django.db.models.fields.FloatField', [], {}),
            'GPS_SPEED': ('django.db.models.fields.IntegerField', [], {}),
            'IGNITION': ('django.db.models.fields.BooleanField', [], {}),
            'MDI_OBD_FUEL': ('django.db.models.fields.IntegerField', [], {}),
            'MDI_OBD_MILEAGE': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'CCIEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'recorded_at': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['notification_service']