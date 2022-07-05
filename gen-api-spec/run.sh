#!/usr/bin/env bash

# This script generate EMQX 5.0 HTTP API spec (OpenAPI 3.0.0) to markdown
# It needs widdershins installed.
# npm install -g widdershins
# See more: https://github.com/Mermade/widdershins

set -euo pipefail

# ensure dir
cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")"

widdershins --environment ./env.json ./spec.json -o /tmp/api-spec.md
# no, you can't use wget
grep -E -v 'You\scan\salso\suse\swget' /tmp/api-spec.md > ../en_US/admin/api-spec.md
cp ../en_US/admin/api-spec.md ../zh_CN/admin/api-spec.md
