all: dist/index.html

dist/index.html: index.html
	cp index.html dist/index.html

test:
	python3 test.py

clean:
	rm -f dist/*