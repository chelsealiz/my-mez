# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.last_name'
        db.add_column(u'news_news', 'last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.last_name'
        db.delete_column(u'news_news', 'last_name')


    models = {
        u'news.news': {
            'Meta': {'ordering': "['order']", 'object_name': 'News'},
            'author': ('django.db.models.fields.DateTimeField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': (u'django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'min_free_cropping': (u'django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'original_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'original_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'thumb_image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['news']