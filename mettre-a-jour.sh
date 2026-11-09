#!/usr/bin/env sh
# Retélécharge la liste public-apis et régénère data.js + public-apis-liste.md
set -e
cd "$(dirname "$0")"
curl -sL https://raw.githubusercontent.com/public-apis/public-apis/master/README.md -o /tmp/public-apis-README.md
python3 -I generer.py /tmp/public-apis-README.md data.js public-apis-liste.md
