import pathlib
import logging
from PIL import Image, UnidentifiedImageError
import exifread

from . import config, utils

log = logging.getLogger(__name__)
logging.getLogger('exifread').setLevel(logging.ERROR)

def create_thumbnail(image_path: pathlib.Path, thumb_path: pathlib.Path):
    if thumb_path.exists():
        return True
    try:
        with Image.open(image_path) as img:
            img.thumbnail(config.THUMBNAIL_SIZE)
            thumb_path.parent.mkdir(parents=True, exist_ok=True)
            img.save(thumb_path)
            return True
    except (UnidentifiedImageError, OSError) as e:
        log.warning(f"Cannot create thumbnail for {image_path}: {e}")
        return False

def process_image(image_path: pathlib.Path, thumb_dir: pathlib.Path):
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, stop_tag='DateTimeOriginal')

        if not tags: return None
        lat, lon = utils.get_decimal_coords(tags)
        if lat is None or lon is None: return None

        thumb_filename = f"{image_path.stem}_thumb{image_path.suffix.lower()}"
        thumb_path = thumb_dir / thumb_filename
        if not create_thumbnail(image_path, thumb_path): return None

        return {
            "original_path": str(image_path),
            "thumbnail_rel_path": "output/" + str(thumb_path.relative_to(thumb_dir.parent)).replace("\\", "/"),
            "latitude": lat,
            "longitude": lon,
            "datetime": utils.format_datetime(tags),
            "model": utils.format_model(tags),
        }
    except Exception as e:
        log.error(f"Failed to process image {image_path}: {e}")
        return None

def process_directory(input_dir: pathlib.Path, thumb_dir: pathlib.Path):
    processed_data = []
    log.info(f"Scanning directory: {input_dir}")
    thumb_dir.mkdir(parents=True, exist_ok=True)

    for item in sorted(input_dir.iterdir()):
        if item.is_file() and item.suffix.lower() in config.SUPPORTED_EXTENSIONS:
            data = process_image(item, thumb_dir)
            if data:
                processed_data.append(data)

    log.info(f"Scan complete. Processed {len(processed_data)} images with GPS data.")
    return processed_data