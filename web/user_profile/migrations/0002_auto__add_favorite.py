# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Favorite'
        db.create_table('user_profile_favorite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recommendation_item.Restaurant'])),
        ))
        db.send_create_signal('user_profile', ['Favorite'])

        # Adding M2M table for field favorites on 'UserProfile'
        db.create_table('user_profile_favorites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['user_profile.userprofile'], null=False)),
            ('favorite', models.ForeignKey(orm['user_profile.favorite'], null=False))
        ))
        db.create_unique('user_profile_favorites', ['userprofile_id', 'favorite_id'])


    def backwards(self, orm):
        # Deleting model 'Favorite'
        db.delete_table('user_profile_favorite')

        # Removing M2M table for field favorites on 'UserProfile'
        db.delete_table('user_profile_favorites')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'recommendation_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recommendation_item.RecommendationList']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120'})
        },
        'recommendation_item.recommendationlist': {
            'Meta': {'object_name': 'RecommendationList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'recommendation_item.restaurant': {
            'Meta': {'object_name': 'Restaurant', '_ormbases': ['recommendation_item.RecommendationItem']},
            'cuisines': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('utility.models.IntegerRangeField', [], {}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'recommendationitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['recommendation_item.RecommendationItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        'user_profile.favorite': {
            'Meta': {'object_name': 'Favorite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recommendation_item.Restaurant']"})
        },
        'user_profile.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'user_profile'"},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['user_profile.Favorite']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profiles': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'singly_id': ('django.db.models.fields.CharField', [], {'max_length': '260', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['user_profile']