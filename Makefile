.PHONY: clean
clean:
	rm -rf src/event_ruler
	rm -rf dist

.PHONY: setup-tools
setup-tools:
	./hack/tools.sh

.PHONY: build
build: clean
	mkdir -p src/event_ruler
	gopy build -output=src/event_ruler -vm=python3 -rename=true -no-make=true ./