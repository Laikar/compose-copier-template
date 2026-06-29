from conftest import DockerCommon


class TestAuthentik(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "authentik",
            "proxy_type": "traefik",
            "public_domain": "authentik.example.com",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "authentik.tf",
            "auth_types": [],
            "db_type": "postgres",
            "db_name": "authentik",
            "db_user": "authentik",
            "db_password": "password",
            "log_dir": template_paths.logs,
        }
