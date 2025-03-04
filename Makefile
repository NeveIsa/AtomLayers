default:
	python match-lattice.py --tolerance=0.0001 --outfile=results.csv
	cat results.csv | grep 22.62

deps:
	uv pip install -r req.txt || pip install -r req.txt
