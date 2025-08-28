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