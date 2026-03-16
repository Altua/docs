#!/usr/bin/env bash

set -euo pipefail

TIMESTAMP=$(date +%Y-%m-%d)
DIR="azure-network-evidence-$TIMESTAMP"
OUTPUT_FILE="$DIR/network-segregation-evidence.md"

mkdir -p "$DIR"

echo "Collecting Azure network segregation evidence into $OUTPUT_FILE"

append_json_section() {
  local title="$1"
  local json_payload="$2"

  {
    echo "## $title"
    echo
    echo '```json'
    printf '%s\n' "$json_payload"
    echo '```'
    echo
  } >> "$OUTPUT_FILE"
}

echo "Exporting VNets..."
vnets_json=$(
  az network vnet list \
    --query "[?tags.environment!='development']" \
    -o json
)

echo "Exporting NSGs..."
nsgs_json=$(
  az network nsg list \
    --query "[?tags.environment!='development']" \
    -o json
)

echo "Preparing evidence document..."
cat > "$OUTPUT_FILE" <<EOF
# Azure network segregation evidence

Generated: $TIMESTAMP

This document contains Azure network configuration evidence for non-development environments.

EOF

append_json_section "Virtual networks" "$vnets_json"
append_json_section "Network security groups" "$nsgs_json"

echo "Exporting NSG rules..."
while IFS=$'\t' read -r name rg; do
  [[ -n "${name:-}" && -n "${rg:-}" ]] || continue

  rules_json=$(
    az network nsg rule list \
      --resource-group "$rg" \
      --nsg-name "$name" \
      -o json
  )

  append_json_section "NSG rules: $name ($rg)" "$rules_json"
done < <(
  az network nsg list \
    --query "[?tags.environment!='development'].{name:name,rg:resourceGroup}" \
    -o tsv
)

echo "Exporting VNet peerings..."
while IFS=$'\t' read -r name rg; do
  [[ -n "${name:-}" && -n "${rg:-}" ]] || continue

  peerings_json=$(
    az network vnet peering list \
      --resource-group "$rg" \
      --vnet-name "$name" \
      -o json
  )

  append_json_section "VNet peerings: $name ($rg)" "$peerings_json"
done < <(
  az network vnet list \
    --query "[?tags.environment!='development'].{name:name,rg:resourceGroup}" \
    -o tsv
)

echo "Evidence collection complete."
echo "Markdown file stored in: $OUTPUT_FILE"
