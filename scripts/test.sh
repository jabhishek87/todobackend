#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# Download requirements to build cache
# pip download -d /build -r requirements_test.txt --no-input

# Install application test requirements
# pip install --no-index -f /build -r requirements_test.txt
pip install  -r requirements_test.txt

echo "finish test.sh"

# Run test.sh arguments
exec $@