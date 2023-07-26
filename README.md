# Azure OpenAI Chunky Streaming Reproduction

This repository contains sample code to show that the Azure OpenAI API with streaming enabled responds with large chanks instead of individual tokens.

This creates an ugly output and longer response times.

**Azure OpenAI seems to respond with a single chunk only when there is a line break, not after each token.**

## Proof

### asciicinema Gif

![Proof as a gif image](./demo.gif)

### Loom

https://www.loom.com/share/94067bd57a0444ea834faa1759784529

## Setup

1. Install python3
2. Copy the `.env.template` file to `.env` and update the env vars inside of this file
3. Setup a venv, e.g. with `python3 -m venv .venv` or `make venv`
4. Activate the venv with `source .venv/bin/activate`
5. Install dependencies `pip install -r requirements.txt` or `make install`
6. Run the app with `python3 main.py` or `make run`
