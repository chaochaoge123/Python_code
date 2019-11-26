#!/usr/bin/env python
# encoding: utf-8


from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_xf_user()

    @staticmethod
    def add_xf_user():
        print(u'同步完成')