# Network segregation

## Version history

| Version | Effective date | Owner | Summary |
|---------|----------------|-------|---------|
| 1.0 | March 16, 2026 | Engineering | Initial documented network segregation policy for Azure infrastructure. |

## Overview

Grunt's infrastructure is hosted in **Microsoft Azure**. Network segregation is implemented using a combination of:

- Azure **Virtual Networks (VNets)** for workloads running on VMs or Kubernetes
- **Network Security Groups (NSGs)** restricting inbound and outbound traffic
- **Azure platform-level tenant isolation** for managed PaaS services
- Service-level access controls such as **IP restrictions, private endpoints, and identity-based access**

Azure enforces **tenant-level isolation between customers and services by default**, providing strong logical separation between environments.

This architecture follows the **Azure shared responsibility model**, where Microsoft secures the underlying cloud platform and Grunt configures network access controls, identity, and resource-level isolation.

## Environment segregation model

Infrastructure resources are logically separated using:

- **Virtual Networks (VNets)** to isolate compute workloads
- **Network Security Groups (NSGs)** to control traffic between subnets and network interfaces
- **Platform-level isolation** provided by Azure for managed PaaS services

For services that run inside VNets (e.g., VMs or Kubernetes nodes), traffic is restricted using NSG rules and subnet segmentation.

For Azure-managed services (e.g., storage, databases, application services), Azure provides **tenant isolation** and service-level access controls such as IP restrictions and private endpoints.

## Network controls

### Virtual network segmentation

Virtual Networks provide logical network boundaries between infrastructure components. Subnets and routing rules further control communication within each network.

### Network Security Groups

Network Security Groups enforce traffic filtering rules at the subnet or network interface level.

Typical controls include:

- limiting inbound traffic to required application ports
- restricting administrative access to approved IP ranges
- default deny behavior for other traffic

## Azure platform-level segregation

Many systems run on **Azure-managed services** that do not reside inside customer VNets. These services operate in Microsoft-managed networks and are segregated through:

- tenant-level isolation between Azure customers
- service-specific firewall configurations
- identity-based access control
- optional private endpoints for private connectivity

This model ensures that workloads remain logically isolated even when not directly connected to customer-managed networks.

## Logging and monitoring

Network configurations and security rules are periodically reviewed as part of infrastructure management and security monitoring processes.

Evidence artifacts may include:

- VNet configuration exports
- NSG configuration and rule exports
- VNet peering configurations
- network topology documentation

## Evidence collection

The following command exports network configuration evidence from Azure into a single Markdown document.  
Resources tagged with `environment=development` are excluded.

```bash
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
```

## Summary

Network segregation within the Azure environment is achieved through:

1. Logical separation using Azure Virtual Networks  
2. Traffic filtering using Network Security Groups  
3. Platform-level tenant isolation for Azure-managed services  
4. Service-level firewall and identity controls  
5. Periodic review and evidence collection of network configurations  

These controls ensure that systems remain logically segregated and that only required network communication is permitted.
