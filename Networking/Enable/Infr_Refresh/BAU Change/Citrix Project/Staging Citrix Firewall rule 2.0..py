
@REM Address-Book Citrix Server
set security address-book zone-servers-dcnservices address addr-enactxddc01 10.130.37.31/32
set security address-book zone-servers-dcnservices address addr-enactxddc02 10.130.37.32/32
set security address-book zone-servers-dcnservices address addr-enactxdb01 10.130.37.33/32
set security address-book zone-servers-rpa address addr-enactxsf01 10.130.71.20/32
set security address-book zone-servers-rpa address addr-enactxsf02 10.130.71.21/32
set security address-book zone-servers-rpa address addr-enactxfs01 10.130.71.22/32
set security address-book zone-servers-rpa address addr-enactxfs02 10.130.71.23/32
set security address-book zone-servers-rpa address addr-enactxlic01 10.130.30.25/32
set security address-book zone-servers-rpa address addr-enactxlic02 10.130.30.26/32
set security address-book zone-servers-edge address addr-enactxvpx01 10.130.30.61/32
set security address-book zone-servers-edge address addr-enactxvpx02 10.130.30.62/32
set security address-book zone-servers-edge address addr-enactxsnip 10.130.30.63/32
set security address-book zone-servers-edge address addr-enactxpxgwvip 10.130.30.64/32
set security address-book zone-servers-edge address addr-enactxsflbvip 10.130.30.65/32
set security address-book zone-servers-edge address addr-enactxliclbvip 10.130.30.66/32
set security address-book zone-servers-dcnservices address-set addrs-ctx-controller-servers address addr-enactxddc01
set security address-book zone-servers-dcnservices address-set addrs-ctx-controller-servers address addr-enactxddc02
set security address-book zone-servers-rpa address-set addrs-ctx-frontend-servers address addr-enactxsf01
set security address-book zone-servers-rpa address-set addrs-ctx-frontend-servers address addr-enactxsf02
set security address-book zone-servers-rpa address-set addrs-ctx-license-servers address addr-enactxlic01
set security address-book zone-servers-rpa address-set addrs-ctx-license-servers address addr-enactxlic02
set security address-book zone-servers-rpa address-set addrs-ctx-profile-servers address addr-enactxfs01
set security address-book zone-servers-rpa address-set addrs-ctx-profile-servers address addr-enactxfs02
set security address-book zone-servers-rpa address-set addrs-ctx-mgmt-servers address-set addrs-ctx-profile-servers
set security address-book zone-servers-rpa address-set addrs-ctx-mgmt-servers address-set addrs-ctx-frontend-servers
set security address-book zone-servers-rpa address-set addrs-ctx-mgmt-servers address-set addrs-ctx-license-servers
set security address-book zone-servers-rpa address-set addrs-ctx-mgmt-servers address addr-enactxhsdgm
set security address-book zone-servers-dcnservices address-set addrs-ctx-mgmt-servers address-set addrs-ctx-controller-servers
set security address-book zone-servers-dcnservices address-set addrs-ctx-mgmt-servers address addr-enactxdb01

@REM Address-Book-Set VDA (NMT&BMP)
set security address-book zone-servers-rpa address addr-enactxstanmp01 dns-name enactxstanmp01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxstanmi01 dns-name enactxstanmi01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxstabmp01 dns-name enactxstabmp01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxstagap01 dns-name enactxstagap01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxhwlnmp01 dns-name enactxhwlnmp01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxhwlnmi01 dns-name enactxhwlnmi01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxhwlbmp01 dns-name enactxhwlbmp01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxhwlgap01 dns-name enactxhwlgap01.ad.enable.net.nz
set security address-book zone-servers-rpa address addr-enactxhsdgm dns-name enactxhsdgm.ad.enable.net.nz
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmt address addr-enactxstanmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmt address addr-enactxstanmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmt address addr-enactxhwlnmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmt address addr-enactxhwlnmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmt address addr-enactxstabmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmt address addr-enactxstagap01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmt address addr-enactxhwlbmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmt address addr-enactxhwlgap01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-servers address-set addrs-ctx-vda-nmt
set security address-book zone-servers-rpa address-set addrs-ctx-vda-servers address-set addrs-ctx-vda-bmt

