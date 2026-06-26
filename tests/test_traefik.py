from conftest import DockerCommon


class TestTraefik(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "traefik",
            "config_file_name": "traefik.yml",
            "proxy_type": "none",
            "monitoring_types": [],
            "auth_types": [],
            "db_type": "none",
            "log_dir": template_paths.logs,
        }
