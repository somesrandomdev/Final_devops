#!/usr/bin/env bash
# Usage: ./rollback.sh  (optional revision number as arg)
set -e
KUBECONFIG=${KUBECONFIG:-~/.kube/config}
kubectl rollout undo deployment/myapp -n demo ${1:+--to-revision=$1}
kubectl rollout status deployment/myapp -n demo --timeout=120s