from copier import run_copy


class TestTemplate:
    def test_render_template(self, template_path):
        run_copy(
            ".",
            template_path,
            data={
                "service_name": "test",
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
            },
            vcs_ref="HEAD",
            defaults=True,
            overwrite=True,
            unsafe=True,
        )
