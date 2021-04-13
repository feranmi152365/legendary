from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'Dashboard'

    def  ready(self):
        import Dashboard.signals
