import logging

log = logging.getLogger(__name__)

def _dms_to_dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if direction in ['S', 'W']:
        dd *= -1
    return dd

def get_decimal_coords(tags):
    lat, lon = None, None
    try:
        gps_latitude = tags.get('GPS GPSLatitude')
        gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
        gps_longitude = tags.get('GPS GPSLongitude')
        gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _dms_to_dd(gps_latitude.values[0], gps_latitude.values[1], gps_latitude.values[2], gps_latitude_ref.values)
            lon = _dms_to_dd(gps_longitude.values[0], gps_longitude.values[1], gps_longitude.values[2], gps_longitude_ref.values)
    except Exception as e:
        log.error(f"Error converting GPS coordinates: {e}", exc_info=True)
    return lat, lon

def format_datetime(tags):
    try:
        datetime_tag = tags.get('EXIF DateTimeOriginal')
        if datetime_tag:
            return str(datetime_tag.values)
    except Exception:
        pass
    return "N/A"

def format_model(tags):
    try:
        model_tag = tags.get('Image Model')
        if model_tag:
            return str(model_tag.values)
    except Exception:
        pass
    return "N/A"