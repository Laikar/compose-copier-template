from conftest import DockerCommon


class TestSonarr(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "sonarr",
            "proxy_type": "traefik",
            "public_domain": "sonarr.example.com",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "",
            "auth_types": ["proxy"],
            "db_type": "none",
            "log_dir": template_paths.logs,
        }


class TestRadarr(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "radarr",
            "proxy_type": "traefik",
            "public_domain": "radarr.example.com",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "",
            "auth_types": ["proxy"],
            "db_type": "none",
            "log_dir": template_paths.logs,
        }


class TestProwlarr(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "prowlarr",
            "proxy_type": "traefik",
            "public_domain": "prowlarr.example.com",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "",
            "auth_types": ["proxy"],
            "db_type": "none",
            "log_dir": template_paths.logs,
        }


class TestFlaresolverr(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "flaresolverr",
            "proxy_type": "none",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "",
            "auth_types": ["proxy"],
            "db_type": "none",
            "log_dir": template_paths.logs,
        }
