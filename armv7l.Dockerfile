FROM ghcr.io/bjia56/armv7l-wheel-builder:main@sha256:7664c40814ba3d9d546d61b4cab16608b86d978f21204a1e59e2efdf1437e8fd

RUN go install github.com/go-python/gopy@v0.4.7 && \
    go install golang.org/x/tools/cmd/goimports@latest

RUN mkdir build
WORKDIR build
COPY . .

RUN for ver in {3.10,3.11,3.12};  \
    do  \
    mkdir -p build${ver} && \
    cd build${ver} && \
    pip${ver} wheel .. && \
    auditwheel repair *armv7l.whl && \
    cd ../ ; \
    done

RUN mkdir -p /export && \
    cp build*/wheelhouse/*.whl /export