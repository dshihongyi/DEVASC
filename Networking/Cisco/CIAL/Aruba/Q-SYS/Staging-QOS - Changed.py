# ~~~ Configure Change ~~~~

qos dscp-map 40 local-priority 6 name CS5
qos dscp-map 41 local-priority 6
qos dscp-map 42 local-priority 6 
qos dscp-map 43 local-priority 6 
qos dscp-map 44 local-priority 6 
qos dscp-map 45 local-priority 6 
qos dscp-map 49 local-priority 5
qos dscp-map 26 local-priority 4

qos queue-profile ef_priority
 name queue 7 Voice_Priority_Queue
 map queue 7 local-priority 5
 map queue 6 local-priority 7
 map queue 5 local-priority 6
 map queue 4 local-priority 4
 map queue 3 local-priority 3
 map queue 2 local-priority 2
 map queue 1 local-priority 1
 map queue 0 local-priority 0


qos schedule-profile voip
  strict queue 7
  strict queue 7 max-bandwidth 100000
  dwrr queue 6 weight 1
  dwrr queue 5 weight 1
  dwrr queue 4 weight 1
  dwrr queue 3 weight 1
  dwrr queue 2 weight 1
  dwrr queue 1 weight 1
  dwrr queue 0 weight 1


apply qos queue-profile ef_priority schedule-profile voip



# ~~~ Output ~~~

qos queue-profile ef_priority
    map queue 0 local-priority 0
    map queue 1 local-priority 1
    map queue 2 local-priority 2
    map queue 3 local-priority 3
    map queue 4 local-priority 4
    map queue 5 local-priority 6
    map queue 6 local-priority 7
    map queue 7 local-priority 5
    name queue 7 Voice_Priority_Queue
# qos queue-profile factory-default
#     map queue 0 local-priority 0
#     name queue 0 Scavenger_and_backup_data
#     map queue 1 local-priority 1
#     map queue 2 local-priority 2
#     map queue 3 local-priority 3
#     map queue 4 local-priority 4
#     map queue 5 local-priority 5
#     map queue 6 local-priority 6
#     map queue 7 local-priority 7
# qos schedule-profile factory-default
#     dwrr queue 0 weight 1
#     dwrr queue 1 weight 1
#     dwrr queue 2 weight 1
#     dwrr queue 3 weight 1
#     dwrr queue 4 weight 1
#     dwrr queue 5 weight 1
#     dwrr queue 6 weight 1
#     dwrr queue 7 weight 1
# qos schedule-profile strict
#     strict queue 0
#     strict queue 1
#     strict queue 2
#     strict queue 3
#     strict queue 4
#     strict queue 5
#     strict queue 6
#     strict queue 7
qos schedule-profile voip
    dwrr queue 0 weight 1
    dwrr queue 1 weight 1
    dwrr queue 2 weight 1
    dwrr queue 3 weight 1
    dwrr queue 4 weight 1
    dwrr queue 5 weight 1
    dwrr queue 6 weight 1
    strict queue 7 max-bandwidth 100000
apply qos queue-profile ef_priority schedule-profile voip
# qos trust none
# qos cos-map 0 local-priority 1
# qos cos-map 1 local-priority 0
# qos cos-map 2 local-priority 2
# qos cos-map 3 local-priority 3
# qos cos-map 4 local-priority 4
# qos cos-map 5 local-priority 5
# qos cos-map 6 local-priority 6
# qos cos-map 7 local-priority 7
# qos dscp-map 0 local-priority 1
# qos dscp-map 1 local-priority 1
# qos dscp-map 2 local-priority 1
# qos dscp-map 3 local-priority 1
# qos dscp-map 4 local-priority 1
# qos dscp-map 5 local-priority 1
# qos dscp-map 6 local-priority 1
# qos dscp-map 7 local-priority 1
# qos dscp-map 8 local-priority 0
# qos dscp-map 9 local-priority 0
# qos dscp-map 10 local-priority 0
# qos dscp-map 11 local-priority 0
# qos dscp-map 12 local-priority 0
# qos dscp-map 13 local-priority 0
# qos dscp-map 14 local-priority 0
# qos dscp-map 15 local-priority 0
# qos dscp-map 16 local-priority 2
# qos dscp-map 17 local-priority 2
# qos dscp-map 18 local-priority 2
# qos dscp-map 19 local-priority 2
# qos dscp-map 20 local-priority 2
# qos dscp-map 21 local-priority 2
# qos dscp-map 22 local-priority 2
# qos dscp-map 23 local-priority 2
# qos dscp-map 24 local-priority 3
# qos dscp-map 25 local-priority 3
qos dscp-map 26 local-priority 4 color green
# qos dscp-map 27 local-priority 3
# qos dscp-map 28 local-priority 3
# qos dscp-map 29 local-priority 3
# qos dscp-map 30 local-priority 3
# qos dscp-map 31 local-priority 3
# qos dscp-map 32 local-priority 4
# qos dscp-map 33 local-priority 4
# qos dscp-map 34 local-priority 4
# qos dscp-map 35 local-priority 4
# qos dscp-map 36 local-priority 4
# qos dscp-map 37 local-priority 4
# qos dscp-map 38 local-priority 4
# qos dscp-map 39 local-priority 4
# qos dscp-map 40 local-priority 6 color green name CS5
# qos dscp-map 41 local-priority 6 color green
# qos dscp-map 42 local-priority 6 color green
# qos dscp-map 43 local-priority 6 color green
# qos dscp-map 44 local-priority 6 color green
# qos dscp-map 45 local-priority 6 color green
qos dscp-map 46 local-priority 5
qos dscp-map 47 local-priority 5 color green
# qos dscp-map 48 local-priority 6
qos dscp-map 49 local-priority 5 color green
# qos dscp-map 50 local-priority 6
# qos dscp-map 51 local-priority 6
# qos dscp-map 52 local-priority 6
# qos dscp-map 53 local-priority 6
# qos dscp-map 54 local-priority 6
# qos dscp-map 55 local-priority 6
# qos dscp-map 56 local-priority 7
# qos dscp-map 57 local-priority 7
# qos dscp-map 58 local-priority 7
# qos dscp-map 59 local-priority 7
# qos dscp-map 60 local-priority 7
# qos dscp-map 61 local-priority 7
# qos dscp-map 62 local-priority 7
# qos dscp-map 63 local-priority 7
