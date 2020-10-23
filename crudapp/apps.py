from django.apps import AppConfig


class CrudappConfig(AppConfig):
    name = 'crudapp'
    def ready(self):
    	import crudapp.mysignal