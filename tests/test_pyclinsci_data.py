# Copyright 2024 pyclinsci authors. See license.md file for details.
"""Test settings from pyclinsci package."""

# Import modules, functions, constants
from pyclinsci import (
    GeoData,
    config_logging,
)

# Initialize logging in this file
logger = config_logging(console="TRACE")

# Access to package description variables
def test_geodata() -> None:
    """Test GeoData class from pyclinsci package."""
    # Add and remove an ISO-3 code
    GeoData.add_iso3_code(country="New Country", iso3="NCO")
    GeoData.remove_iso3_code(iso3="NCO")

    # Create an instance of GenericData and display it
    tmp_data = GeoData(file_path="examples/output/geodata_europe.xlsx")
    tmp_data.build_figure(
        scope                     ="europe",
        layout_coloraxis_showscale=False,
        width                     =600,
        height                    =600,
        color_continuous_scale    = ["#00485E", "#00485E"],
        marker                    ={"line": {"color": "#000709"}},
    )
