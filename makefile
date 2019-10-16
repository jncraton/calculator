all: dist/index.html

dist/index.html: templates/index.html
	cp templates/index.html dist/index.html

test: dist/index.html
	python3 test.py

clean:
	rm -f dist/*