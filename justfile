alias r := run
# run with poetry
run: 
    poetry run python -m iba-fetch

alias rd := run-dev
# run with poetry (dev)
run-dev: 
    ENV=development poetry run python -m iba-fetch