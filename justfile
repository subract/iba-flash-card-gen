alias d := dev
# run with poetry (dev)
dev: 
    ENV=development poetry run python -m iba-flash-card-gen

alias r := run
# run with poetry
run: 
    poetry run python -m iba-flash-card-gen