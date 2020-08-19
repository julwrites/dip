import hy
import pytest

def pytest_collect_file(parent, path):
    if (path.ext == ".hy" and
        path.basename != "__init__.hy" and
        "#" not in path.basename and
        "test" in path.basename):
        pytest_mod = pytest.Module(path, parent)
        return pytest_mod
