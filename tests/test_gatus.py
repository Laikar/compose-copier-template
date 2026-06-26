from conftest import DockerCommon
from pathlib import Path
import yaml


class TestGatus(DockerCommon):
    def default_data(self, template_paths):
        return {
            "service_template": "gatus",
            "config_file_name": "gatus.yml",
            "proxy_type": "traefik",
            "public_domain": "gatus.example.com",
            "internal_host": "gatus",
            "internal_port": 8080,
            "monitoring_types": [],
            "auth_types": [],
            "gatus_builtin_username": "admin",
            "gatus_builtin_password": "admin",
            "db_type": "none",
            "log_dir": template_paths.logs,
        }

    def test_check_uptime(self, template_paths):
        self.render_template(template_paths)
        docker = self.docker(template_paths.main)
        monitoring = {
            "endpoints": [
                {
                    "name": "example",
                    "url": "https://1.1.1.1",
                    "interval": "30s",
                    "conditions": ["[STATUS] == 200"],
                }
            ]
        }
        example_config = Path(template_paths.main) / "config.d" / "example.yml"
        example_config.write_text(yaml.dump(monitoring))
        docker.compose.up(detach=True)
        try:
            log_stream = docker.compose.logs(stream=True, follow=True)
            while True:
                line = next(log_stream)[1]
                text = (
                    line.decode("utf-8", errors="ignore")
                    if isinstance(line, bytes)
                    else str(line)
                )
                print(text)
                if "Listening on 0.0.0.0:8080" in text:
                    break
                assert "gatus exited with code 2 " not in text

        finally:
            # 4. Always shut down cleanly
            docker.compose.down(remove_orphans=True)
