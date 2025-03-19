import polars as pl
import numpy as np
from fire import Fire


def main(matchcsv, basisangle=60):
    df = pl.read_csv(matchcsv)


if __name__ == "__main__":
    Fire(main)
