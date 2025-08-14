import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
DEFAULT_INPUT_DIR = PROJECT_ROOT / "input_images"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_THUMBNAIL_DIR = DEFAULT_OUTPUT_DIR / "thumbnails"

THUMBNAIL_SIZE = (200, 200)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

GOOGLE_MAPS_URL_TEMPLATE = "https://www.google.com/maps?q={lat},{lon}"