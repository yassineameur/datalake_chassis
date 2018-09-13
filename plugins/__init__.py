from airflow.plugins_manager import AirflowPlugin


class CPBasePlugin(AirflowPlugin):
    name = "cp_base_plugin"
    operators = [
    ]
    flask_blueprints = []
    hooks = [
    ]
    executors = []
    admin_views = []


menu_links = []
