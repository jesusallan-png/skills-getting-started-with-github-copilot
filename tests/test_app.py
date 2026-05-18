import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
import app


def test_app_imported():
    assert app is not None
