.PHONY: clean
clean:
	rm -rf out

.PHONY: setup-tools
setup-tools:
	./hack/tools.sh

.PHONY: build
build: clean
	gopy build -output=out -vm=python3 -rename=true -no-make=true ./

.PHONY: test
test: build
	pytest