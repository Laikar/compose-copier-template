_default:
    just --choose

render: delete_target
    copier copy . target/
delete_target:
    rm -rf target
