# ~~~~~~~~ Core Switch ~~~~~~~~~~

set vlans vlan-site-HWL-BMS vlan-id 3023
set vlans vlan-site-HWL-BMS l3-interface irb.3023
set interfaces irb unit 3023 description vlan-site-HWL-BMS
set interfaces irb unit 3023 family inet address 10.112.23.1/24

set vlans vlan-bms-vrf-stub vlan-id 4082
set vlans vlan-bms-vrf-stub l3-interface irb.4082
set interfaces irb unit 4082 description vlan-bms-vrf-stub
set interfaces irb unit 4082 family inet address 169.254.254.2/30

set firewall family inet filter filter-loopback term rule-allow-public-icmp from source-address 169.254.254.0/30


set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-bms-vrf-stub
set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-HWL-BMS
set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-HWL-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-HRB-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-HRB-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-PAP-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-PAP-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-RIC-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-RIC-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-RED-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-RED-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-ROL-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-ROL-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-CEN-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-CEN-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-STA-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-STA-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-KAI-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-KAI-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-RNG-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-RNG-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-BUR-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-BUR-BMS

# set groups group-interface-infra-switch interfaces <*> unit 0 family ethernet-switching vlan members vlan-site-MTP-BMS
# set interfaces interface-range range-remote-co-uplinks unit 0 family ethernet-switching vlan members vlan-site-MTP-BMS



set routing-instances vr-co-bms instance-type virtual-router
set routing-instances vr-co-bms routing-options static route 0.0.0.0/0 next-hop 169.254.254.1
set routing-instances vr-co-bms interface irb.3023
set routing-instances vr-co-bms interface irb.4082

# set routing-instances vr-co-bms interface irb.3013
# set routing-instances vr-co-bms interface irb.3033
# set routing-instances vr-co-bms interface irb.3043
# set routing-instances vr-co-bms interface irb.3053
# set routing-instances vr-co-bms interface irb.3063
# set routing-instances vr-co-bms interface irb.3073
# set routing-instances vr-co-bms interface irb.3083
# set routing-instances vr-co-bms interface irb.3093
# set routing-instances vr-co-bms interface irb.3103
# set routing-instances vr-co-bms interface irb.3113
# set routing-instances vr-co-bms interface irb.3123




# ~~~~~~~ IT Firewall ~~~~~~~~






set interfaces reth1 unit 4082 description "Stub network to esl-sw-core - vr-co-bms VRF for BMS subnet"
set interfaces reth1 unit 4082 vlan-id 4082
set interfaces reth1 unit 4082 family inet address 169.254.254.1/30

set security zones security-zone zone-co-bms host-inbound-traffic system-services ping
set security zones security-zone zone-co-bms interfaces reth1.4082
set security address-book zone-co-bms attach zone zone-co-bms

set security address-book zone-co-bms address addr-site-ALL-BMS 10.112.0.0/17

set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match source-address addrs-admin-workstations
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match destination-address addr-site-ALL-BMS
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match application junos-icmp-ping
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match application junos-ssh
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match application junos-http
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms match application junos-https
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms then permit
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms then log session-init
set security policies from-zone zone-admin to-zone zone-co-bms policy policy-admin-co-bms then log session-close

set routing-options static route 10.112.23.0/24 next-hop 169.254.254.2












!~~~~~~~~~~~~~DHCP replay ~~~~~~~~~~~~~~~

Core switch

set routing-instances vr-co-bms forwarding-options dhcp-relay overrides always-write-giaddr
set routing-instances vr-co-bms forwarding-options dhcp-relay server-group ESL-DHCP 10.130.22.100
set routing-instances vr-co-bms forwarding-options dhcp-relay server-group ESL-DHCP 10.130.22.101
set routing-instances vr-co-bms forwarding-options dhcp-relay active-server-group ESL-DHCP
set routing-instances vr-co-bms forwarding-options dhcp-relay group ESL-DHCP route-suppression access-internal
set routing-instances vr-co-bms forwarding-options dhcp-relay group ESL-DHCP interface irb.3023


Firewall

set security zones security-zone zone-co-bms host-inbound-traffic system-services dhcp
set security zones security-zone zone-co-bms host-inbound-traffic system-services bootp

set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp match source-address any
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp match destination-address addrs-dc
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp match application junos-bootpc
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp match application junos-bootps
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp then permit
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp then log session-init
set security policies from-zone zone-co-bms to-zone zone-servers-ad policy policy-co-bms-addrs-dc-dhcp then log session-close