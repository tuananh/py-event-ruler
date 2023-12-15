.PHONY: clean
clean:
	rm -rf out

.PHONY: build
build: clean
	gopy build -output=dist -vm=python3 ./