all: dist/index.html

dist/index.html: render.py templates/index.html
	python3 render.py

test: dist/index.html
	python3 test.py

clean:
	rm -f dist/*