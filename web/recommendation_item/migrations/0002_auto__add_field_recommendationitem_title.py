# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RecommendationItem.title'
        db.add_column('recommendation_item_recommendationitem', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RecommendationItem.title'
        db.delete_column('recommendation_item_recommendationitem', 'title')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120'})
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