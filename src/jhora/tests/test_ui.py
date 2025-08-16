import pytest

try:
    from PyQt6.QtWidgets import QApplication
except Exception:  # pragma: no cover - environment without Qt
    pytest.skip("PyQt6 not available", allow_module_level=True)

from jhora.ui.horo_chart_tabs import ChartTabbed


def test_chart_tabbed_init():
    app = QApplication([])
    chart = ChartTabbed()
    assert chart is not None
