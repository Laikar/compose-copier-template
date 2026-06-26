class TestGeneric:
    def default_data(self, template_paths):
        return {
            "service_name": "custom",
            "service_template": "custom",
            "proxy_type": "traefik",
            "public_domain": "test.example.com",
            "internal_host": "test",
            "internal_port": 8080,
            "monitoring_types": ["gatus"],
            "gatus_monitoring_url": "http://test:8080/",
            "config_file_name": "test.toml",
            "auth_types": ["oidc"],
            "ldap_search_domain": "dc=example,dc=com",
            "oidc_client_id": "12345678",
            "oidc_client_secret": "abcdefghijklmnopqrstuvwxyz",
            "db_type": False,
        }
