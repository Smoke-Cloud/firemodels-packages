#!/bin/bash
set -eEuxo pipefail

bash install-oneapi-fedora.sh
bash install-fds-fedora.sh
bash run-tests.sh