#!/usr/bin/env bash
set -euo pipefail

main() {
    setup_tools
}

setup_tools() {
    python3 -m pip install pybindgen
    python3 -m pip install --upgrade build
    
    go install golang.org/x/tools/cmd/goimports@latest
    go install github.com/go-python/gopy@latest

    if ! echo "$PATH" | grep -q "${GOPATH:-undefined}/bin\|$HOME/go/bin"; then
        echo "Go workspace's \"bin\" directory is not in PATH. Run 'export PATH=\"\$PATH:\${GOPATH:-\$HOME/go}/bin\"'."
    fi
}


main "$@"