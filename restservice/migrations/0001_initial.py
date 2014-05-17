# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'restservice_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('connected_car_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('notification_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tank_max_value', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('fuel_type', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('average_fuel_consumption', self.gf('django.db.models.fields.FloatField')(default=-1, max_length=50)),
            ('last_fuel_amount', self.gf('django.db.models.fields.FloatField')(default=-1, max_length=50)),
        ))
        db.send_create_signal(u'restservice', ['User'])

        # Adding model 'RefuelEvent'
        db.create_table(u'restservice_refuelevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restservice.User'])),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gas_station_id', self.gf('django.db.models.fields.IntegerField')(max_length=20, null=True, blank=True)),
            ('liked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'restservice', ['RefuelEvent'])

        # Adding model 'Recommendation'
        db.create_table(u'restservice_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restservice.User'])),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('gas_station_id', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal(u'restservice', ['Recommendation'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'restservice_user')

        # Deleting model 'RefuelEvent'
        db.delete_table(u'restservice_refuelevent')

        # Deleting model 'Recommendation'
        db.delete_table(u'restservice_recommendation')


    models = {
        u'restservice.recommendation': {
            'Meta': {'object_name': 'Recommendation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gas_station_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restservice.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'restservice.refuelevent': {
            'Meta': {'object_name': 'RefuelEvent'},
            'amount': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'gas_station_id': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'liked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restservice.User']"})
        },
        u'restservice.user': {
            'Meta': {'object_name': 'User'},
            'average_fuel_consumption': ('django.db.models.fields.FloatField', [], {'default': '-1', 'max_length': '50'}),
            'connected_car_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'fuel_type': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_fuel_amount': ('django.db.models.fields.FloatField', [], {'default': '-1', 'max_length': '50'}),
            'notification_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tank_max_value': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['restservice']