@REM Rules CTX Controller to VDAs (Rule line 1-4)
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http match source-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http match destination-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http match application junos-http
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http match application junos-https
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http then permit
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http then log session-init
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-rpa policy policy-ctx-controller-vda-http then log session-close
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http match source-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http match destination-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http match application junos-http
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http match application junos-https
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-vda-controller-http then log session-close

@REM Rules CTX Front/FAS to Controller - http,https,smb,rpc (Rule line 5)
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match source-address addrs-ctx-frontend-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match destination-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-http
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-https
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-ms-rpc-tcp
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-smb
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-smb-session
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application app-quic
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http then log session-close


@REM Rules CTX Front/FAS to ENAICAP01 - rpc-tcp (Rule line 6)

# Group Policy applied (set security policies from-zone zone-servers-rpa to-zone zone-servers-prod apply-groups allow-ad-subca-template)

@REM Rules Jumphost to CTX Management - rdp (Rule line 7)
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp match source-address addr-enajump01
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp match source-address addr-enajump02
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp match destination-address addrs-ctx-mgmt-servers
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp match application junos-rdp
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp then permit
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp  then log session-init
set security policies from-zone zone-admin to-zone zone-servers-dcnservices policy policy-admin-ctx-mgmt-rdp  then log session-close
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp match source-address addr-enajump01
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp match source-address addr-enajump02
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp match destination-address addrs-ctx-mgmt-servers
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp match application junos-rdp
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp then permit
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp  then log session-init
set security policies from-zone zone-admin to-zone zone-servers-rpa policy policy-admin-ctx-mgmt-rdp  then log session-close

