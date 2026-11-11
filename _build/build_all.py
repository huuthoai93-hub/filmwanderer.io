#!/usr/bin/env python3
"""Rebuild every page of the site. Run from the repository root:  python3 _build/build_all.py"""
import pathlib, runpy

here = pathlib.Path(__file__).resolve().parent
for part in ("home", "filmdesk", "filmtrail"):
    runpy.run_path(str(here / part / "build.py"), run_name="__main__")
