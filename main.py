# DioptraSpy
# Copyright (C) 2025 Kanarath
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import logging
import pathlib
import sys
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

try:
    from dioptra_spy import config, image_processor, data_generator
except ImportError as e:
    log.error(f"Import Error: {e}. Please run this script from the project's root directory.")
    sys.exit(1)

def main():
    start_time = time.time()
    log.info("--- Starting Dioptra Spy (Data Pre-processor) ---")

    parser = argparse.ArgumentParser(description="Process images to generate geolocation data for the Dioptra Spy web interface.")
    parser.add_argument("-i", "--input-dir", type=pathlib.Path, default=config.DEFAULT_INPUT_DIR, help="Directory containing input images.")
    parser.add_argument("-o", "--output-dir", type=pathlib.Path, default=config.DEFAULT_OUTPUT_DIR, help="Directory to save the data.json and thumbnails.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose debug logging.")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()
    thumb_dir = output_dir / "thumbnails"
    json_file_path = output_dir / "data.json"

    if not input_dir.is_dir():
        log.error(f"Input directory not found: {input_dir}")
        sys.exit(1)

    image_data = image_processor.process_directory(input_dir, thumb_dir)
    if not image_data:
        log.warning("No images with usable GPS data were found. No data.json file will be generated.")
        sys.exit(0)

    data_generator.generate_json_data(image_data, json_file_path)

    log.info(f"--- Pre-processing finished in {time.time() - start_time:.2f} seconds ---")
    log.info(f"JSON data saved to: {json_file_path}")
    log.info("Next step: Open the dioptra-spy.html file in your web browser.")

if __name__ == "__main__":
    main()