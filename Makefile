match:
	python 1-match-lattice.py --firstlayer=vaspfiles/bto.vasp --secondlayer=vaspfiles/bto.vasp --outfile=results/layer12.csv 
	cat results/layer12.csv | grep 22.62
select:
	python 2-select.py --matchcsv=results/layer12.csv

format:
	python -m ruff format .

deps:
	uv pip install -r req.txt || pip install -r req.txt


git:
	git add .
	git commit -m auto_commit
	git push
