import pytest
from dash import Dash
from dash.testing.application_runners import import_app

# Fixture to start the Dash app
@pytest.fixture
def dash_app(dash_duo):
    app = import_app("app")  # imports app.py
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(dash_app):
    dash_app.wait_for_text_to_equal("h1", "Soul Foods Pink Morsel Sales Visualiser")

def test_visualisation_present(dash_app):
    graph = dash_app.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_app):
    radio = dash_app.find_element("#region-radio")
    assert radio is not None
