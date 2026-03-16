#!/usr/bin/env bash

set -e

TIMESTAMP=$(date +%Y-%m-%d)
DIR="azure-network-evidence-$TIMESTAMP"

mkdir -p "$DIR"

echo "Collecting Azure network segregation evidence into $DIR"

echo "Exporting VNets..."
az network vnet list \
  --query "[?tags.environment!='development']" \
  -o json > "$DIR/vnets.json"

echo "Exporting NSGs..."
az network nsg list \
  --query "[?tags.environment!='development']" \
  -o json > "$DIR/nsgs.json"

echo "Exporting NSG rules..."
az network nsg list \
  --query "[?tags.environment!='development'].{name:name,rg:resourceGroup}" \
  -o tsv | while read name rg
do
  az network nsg rule list \
    --resource-group "$rg" \
    --nsg-name "$name" \
    -o json > "$DIR/nsg-rules-$name.json"
done

echo "Exporting VNet peerings..."
az network vnet list \
  --query "[?tags.environment!='development'].{name:name,rg:resourceGroup}" \
  -o tsv | while read name rg
do
  az network vnet peering list \
    --resource-group "$rg" \
    --vnet-name "$name" \
    -o json > "$DIR/vnet-peerings-$name.json"
done

echo "Evidence collection complete."
echo "Files stored in: $DIR"