(....# @# Group Policy applied (policy-admin-servers-rpa-rdp)

@REM Rules Jumphost to CTX VDAs - rdp (Rule line 8)
# Group Policy applied (policy-admin-servers-rpa-rdp)

@REM addr-enactxhsdgm to SMB/DFS - junos-smb (Rule line 9)
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb match source-address addr-enactxhsdgm
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb match destination-address addrs-file-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb match application junos-smb
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-ctx-gm-enable-smb then log session-close

@REM Rules Jumphost to Netscaler MGMT - https/ssh/ntp (Rule line 10)
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match source-address addr-enajump01
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match source-address addr-enajump02
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match destination-address addr-enactxvpx01
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match destination-address addr-enactxvpx02
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match application junos-https
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match application junos-ssh
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management match application junos-ntp
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management then permit
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management then log session-init
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-netscaler-management then log session-close

@REM Rules Netscaler SNIP to CTX Servers - https (Rule line 11-15)
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https match source-address addr-enactxsnip
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https match destination-address addrs-ctx-frontend-servers
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https match application junos-https
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https then permit
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https then log session-init
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-frontend-https then log session-close
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https match source-address addr-enactxsnip
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https match destination-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https match application junos-https
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https match application app-http-alt 
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https then permit
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https then log session-init
set security policies from-zone zone-servers-edge to-zone zone-servers-dcnservices policy policy-netscaler-ctx-controler-https then log session-close
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda match source-address addr-enactxsnip
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda match destination-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda match application app-citrix-client
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda then permit
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda then log session-init
set security policies from-zone zone-servers-edge to-zone zone-servers-rpa policy policy-netscaler-ctx-vda then log session-close
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap match source-address addr-enactxsnip
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap match destination-address addrs-dc
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap match application junos-ldap
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap match application app-ldaps
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap then permit
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap then log session-init
set security policies from-zone zone-servers-edge to-zone zone-servers-ad policy policy-netscaler-ad-ldap then log session-close

@REM Rules CTX VDA to Profile Storage smb (Rule line 16)
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile match source-address addrs-ctx-vda-nmt
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile match destination-address addrs-ctx-profile-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile match application junos-smb
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-profile then log session-close

@REM Rules CTX VDA to Storeage Front http (Rule line xx)
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend match source-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend match destination-address addrs-ctx-frontend-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend match application junos-http
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend match application junos-https
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-ctx-vda-frontend then log session-close

@REM Rules CTX Controller to vCenter - smb (Rule line 17)
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https match source-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https match destination-address addr-enaimpp01
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https match destination-address addr-enaimcp01
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https match application junos-https
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https then permit
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https then log session-init
set security policies from-zone zone-servers-dcnservices to-zone zone-infra-mgmt policy policy-ctx-controller-vcenter-https then log session-close

@REM Rules Jumphost to Netscaler VIP - https (Rule line 18, 22)
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb match source-address addr-enajump01
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb match source-address addr-enajump02
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb match destination-address addr-enactxpxgwvip
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb match destination-address addr-enactxsflbvip
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb match application junos-https
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb then permit
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb then log session-init
set security policies from-zone zone-admin to-zone zone-servers-edge policy policy-admin-citrix-vip-gw-lb then log session-close

@REM Rules Enable/VPN Subnet to VIP - https (Rule line 19-20, 23-24)
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb match source-address any
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb match destination-address addr-enactxpxgwvip
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb match destination-address addr-enactxsflbvip
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb match application junos-https
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb then permit
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb then log session-init
set security policies from-zone zone-enable-lan to-zone zone-servers-edge policy policy-enable-citrix-vip-gw-lb then log session-close

@REM Rules CTX Controller to LC-VIP - https (Rule line 19-20, 23-24)
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic match source-address addrs-ctx-controller-servers
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic match destination-address addr-enactxliclbvip
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic match application app-citrix-licensing
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic match application app-citrix-licensing-admin
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic then permit
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic then log session-init
set security policies from-zone zone-servers-dcnservices to-zone zone-servers-edge policy policy-enable-citrix-vip-lic then log session-close
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https match source-address addrs-ctx-frontend-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https match destination-address addr-enactxpxgwvip
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https match application junos-https
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https match application junos-icmp-ping
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-edge policy policy-ctx-frontend-netscaler-https then log session-close

@REM Rules CTX VDA Servers to enalicp01 - TCP 135 - RPC & TCP 445 - SMB (Rule new request 03/11/2023)
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal match source-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal match destination-address addr-enalicp01
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal match application junos-ms-rpc-tcp
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal match application junos-smb-session
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-cal then log session-close

@REM Rules CTX Servers to KMS (Rule new request 10/11/2023)
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms match source-address addrs-ctx-mgmt-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms match source-address addrs-ctx-vda-servers
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms match destination-address addr-enalicp01
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms match application app-kms
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-kms then log session-close

@REM Rules CTX VDA to dhcp Servers
set forwarding-options dhcp-relay overrides always-write-giaddr
set forwarding-options dhcp-relay server-group ESL-DHCP 10.130.22.100
set forwarding-options dhcp-relay server-group ESL-DHCP 10.130.22.101
set forwarding-options dhcp-relay group ESL-DHCP interface reth1.4071
set forwarding-options dhcp-relay group ESL-DHCP interface reth1.4072
set forwarding-options dhcp-relay active-server-group ESL-DHCP
set forwarding-options dhcp-relay active-server-group allow-server-change
set security zones security-zone zone-servers-rpa host-inbound-traffic system-services dhcp
set security zones security-zone zone-servers-rpa host-inbound-traffic system-services bootp
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp match source-address any
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp match destination-address addrs-dc
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp match application junos-bootpc
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp match application junos-bootps
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-ad policy policy-ctx-vda-addrs-dc-dhcp then log session-close


@REM Rules Netscaler to Internet Azure - https
set security address-book zone-internet address addr-sts.windows.net dns-name sts.windows.net
set security address-book zone-internet address addr-docs.oasis-open.org dns-name docs.oasis-open.org
set security address-book zone-internet address addr-schemas.xmlsoap.org dns-name schemas.xmlsoap.org
set security address-book zone-internet address-set addrs-azure-ad-enterprise-app address addr-sts.windows.net
set security address-book zone-internet address-set addrs-azure-ad-enterprise-app address addr-docs.oasis-open.org
set security address-book zone-internet address-set addrs-azure-ad-enterprise-app address addr-schemas.xmlsoap.org
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet match source-address addr-enactxpxgwvip
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet match destination-address addrs-azure-ad-enterprise-app
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet match application junos-http
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet match application junos-https
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet then permit
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet then log session-init
set security policies from-zone zone-servers-edge to-zone zone-internet policy policy-citrix-vip-gw-internet then log session-close

@REM Rules Internet-Azure Auth Portal to Netscaler VIP
# @Core Switch
set firewall family inet filter filter-inet-to-dmz term rule-netscaler-edge-https from destination-address 202.36.221.39/32
set firewall family inet filter filter-inet-to-dmz term rule-netscaler-edge-https from destination-port https
set firewall family inet filter filter-inet-to-dmz term rule-netscaler-edge-https then count rule-netscaler-edge-https
set firewall family inet filter filter-inet-to-dmz term rule-netscaler-edge-https then log
set firewall family inet filter filter-inet-to-dmz term rule-netscaler-edge-https then accept
# @IT Firewall
set security address-book global address addr-202.36.221.39_32 202.36.221.39/32
set security nat proxy-arp interface reth1.4083 address 202.36.221.39/32
set security nat destination pool dst-nat-enactxpxgwvip address 10.130.30.64/32
set security nat destination rule-set rule-advsec-sftp rule r2 match destination-address 202.36.221.39/32
set security nat destination rule-set rule-advsec-sftp rule r2 then destination-nat pool dst-nat-enactxpxgwvip
set security address-book zone-servers-edge address addr-enactxpxgwvip 10.130.30.64/32
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw match source-address addrs-azure-auth-portal
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw match source-address addr-CCL-Support
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw match destination-address addr-enactxpxgwvip
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw match destination-address addr-202.36.221.39_32
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw match application junos-https
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw then permit
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw then log session-init
set security policies from-zone zone-internet to-zone zone-servers-edge policy policy-internet-edge-citrix-vip-gw then log session-close
set security address-book zone-internet address addr-login.microsoftonline.com dns-name login.microsoftonline.com
set security address-book zone-internet address addr-login.microsoftonline-p.com dns-name login.microsoftonline-p.com
set security address-book zone-internet address addr-secure.aadcdn.microsoftonline-p.com dns-name secure.aadcdn.microsoftonline-p.com
set security address-book zone-internet address addr-aadcdn.msftauth.net dns-name aadcdn.msftauth.net
set security address-book zone-internet address addr-aadcdn.msftauthimages.net dns-name aadcdn.msftauthimages.net
set security address-book zone-internet address addr-aadcdn.msauthimages.net dns-name aadcdn.msauthimages.net
set security address-book zone-internet address addr-logincdn.msftauth.net dns-name logincdn.msftauth.net
set security address-book zone-internet address addr-login.live.com dns-name login.live.com
set security address-book zone-internet address addr-aadcdn.msauth.net dns-name aadcdn.msauth.net
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-login.microsoftonline.com
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-login.microsoftonline-p.com
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-secure.aadcdn.microsoftonline-p.com
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-aadcdn.msftauth.net
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-aadcdn.msftauthimages.net
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-aadcdn.msauthimages.net
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-logincdn.msftauth.net
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-login.live.com
set security address-book zone-internet address-set addrs-azure-auth-portal address addr-aadcdn.msauth.net

@REM Rules add Citrix servers to exist rpa rules
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlbmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstabmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlgap01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstagap01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlnmp01 
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstanmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlnmi01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstanmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmp address addr-enactxhwlnmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmp address addr-enactxstanmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmi address addr-enactxhwlnmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmi address addr-enactxstanmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmp address addr-enactxhwlbmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmp address addr-enactxstabmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-gap address addr-enactxhwlgap01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-gap address addr-enactxstagap01
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-rpa-protege-client match source-address addrs-ctx-vda-bmp
set security policies from-zone zone-servers-rpa to-zone zone-building-security policy policy-rpa-building-security match source-address addrs-ctx-vda-bmp
set security policies from-zone zone-servers-rpa to-zone zone-internet policy policy-temp-rpa-server-internet match source-address addrs-ctx-vda-gap 
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-rpa-enable-smb match source-address addrs-ctx-vda-gap
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech match source-address addrs-ctx-vda-gap
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech-oracle match source-address addrs-ctx-vda-gap
set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-apps-smtprelay match source-address addrs-ctx-vda-gap 
set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addrs-ctx-vda-gap
set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addrs-ctx-vda-nmp 
set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addrs-ctx-vda-nmi
set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addrs-ctx-vda-nmp
set security policies from-zone zone-servers-rpa to-zone zone-servers-itfservices policy policy-itf-u2000 match source-address addrs-ctx-vda-nmi

@REM Rules add Citrix VDA BMP to rpa card printer
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer match source-address addrs-ctx-vda-bmp
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer match destination-address addr-printer-cd800
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer match application app-print-pdl
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer match application app-print-pd2
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer then permit
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer then log session-init
set security policies from-zone zone-servers-rpa to-zone zone-servers-rpa policy policy-rpa-card-printer then log session-close











set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlbmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstabmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlgap01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstagap01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlnmp01 
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstanmp01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxhwlnmi01
set security address-book zone-servers-rpa address-set addrs-rpa-app-servers address addr-enactxstanmi01

set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmp address addr-enactxhwlnmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmp address addr-enactxstanmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmi address addr-enactxhwlnmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-nmi address addr-enactxstanmi01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmp address addr-enactxhwlbmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-bmp address addr-enactxstabmp01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-gap address addr-enactxhwlgap01
set security address-book zone-servers-rpa address-set addrs-ctx-vda-gap address addr-enactxstagap01


set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-rpa-protege-client match source-address addrs-ctx-vda-bmp

set security policies from-zone zone-servers-rpa to-zone zone-building-security policy policy-rpa-building-security match source-address addrs-ctx-vda-bmp

set security policies from-zone zone-servers-rpa to-zone zone-internet policy policy-temp-rpa-server-internet match source-address addrs-ctx-vda-gap 

set security policies from-zone zone-servers-rpa to-zone zone-internet policy policy-temp-rpa-server-internet match source-address addrs-ctx-vda-bmp

set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-rpa-enable-smb match source-address addrs-ctx-vda-gap

set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech match source-address addrs-ctx-vda-gap

set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech-oracle match source-address addrs-ctx-vda-gap

set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-apps-smtprelay match source-address addrs-ctx-vda-gap 

set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addrs-ctx-vda-gap
set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addrs-ctx-vda-nmp 

set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addrs-ctx-vda-nmi
set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addrs-ctx-vda-nmp

set security policies from-zone zone-servers-rpa to-zone zone-servers-itfservices policy policy-itf-u2000 match source-address addrs-ctx-vda-nmi






# set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-rpa-protege-client match source-address addr-enactxhwlbmp01
# set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-rpa-protege-client match source-address addr-enactxstabmp01

# set security policies from-zone zone-servers-rpa to-zone zone-building-security policy policy-rpa-building-security match source-address addr-enactxhwlbmp01
# set security policies from-zone zone-servers-rpa to-zone zone-building-security policy policy-rpa-building-security match source-address addr-enactxstabmp01

# set security policies from-zone zone-servers-rpa to-zone zone-internet policy policy-temp-rpa-server-internet match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-internet policy policy-temp-rpa-server-internet match source-address addr-enactxstagap01

# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-rpa-enable-smb match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-rpa-enable-smb match source-address addr-enactxstagap01

# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech match source-address addr-enactxstagap01

# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech-oracle match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-gtech-oracle match source-address addr-enactxstagap01

# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-apps-smtprelay match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-servers-prod policy policy-citrix-apps-smtprelay match source-address addr-enactxstagap01

# set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addr-enactxhwlgap01 
# set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addr-enactxstagap01 
# set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addr-enactxhwlnmp01 
# set security policies from-zone zone-servers-rpa to-zone zone-dcn policy policy-rpa-u2000-v2r16 match source-address addr-enactxstanmp01

# set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addr-enactxhwlnmi01
# set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addr-enactxstanmi01
# set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addr-enactxhwlnmp01
# set security policies from-zone zone-enable-lan to-zone zone-servers-rpa policy policy-enable-lan-vpn-rdp-in match destination-address addr-enactxstanmp01

# set security policies from-zone zone-servers-rpa to-zone zone-servers-itfservices policy policy-itf-u2000 match source-address addr-enactxhwlnmi01
# set security policies from-zone zone-servers-rpa to-zone zone-servers-itfservices policy policy-itf-u2000 match source-address addr-enactxstanmi01





~~~ Change revert on COB of 15th Dec ~~~

set security address-book zone-servers-rpa address addr-ctx-frontend 10.130.71.0/24
set security address-book zone-servers-rpa address-set addrs-ctx-frontend-servers address addr-ctx-frontend

set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-ms-rpc-tcp
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-smb
set security policies from-zone zone-servers-rpa to-zone zone-servers-dcnservices policy policy-ctx-frontend-controller-http match application junos-smb-session


# @REM DHCP Relay

# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc match source-address any
# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc match destination-address addrs-dc
# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc match application junos-dhcp-relay
# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc then permit
# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc then log session-init
# set security policies from-zone zone-enable-lan to-zone zone-servers-ad policy policy-dhcp-relay-addrs-dc then log session-close


