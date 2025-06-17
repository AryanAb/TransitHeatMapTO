import os
import time
import json
from dotenv import load_dotenv
from datetime import datetime
import googlemaps
from tqdm import tqdm

from coordinates import U_OF_T, corners
from utils import is_point_below_coast

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)


def create_grid(gap: float):
    """
    Returns a list of points which form a grid within the bounding box defined by the corners array.
    The points are located with a distance set by `gap`.
    """
    tr, _, bl, _ = corners
    lat, long = bl[0], bl[1]
    points = []
    while lat < tr[0]:
        long = bl[1]
        while long < tr[1]:
            if not is_point_below_coast(lat, long):
                points.append((lat, long))
            long += gap
        lat += gap
    return points


def calculate_time_to_travel(
    origin,
    destination,
    departure_time=datetime.strptime("2025-09-06 12:00", "%Y-%m-%d %H:%M"),
):
    """
    Returns the time it takes to travel from the `origin` to `destination` in seconds.
    """
    directions_results = gmaps.directions(
        origin=origin,
        destination=destination,
        mode="transit",
        departure_time=departure_time,
    )

    if directions_results:
        if directions_results[0].get("legs") and directions_results[0]["legs"]:
            if directions_results[0]["legs"][0].get("duration", {}).get("value"):
                return directions_results[0]["legs"][0]["duration"]["value"]


def main():
    coordinate_to_duration_map = {}
    points = create_grid(0.012)
    for point in tqdm(points):
        duration = calculate_time_to_travel(
            point,
            U_OF_T,
            departure_time=datetime.strptime("2025-09-06 08:00", "%Y-%m-%d %H:%M"),
        )
        coordinate_to_duration_map[", ".join(str(x) for x in point)] = duration
        time.sleep(0.25)  # sleep for a bit to avoid rate limiting

    with open("data/file.json", "w") as file:
        file.write(json.dumps(coordinate_to_duration_map))


if __name__ == "__main__":
    main()
