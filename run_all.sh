#!/bin/bash

set -euo pipefail

for d in $(seq -w 01 25); do
  for s in 1 2; do
    dir="d${d}/s${s}"
    [[ -d "${dir}" ]] && {
      echo -n "${dir}: "
      (cd "${dir}" && PYTHONPATH=$(realpath ../..) "${VIRTUAL_ENV}"/bin/python main.py)
    }
  done
done
