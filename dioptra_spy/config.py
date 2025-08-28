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

import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
DEFAULT_INPUT_DIR = PROJECT_ROOT / "input_images"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_THUMBNAIL_DIR = DEFAULT_OUTPUT_DIR / "thumbnails"

THUMBNAIL_SIZE = (200, 200)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

GOOGLE_MAPS_URL_TEMPLATE = "https://www.google.com/maps?q={lat},{lon}"