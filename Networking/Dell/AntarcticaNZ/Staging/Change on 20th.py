
# switchport trunk allowed vlan 1,10,620-621

switchport trunk allowed vlan 1,10,506,620,621


interface port-channel21
 description "Uplink to CHCH-Mgmt1"
 no shutdown
 switchport mode trunk
 switchport access vlan 1
 switchport trunk allowed vlan 10
 mtu 9216
 vlt-port-channel 21
 spanning-tree guard loop


interface ethernet1/1/48:1
 description "Uplink to CHCH-Mgmt1"
 no shutdown
 channel-group 21 mode active
 no switchport
 mtu 9216
 flowcontrol receive off



CHCH-MGMT1#
interface port-channel 21
switchport access vlan 1
switchport trunk allowed vlan add 506,620,621
no shut





