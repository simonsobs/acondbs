"""global constants in tests
"""
from pathlib import Path


TEST_DIR_TOP = Path(__file__).resolve().parent
SAMPLE_DIR = TEST_DIR_TOP.joinpath("sample")


del Path


