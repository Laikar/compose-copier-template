from pathlib import Path
from copier import run_copy
import pytest
from python_on_whales import DockerClient


@pytest.fixture(scope="class")
def template_path(tmp_path_factory: pytest.TempPathFactory):
    return tmp_path_factory.mktemp("template")


@pytest.fixture(scope="class")
def run_compose(template, copier_answers):
    template_dest, copier_answers = template
    network_name = copier_answers["internal_net"]
    docker = DockerClient(compose_files=[template_dest / "compose.yml"])
    docker.network.create(network_name)
    docker.compose.up(detach=True)
    yield docker, {"network_name": network_name}
    docker.compose.down(volumes=True, remove_orphans=True)
    docker.network.remove(networks=network_name)


@pytest.fixture(scope="class")
def template(template_path, copier_answers):
    run_copy(
        ".",
        template_path,
        data=copier_answers,
        vcs_ref="HEAD",
        defaults=True,
        overwrite=True,
        unsafe=True,
    )
    return template_path, copier_answers


class TestsCommon:
    def test_docker_compose_up(self, template, run_compose):
        """Test that docker-compose up works without issues"""
        docker, data = run_compose
        containers = docker.compose.ps()
        assert len(containers) > 0
        assert containers[0].state.running is True

    def test_template(self, template):
        template_dest, answers = template
        template_dest: Path

        if answers["proxy_type"]:
            assert not (template_dest / answers["proxy_type"]).exists()
