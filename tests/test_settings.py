from pathlib import Path

import pytest

from settings import Settings


@pytest.fixture
def settings():
    return Settings()


def test_settings(settings):
    base_dir = Path(__file__).absolute().parent.parent
    assert settings.base_dir == base_dir
    assert settings.resources == base_dir / "resources"
