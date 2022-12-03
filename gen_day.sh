#!/bin/bash

set -euo pipefail

day=$1 && shift

[[ -d $day ]] && {
    echo "file exists"
    exit 1
}

mkdir "${day}"
mkdir "${day}"/s1
mkdir "${day}"/s2

touch "${day}"/__init__.py
touch "${day}"/s1/__init__.py
touch "${day}"/s2/__init__.py

cat <<EOF > "${day}"/s1/main.py
#!/usr/bin/env python3


EOF

chmod +x "${day}"/s1/main.py
cp "${day}"/s1/main.py "${day}"/s2/main.py
