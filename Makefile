all: match1 .WAIT select .WAIT match3

match3:
	python 3-match-third.py vaspfiles/bto.vasp results/layer12matches_with_stable_basis.csv --outdir=results/layer3matches

match1:
	python 1-match-lattice.py --firstlayer=vaspfiles/bto.vasp --secondlayer=vaspfiles/bto.vasp --outfile=results/layer12matches.csv 
	# cat results/layer12matches.csv | grep 22.62
	
select:
	python 2-select.py  --firstlayer=vaspfiles/bto.vasp --secondlayer=vaspfiles/bto.vasp --matchcsv=results/layer12matches.csv --outfile=results/layer12matches_with_stable_basis.csv
	echo ""; bat results/layer12matches_with_stable_basis.csv || cat results/layer12matches_with_stable_basis.csv

format:
	python -m ruff format .

deps:
	uv pip install -r req.txt || pip install -r req.txt


git:
	git add .
	git commit -m auto_commit
	git push

clean:
	rm -r results/*.csv
