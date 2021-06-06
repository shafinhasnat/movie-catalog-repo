#! /usr/bin/env bash

# wait for dataase to get ready
sleep 10

# Run migrations
python -m flask db upgrade
