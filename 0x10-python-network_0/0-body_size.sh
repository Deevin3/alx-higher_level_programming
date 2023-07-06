#!/bin/bash
#send reaquest to URL, and display size of response
curl -s "$1" | wc -c
