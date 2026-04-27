"""Data models for the camera and user specification."""

class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """
    def __init__(self, overlap: float, sidelap: float, height: float, scan_dimension_x: int, scan_dimension_y: int, exposure_time_ms: float, camera_angle: float):
        self.overlap = overlap
        self.sidelap = sidelap
        self.height = height 
        self.scan_dimension_x = scan_dimension_x
        self.scan_dimension_y = scan_dimension_y
        self.exposure_time_ms = exposure_time_ms
        self.camera_angle = camera_angle
    pass


class Camera:
    """
    Data model for a simple pinhole camera.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """
    def __init__(self, fx: float, fy: float, sensor_size_x_mm: float, sensor_size_y_mm: float, num_pixels_x: int, num_pixels_y: int):
        self.fx = fx
        self.fy = fy
        self.sensor_size_x_mm = sensor_size_x_mm
        self.sensor_size_y_mm = sensor_size_y_mm
        self.num_pixels_x = num_pixels_x
        self.num_pixels_y = num_pixels_y
        
    pass


class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """
    pass

