from copier import run_copy
from conftest import DockerCommon


class TestTraefik(DockerCommon):
    def render_template(self, template_paths):
        run_copy(
            ".",
            template_paths.main,
            data={
                "service_name": "traefik",
                "config_file_name": "traefik.yml",
                "proxy_type": "none",
                "monitoring_types": [],
                "auth_types": [],
                "db_type": False,
                "log_dir": template_paths.logs,
            },
            vcs_ref="HEAD",
            defaults=True,
            overwrite=True,
            unsafe=True,
        )
