PYXBGEN = pyxbgen

all: separouting_v3.py rocs_001_001_06.py

separouting_v3.py:
	${PYXBGEN} -m separouting_v3 separouting_v3.xsd

rocs_001_001_06.py:
	${PYXBGEN} -m rocs_001_001_06 rocs.001.001.06.xsd

clean:
	rm separouting_v3.py
	rm rocs_001_001_06.py
