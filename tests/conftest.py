import pytest
from python_on_whales import DockerClient
from typing import NamedTuple
from copier import run_copy


class TemplatePaths(NamedTuple):
    main: str
    data: str
    logs: str


@pytest.fixture
def template_paths(tmp_path_factory: pytest.TempPathFactory):
    return TemplatePaths(
        tmp_path_factory.mktemp("main").as_posix(),
        tmp_path_factory.mktemp("logs").as_posix(),
        tmp_path_factory.mktemp("data").as_posix(),
    )


class Common:
    def render_template(self, template_paths, data=None):
        run_copy(
            ".",
            template_paths.main,
            data=data or self.default_data(template_paths),
            vcs_ref="HEAD",
            defaults=True,
            overwrite=True,
            unsafe=True,
        )

    def test_render_template(self, template_paths):
        self.render_template(template_paths)


class DockerCommon(Common):
    def docker(self, directory):
        return DockerClient(compose_project_directory=directory)

    def ensure_requirements(self, docker: DockerClient):
        config = docker.compose.config()
        for name, network in config.networks.items():
            if network.external and not docker.network.exists(name):
                docker.network.create(name)

    def test_compose_up(self, template_paths):
        self.render_template(template_paths)
        docker = self.docker(template_paths.main)
        self.ensure_requirements(docker)
        docker.compose.up(detach=True, remove_orphans=True)
        docker.compose.down(remove_orphans=True)
