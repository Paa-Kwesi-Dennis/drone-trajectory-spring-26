import typing as T
import math
import numpy as np

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import (
    compute_image_footprint_on_surface,
    compute_ground_sampling_distance,
)


def compute_distance_between_images(
    camera: Camera, dataset_spec: DatasetSpec
) -> tuple[float, float]:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        The horizontal and vertical distance between images (in meters).
    """
    height = dataset_spec.height
    theta = dataset_spec.camera_angle

    fov_x = np.pi / 2  # use actual camera FOV
    alpha = fov_x / 2

    if np.isclose(theta, np.pi / 2):  # nadir (straight down)
        footprint_x, footprint_y = compute_image_footprint_on_surface(camera, height)
    else:
        near_x = height * np.tan(theta - alpha)
        far_x  = height * np.tan(theta + alpha)
        footprint_x = abs(far_x - near_x)  # abs for safety
        footprint_y = compute_image_footprint_on_surface(camera, height)[1]

    distance_x = footprint_x * (1 - dataset_spec.overlap)
    distance_y = footprint_y * (1 - dataset_spec.sidelap)

    return np.array([distance_x, distance_y], dtype=np.float32)
    

def compute_speed_during_photo_capture(
    camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1
) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.
        allowed_movement_px: The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        The speed at which the drone should move during photo capture.
    """
    distance = compute_ground_sampling_distance(camera, dataset_spec.height)
    return distance / (dataset_spec.exposure_time_ms/1000)


def generate_photo_plan_on_grid(
    camera: Camera, dataset_spec: DatasetSpec
) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        Scan plan as a list of waypoints.

    """
    raise NotImplementedError()