---
tags:
  - machine
  - virtual
  - core
Interfaces:
  - "[[scallop-vmbr0|vmbr0]]"
  - "[[scallop-vmbr1|vmbr1]]"
IP:
  - 192.168.0.x/24
  - 10.10.0.1
Host: "[[thinkcentre-m710s_1|scallop]]"
Hostname: router
---

# OS
[[opnsense]]

# Function
Gateway for [[scallop-subnet|Scallop Subnet]] 
ip `10.10.0.1/23`
DHCP:
- `10.10.1.1` -> `10.10.1.254`