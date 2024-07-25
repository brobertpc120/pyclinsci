# Copyright 2024 pyclinsci authors. See license.md file for details.

# Import libraries and objects
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from os import R_OK, access
from pathlib import Path
from typing import Any

import plotly.express as px
from loguru import logger
from pandas import DataFrame, read_excel
from plotly.graph_objs._figure import Figure

from pyclinsci._files import dialog_select_file_dir
from pyclinsci._settings import MODULE_PATH


@dataclass
class GenericData(ABC):
    """Abstract class to store and manage data.

    This class represents a generic data handler that allows importing data
    from a file path into a DataFrame and displaying it using a figure. It can
    also be initialized with a DataFrame instance.

    """

    file_path : Path      = field(default_factory=Path     )
    """Path to the file containing imported data."""

    data      : DataFrame = field(default_factory=DataFrame)
    """DataFrame containing the full data."""

    fig       : Figure    = field(default_factory=Figure   )
    """Figure handler of the data display."""

    def __post_init__(self: "GenericData") -> None:
        """Initialize the GenericData instance after its creation.

        This method checks if the GenericData instance has been initiated with
        a DataFrame. It then verifies if the file path is readable by checking
        its accessibility. If the file path is not provided, it prompts the
        user to select a file using a dialog box. Finally, it imports the data
        from the file path using the read_excel function and logs the
        successful data loading.

        Raises:
            ValueError: If the file path is not readable.

        """
        # GenericData instance has been initiated out of a DataFrame
        if len(list(self.data.columns)) > 0:
            pass

        # Check if file is readable
        if not access(self.file_path, R_OK):
            log_error  = f"File ({self.file_path}) cannot be read. You should "
            log_error += "control if the file path exists and is reachable."
            logger.error(log_error)
            raise ValueError(log_error)

        # Select file to be imported
        if self.file_path == Path():
            self.file_path  = dialog_select_file_dir(
                opt={"*.xlsx": "Excel files"},
            )

        # Import data from file_path
        self.data = read_excel(io=self.file_path)
        logger.info(f"Data were loaded from <{self.file_path}>.")

    def display_data(
        self: "GenericData",
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        """Display the data using a dedicated figure.

        This method calls `build_figure` to create a plotly figure, and
        displays it.

        Parameters:
            **kwargs (Any): Keyword arguments to be passed to the
                `build_figure` method.

        """
        # Build figure
        self.build_figure(**kwargs)

        # Show figure
        self.fig.show()

    @abstractmethod
    def build_figure(
        self: "GenericData",
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        """Build the figure for displaying the data.

        This method is an abstract method that needs to be implemented by
        subclasses to create a plotly figure for displaying the data. Any
        additional keyword arguments passed to this method will be forwarded
        to the implementation in subclasses.

        Parameters:
            **kwargs (Any): Keyword arguments to be passed to the implemented
                `build_figure` method in subclasses.

        """

class GeoData(GenericData):
    """Represent a class for handling geographical data.

    This class extends the GenericData abstract class and provides methods for
    building and displaying geographical data using plotly choropleth maps. It
    includes functionality to extract ISO-3 codes from a configuration file,
    add or replace ISO-3 codes for countries, and remove specific ISO-3 codes
    from the dictionary.

    See Also:
        GenericData : Abstract class for storing and managing data.

    Note:
        This class assumes that the 'geodata.iso3.ini' file is located in the
        `ini_files` directory within the module path specified in the
        `MODULE_PATH` constant.

    .. code-block:: python
        :linenos:
        :caption: Code example

        # Create a GeoData instance
        geo_data = GeoData(file_path="data/geographical_data.xlsx")

        # Display the geographical data
        geo_data.display_data()

        # Add a new ISO-3 code for a country
        GeoData.add_iso3_code("NewCountry", "NEW")

        # Remove an existing ISO-3 code
        GeoData.remove_iso3_code("OLD")

    """

    def __post_init__(self: "GenericData") -> None:
        """Execute post-initialization steps for the GeoData class.

        This method calls the post-initialization method of the parent class
        GenericData using super(). It extracts ISO-3 codes from the
        `geodata.iso3.ini` file using the load_iso3_file() method and assigns
        them to the instance variable iso3_code. It adds ISO-3 codes to the
        geographical data by mapping the `Country` column to the `ISO3` column
        based on the iso3_code dictionary.
        """
        # Execute post initialization for GenericData class
        super().__post_init__()

        # Extract ISO-3 code from ini_files/geodata.iso.ini
        self.iso3_code = GeoData.load_iso3_file()

        # Add ISO-3 code to the geographical data
        self.data["ISO3"] = self.data["Country"]
        self.data = self.data.replace({"ISO3": self.iso3_code})

    def build_figure(
        self: "GeoData",
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        """Build choropleth map based on the geographical data.

        This method builds a choropleth map figure using plotly based on the
        geographical data stored in the class instance.

        Parameters:
            kwargs (Any): Keyword arguments.
            lat (str): Latitude column name.
            lon (str): Longitude column name.
            locations (str, default="ISO3"): Column name representing the
                locations on the map.
            locationmode (str): The mode used to identify locations on the map.
            color (str, default="Data"): Column name representing the color
                data.
            hover_name (str, default="Country"): Column name for hover
                information.
            hover_data (str): Additional data to display on hover.
            color_discrete_sequence (list[str]): List of colors to use for
                discrete data.
            color_discrete_map (dict[str,str]): Mapping of values to colors
                for discrete data.
            color_continuous_scale (list[str], default=["#BFD1D7","#00485E"]):
                Color scale for continuous data.
            range_color (list[str]): Range of colors to map data values to
                colors.
            color_continuous_midpoint (float): Midpoint for continuous color
                scale.
            projection (str): Map projection type.
            scope (str): Map scope.
            center (dict): Center coordinates for the map.
            title (str): Title for the map.
            width (int): Width of the map figure.
            height (int):  Height of the map figure.

        """
        # Extract choropleth parameters
        display_keys = [
            "lat",
            "lon",
            "locations",
            "locationmode",
            "color",
            "hover_name",
            "hover_data",
            "color_discrete_sequence",
            "color_discrete_map",
            "color_continuous_scale",
            "range_color",
            "color_continuous_midpoint",
            "projection",
            "scope",
            "center",
            "title",
            "width",
            "height",
        ]
        display_args = \
            {key:val for key,val in kwargs.items() if key in display_keys}
        update_args = \
            {key:val for key,val in kwargs.items() if key not in display_keys}

        # Set choropleth default values
        if "locations" not in display_args:
            display_args["locations"] = "ISO3"
        if "color" not in display_args:
            display_args["color"] = "Data"
        if "hover_name" not in display_args:
            display_args["hover_name"] = "Country"
        if "color_continuous_scale" not in display_args:
            display_args["color_continuous_scale"]=["#BFD1D7", "#00485E"]

        # Build geographical map
        self.fig = px.choropleth(
            self.data,
            **display_args,
        )

        # Extract borders information
        if "marker" not in update_args:
            border_args = {
                "marker": {"line": {"width": 1.0, "color": "#ffffff"}},
            }
        else:
            marker = update_args["marker"]
            if "line" not in marker:
                marker["line"] = {"width": 0.75, "color": "#ffffff"}
            else:
                if "width" not in marker["line"]:
                    marker["line"]["width"] = 0.75
                if "color" not in marker["line"]:
                    marker["line"]["color"] = "#ffffff"

            border_args = {"marker": marker}
            update_args = \
                {key:val for key,val in update_args.items() if key != "marker"}


        # Update borders
        self.fig.update_traces(**border_args)

        # Update and show figure
        self.fig.update(**update_args)

    @staticmethod
    def load_iso3_file() -> dict[str, str]:
        """Build a dictionary of ISO-3 codes.

        Open and read the 'geodata.iso3.ini' file to build a dictionary
        of ISO-3 codes.

        Returns:
            dict[str, str]: A dictionary mapping keys to ISO-3 values.

        """
        # Open ini_files/geodata.iso.ini and build iso3_code dictionary
        iso3_code = {}
        iso3_file_path = Path(MODULE_PATH / "ini_files/geodata.iso3.ini")
        with iso3_file_path.open() as file:
            for line in file:
                iso3, country = line.strip().split(":")
                iso3_code[country] = iso3

        # Return dictionary
        return iso3_code

    @staticmethod
    def add_iso3_code(country: str, iso3: str) -> None:
        """Add or replace an ISO-3 code for a country.

        Parameters:
            country (str): The name of the country for which the ISO-3 code is
                being added.
            iso3 (str): The ISO-3 code to be added for the country.

        Raises:
            ValueError: If the provided ISO-3 code already exists for another
                country.

        """
        # Load and extract ISO3 codes
        iso3_code = GeoData.load_iso3_file()

        # Control if ISO code already exists
        if iso3 in iso3_code.values():
            keys = [key for key, val in iso3_code.items() if val == iso3]
            log_error = f"<{iso3}> is already set to <{keys}>"
            logger.error(log_error)
            raise ValueError(log_error)

        # Add new code to country
        iso3_code[country] = iso3
        iso3_file_path = Path(MODULE_PATH / "ini_files/geodata.iso3.ini")
        with iso3_file_path.open(mode="w") as file:
            for key, value in iso3_code.items():
                file.write(f"{value}:{key}\n")

        logger.info(f"Added <{iso3}:{country}> to the ISO-3 dictionary.")

    @staticmethod
    def remove_iso3_code(iso3: str) -> None:
        """Remove a specific ISO-3 code from the ISO-3 dictionary.

        Parameters:
            iso3 (str): The ISO-3 code to be removed from the dictionary.

        """
        # Load and extract ISO3 codes
        iso3_code = GeoData.load_iso3_file()

        # Remove ISO3 code
        iso3_code = {key:val for key, val in iso3_code.items() if val != iso3}

        # Save updated ISO3 dictionary
        iso3_file_path = Path(MODULE_PATH / "ini_files/geodata.iso3.ini")
        with iso3_file_path.open(mode="w") as file:
            for key, value in iso3_code.items():
                file.write(f"{value}:{key}\n")

        logger.info(f"Removed ISO-3 <{iso3}> from the ISO-3 dictionary.")
