_default:
    just --choose

new_service name:
    #!/usr/bin/env bash
    set -euo pipefail
    src="$(pwd)/src/common"
    dst="$(pwd)/src/{{ name }}"
    mkdir -p "$dst"
    cd "$src"
    find . -type d -exec mkdir -p "$dst/{}" \;
    find . -type f -not -name '_*' -exec ln -srf "$PWD/{}" "$dst/{}" \;
build_copier_conf:
    #!/usr/bin/env bash
    diff -q \
        <(yq -s 'reduce .[] as $item ({}; . * $item)' copier.d/*) \
        <(yq '.' copier.yaml) >/dev/null
    if [ $? -eq 0 ]; then
        exit 0
    else
        yq -s -y 'reduce .[] as $item ({}; . * $item)' copier.d/* > copier.yaml
        exit 1
    fi

render: delete_target
    copier copy . target/
delete_target:
    rm -rf target
