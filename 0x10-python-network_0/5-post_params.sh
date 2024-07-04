#!/bin/bash
# sends POST request with data
# curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
