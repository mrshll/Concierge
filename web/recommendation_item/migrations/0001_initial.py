# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('recommendation_item_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('recommendation_item', ['Address'])

        # Adding model 'RecommendationItem'
        db.create_table('recommendation_item_recommendationitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('data_sources', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recommendation_item.Address'])),
        ))
        db.send_create_signal('recommendation_item', ['RecommendationItem'])

        # Adding model 'Restaurant'
        db.create_table('recommendation_item_restaurant', (
            ('recommendationitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['recommendation_item.RecommendationItem'], unique=True, primary_key=True)),
            ('cuisines', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('price', self.gf('utility.models.IntegerRangeField')()),
        ))
        db.send_create_signal('recommendation_item', ['Restaurant'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('recommendation_item_address')

        # Deleting model 'RecommendationItem'
        db.delete_table('recommendation_item_recommendationitem')

        # Deleting model 'Restaurant'
        db.delete_table('recommendation_item_restaurant')


    models = {
        'recommendation_item.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'recommendation_item.recommendationitem': {
            'Meta': {'object_name': 'RecommendationItem'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recommendation_item.Address']"}),
            'data_sources': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'recommendation_item.restaurant': {
            'Meta': {'object_name': 'Restaurant', '_ormbases': ['recommendation_item.RecommendationItem']},
            'cuisines': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('utility.models.IntegerRangeField', [], {}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'recommendationitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['recommendation_item.RecommendationItem']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['recommendation_item']