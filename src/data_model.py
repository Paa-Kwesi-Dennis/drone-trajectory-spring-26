"""Data models for the camera and user specification."""

class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """
    def __init__(self, overlap, sidelap, height, scan_dimension_x, scan_dimension_y, exposure_time_m):
        self.overlap = overlap
        self.sidelap = sidelap
        self.height = height 
        self.scan_dimension_x = scan_dimension_x
        self.scan_dimension_y = scan_dimension_y
        self.exposure_time_m = exposure_time_m
    pass


class Camera:
    """
    Data model for a simple pinhole camera.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """
    pass


class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """
    pass

# Model the nomimal dataset spec

overlap = 0.7
sidelap = 0.7
height = 30.48 # 100 ft
scan_dimension_x = 150
scan_dimension_y = 150
exposure_time_ms = 2 # 1/500 exposure time

dataset_spec = DatasetSpec(overlap, sidelap, height, scan_dimension_x, scan_dimension_y, exposure_time_ms)

print(f"Nominal specs: {dataset_spec}")