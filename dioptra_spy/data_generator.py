import json
import pathlib
import logging

log = logging.getLogger(__name__)

def generate_json_data(image_data_list: list, output_file: pathlib.Path):
    log.info(f"Generating JSON data for {len(image_data_list)} images.")
    try:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(image_data_list, f, ensure_ascii=False, indent=2)
        log.info(f"Successfully saved data to: {output_file}")
        return True
    except Exception as e:
        log.error(f"Failed to generate JSON file: {e}", exc_info=True)
        return False