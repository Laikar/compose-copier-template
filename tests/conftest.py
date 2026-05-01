import pytest
from python_on_whales import DockerClient
from collections import namedtuple

# Declaring namedtuple()
TemplatePaths = namedtuple("TemplatePaths", ["main", "logs", "data"])


@pytest.fixture
def template_paths(tmp_path_factory: pytest.TempPathFactory):
    return TemplatePaths(
        tmp_path_factory.mktemp("main").as_posix(),
        tmp_path_factory.mktemp("logs").as_posix(),
        tmp_path_factory.mktemp("data").as_posix(),
    )


class Common:
    def test_render_template(self, template_paths):
        self.render_template(template_paths)


class DockerCommon(Common):
    def docker(self, directory):
        return DockerClient(compose_project_directory=directory)

    def test_compose_up(self, template_paths):
        self.render_template(template_paths)
        docker = self.docker(template_paths.main)
        docker.compose.up(detach=True, remove_orphans=True)
        docker.compose.down(remove_orphans=True)
