from tools.tool import load_layer_basis
from tools.match import run
import polars as pl
from fire import Fire
import numpy as np
from tqdm import tqdm
from pathlib import Path


def main(firstlayer, priormatches, outdir):
    A = load_layer_basis(firstlayer)
    df = pl.read_csv(priormatches)

    nrows = len(df)
    for i in tqdm(range(nrows)):
        row = df[i]
        v1 = row["v1x"], row["v1y"]
        v2 = row["v2x"], row["v2y"]
        G = np.array([v1, v2]).T

        df = run(A, G, tolerance=1e-4)
        outfile = Path(outdir) / f"{i}.py"
        df.write_csv(outfile)


if __name__ == "__main__":
    Fire(main)
