import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import contextily as ctx
from pyproj import Transformer
from matplotlib.lines import Line2D
from coordinates import (
    DISTILLERY_DISTRICT,
    GO_TRAIN_STATIONS,
    TTC_SUBWAY_STATIONS,
)
from utils import is_point_below_coast


def extract_data(path):
    """Extract coordinates and travel times from the JSON file located at `path`."""
    with open(path) as file:
        coordinate_to_duration_map = json.load(file)

        # Drop all the None values
        coordinate_to_duration_map = {
            k: v for k, v in coordinate_to_duration_map.items() if v is not None
        }
        # Convert the map so that the key is a tuple of numbers
        coordinate_to_duration_map = {
            (float(k.split(",")[0]), float(k.split(",")[1])): v
            for k, v in coordinate_to_duration_map.items()
        }

        points = np.array(list(coordinate_to_duration_map.keys()))
        values = np.array(list(coordinate_to_duration_map.values()))

    return points, values


def create_interpolated_heatmap(points, values, resolution=100, a_min=None, a_max=6000):
    """
    Create interpolated heatmap using the gathered data.
    `points` is a list of tuples of points. `values` is a list of same length with the travel times at each point.
    The `a_min` and `a_max` values are used clip the data from below and above to curtail outliers.
    """
    # Separate lat/lon for clarity
    lats = points[:, 0]
    lons = points[:, 1]

    # Create a grid (lat on y-axis, lon on x-axis)
    grid_lon, grid_lat = np.meshgrid(
        np.linspace(min(lons), max(lons), resolution),
        np.linspace(min(lats), max(lats), resolution),
    )

    # Interpolate values to grid
    grid_travel_times = griddata(
        points, values, (grid_lat, grid_lon), method="cubic", fill_value=np.nan
    )
    grid_travel_times = np.clip(grid_travel_times, a_min=a_min, a_max=a_max)

    # Sometimes for some reason scipy interpolates between places where it should be nan.
    # This is a hacky way of fixing that.
    for i, j in np.ndindex(grid_lat.shape):
        lat = grid_lat[i, j]
        lon = grid_lon[i, j]
        if is_point_below_coast(lat, lon):
            grid_travel_times[i, j] = np.nan

    return grid_lat, grid_lon, grid_travel_times


def transform_to_mercator(lon, lat):
    """Transform `(lat, lon)` to Web Mercator (EPSG:3857)"""
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    x_transformed, y_transformed = transformer.transform(lon, lat)
    return x_transformed, y_transformed


def plot_grid_points(lats, lons):
    """Plot the base grid points. Useful for debugging."""
    x_pts, y_pts = transform_to_mercator(lons, lats)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(
        x_pts,
        y_pts,
        color="blue",
        s=45,
        marker="o",
        edgecolor="white",
        linewidth=1.5,
        zorder=3,
    )
    ctx.add_basemap(
        ax, crs="EPSG:3857", source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.5
    )
    plt.tight_layout()
    plt.show()


def plot_heatmap(x_coords, y_coords, grid_travel_times, destination):
    """Plot heatmap with a basemap under."""
    fig, ax = plt.subplots(figsize=(5, 5))
    img = ax.imshow(
        grid_travel_times,
        extent=[x_coords.min(), x_coords.max(), y_coords.min(), y_coords.max()],
        origin="lower",
        cmap="inferno_r",
        alpha=1,
    )

    # plot GO stations
    for station_lat, station_lon in GO_TRAIN_STATIONS:
        x_coord, y_coord = transform_to_mercator(station_lon, station_lat)
        ax.scatter(
            x_coord,
            y_coord,
            color="green",
            s=30,
            marker="o",
            edgecolor="white",
            linewidth=1,
            zorder=3,
            alpha=0.6,
        )

    # plot TTC subway stations
    for station_lat, station_lon in TTC_SUBWAY_STATIONS:
        x_coord, y_coord = transform_to_mercator(station_lon, station_lat)
        ax.scatter(
            x_coord,
            y_coord,
            color="red",
            s=25,
            marker="o",
            edgecolor="white",
            linewidth=1,
            zorder=3,
            alpha=0.6,
        )

    # plot the destination point
    x_coord, y_coord = transform_to_mercator(destination[1], destination[0])
    ax.scatter(
        x_coord,
        y_coord,
        color="blue",
        s=45,
        marker="o",
        edgecolor="white",
        linewidth=1.5,
        zorder=3,
    )

    legend_elements = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="blue",
            lw=0,
            label="Destination",
            markersize=5,
            markeredgecolor="white",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="green",
            lw=0,
            label="GO Train Stations",
            markersize=5,
            markeredgecolor="white",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="red",
            lw=0,
            label="TTC Subway Stations",
            markersize=5,
            markeredgecolor="white",
        ),
    ]
    ax.legend(loc="lower right", handles=legend_elements)

    ctx.add_basemap(
        ax, crs="EPSG:3857", source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.55
    )
    plt.axis("off")
    plt.colorbar(img, ax=ax, label="Travel Time in Minutes")
    plt.title("Heatmap of Toronto Transit Travel Times")
    plt.tight_layout()
    plt.show()


def main():
    points, values = extract_data("data/Distillery_0800.json")
    (
        grid_lat,
        grid_lon,
        grid_travel_times,
    ) = create_interpolated_heatmap(
        points, values, resolution=100, a_min=None, a_max=6000
    )
    x_coords, y_coords = transform_to_mercator(grid_lon, grid_lat)
    # Divide by 60 to convert from seconds to minutes
    plot_heatmap(x_coords, y_coords, grid_travel_times / 60, DISTILLERY_DISTRICT)


if __name__ == "__main__":
    main()
