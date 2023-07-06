#!/bin/bash

url="$1"

# Send request and store response in a temporary file
response=$(curl -s -o /tmp/response.txt -w '%{size_download}' "$url")

# Get size of the response body in bytes
size=$(cat /tmp/response.txt | wc -c)

# Display the size of the response body
echo "Size of the response body: $size bytes"

# Clean up temporary file
rm /tmp/response.txt
