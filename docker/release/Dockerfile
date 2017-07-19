FROM abhishekk/todobackend-base:latest
MAINTAINER Abhishek Jaiswal <abhishekjaiswal.kol@gmail.com>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse