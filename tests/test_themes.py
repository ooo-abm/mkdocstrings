"""Tests for the different themes we claim to support."""

import sys

import pytest


@pytest.mark.parametrize(
    "plugin",
    [
        {"theme": "mkdocs"},
        {"theme": "readthedocs"},
        {"theme": {"name": "material"}},
    ],
    indirect=["plugin"],
)
@pytest.mark.skipif(sys.version_info < (3, 7), reason="material is not installed on Python 3.6")
def test_render_themes_templates_python(plugin):
    """Test rendering of a given theme's templates."""
    modules = {
        "mkdocstrings.extension",
        "mkdocstrings.inventory",
        "mkdocstrings.loggers",
        "mkdocstrings.plugin",
        "mkdocstrings.handlers.base",
        "mkdocstrings.handlers.python",
        "mkdocstrings.handlers.rendering",
    }
    handler = plugin.handlers.get_handler("python")
    handler.renderer._update_env(plugin.md, plugin.handlers._config)  # noqa: WPS437
    for identifier in modules:
        data = handler.collector.collect(identifier, {})
        handler.renderer.render(data, {})