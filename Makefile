.PHONY: clean
clean:
	rm -rf dist

.PHONY: setup-tools
setup-tools:
	./hack/tools.sh

.PHONY: build
build: clean
	gopy build -output=dist -vm=python3 -rename=true ./