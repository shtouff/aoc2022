#!/bin/bash

set -euo pipefail

day=$1 && shift

[[ -d $day ]] && {
    echo "file exists"
    exit 1
}

mkdir -p "${day}"/s1

touch "${day}"/__init__.py
touch "${day}"/s1/__init__.py

cat <<EOF > "${day}"/s1/main.py
#!/usr/bin/env python3


EOF

chmod +x "${day}"/s1/main.py
cp -a "${day}"/s1 "${day}"/s2
