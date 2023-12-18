FROM ghcr.io/bjia56/armv7l-wheel-builder:main

RUN go install github.com/go-python/gopy@v0.4.7 && \
    go install golang.org/x/tools/cmd/goimports@latest

RUN mkdir build
WORKDIR build
COPY . .

RUN for ver in {3.7,3.8,3.9,3.10,3.11};  \
    do  \
    mkdir -p build${ver} && \
    cd build${ver} && \
    pip${ver} wheel .. && \
    auditwheel repair *armv7l.whl && \
    cd ../ ; \
    done

RUN mkdir -p /export && \
    cp build*/wheelhouse/*.whl /export