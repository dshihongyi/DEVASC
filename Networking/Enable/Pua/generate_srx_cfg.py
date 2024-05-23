#! /usr/bin/env /home/aaron/Documents/Enable/Pua/venv/bin/python

import yaml

from jinja2 import Environment, FileSystemLoader
from pprint import pprint

SETTINGS_FILE = "settings.itf.yaml"


settings = None
environment = Environment(loader=FileSystemLoader("templates/"),
                          trim_blocks=True,
                          lstrip_blocks=True)

with open("conf/settings.itf.yaml") as f:
    settings = (yaml.safe_load(f))
    #pprint(settings)

with open("config."+ '.'.join(SETTINGS_FILE.split(".")[:-1]) + '.conf', 'w') as f:
    # deletion config
    f.write("# DELETION STATEMENTS BEGIN - ONLY USE IF NEEDED - TAKE CARE!!!\n\n")
    template = environment.get_template("template.zone.j2")
    content = template.render(new_zones=settings['new_zones'], delete_config=True)
    f.write(content)

    template = environment.get_template("template.addressbook.j2")
    for zone in settings['new_zones']:
        content = template.render(zone=f"zone-{zone}",
                                  delete_config=True)
        f.write(content)
    
    template = environment.get_template("template.reth1int.j2")
    for zone, units in settings['interfaces'].items():
        content = template.render(zone=zone,
                                  interfaces=units,
                                  delete_config=True)
        f.write(content)
    
    template = environment.get_template("template.sourcenat.j2")
    for zone, details in settings['sourcenat'].items():
        content = template.render(name=details['name'],
                                  delete_config=True)
        f.write(content)

    template = environment.get_template("template.policygroups.j2")
    for policyname, details in settings['policygroups'].items():
        content = template.render(type=details['type'],
                                  zone=details['zone'],
                                  end_zones=details['end_zones'],
                                  policy_groupname=policyname,
                                  delete_config=True)
        f.write(content)
    
    template = environment.get_template("template.policy.j2")
    for policyname, details in settings['policies'].items():
        content = template.render(from_zone=details['from_zone'],
                                  to_zone=details['to_zone'],
                                  policy_name=policyname,
                                  delete_config=True)
        f.write(content)


    f.write("\n# DELETION STATEMENTS END\n\n\n\n")

    # zone
    template = environment.get_template("template.zone.j2")
    content = template.render(new_zones=settings['new_zones'])
    f.write(content)

    # addressbook
    template = environment.get_template("template.addressbook.j2")
    for zone, addrs in settings['new_addressbook'].items():
        content = template.render(zone=zone,
                                  addrs=addrs['addr'],
                                  addrsets=addrs['addr_set'])
        f.write(content)
    
    # reth1 interfaces
    template = environment.get_template("template.reth1int.j2")
    for zone, units in settings['interfaces'].items():
        content = template.render(zone=zone,
                                  interfaces=units)
        f.write(content)
    
    # source nat
    template = environment.get_template("template.sourcenat.j2")
    for zone, details in settings['sourcenat'].items():
        content = template.render(zone=zone,
                                  name=details['name'],
                                  prefix=details['prefix'])
        f.write(content)
    
    # policy groups
    template = environment.get_template("template.policygroups.j2")
    for policyname, details in settings['policygroups'].items():
        content = template.render(type=details['type'],
                                  zone=details['zone'],
                                  end_zones=details['end_zones'],
                                  policy_groupname=policyname)
        f.write(content)

    # policies
    template = environment.get_template("template.policy.j2")
    for policyname, details in settings['policies'].items():
        content = template.render(source_addresses=details['source_addresses'],
                                  destination_addresses=details['destination_addresses'],
                                  from_zone=details['from_zone'],
                                  to_zone=details['to_zone'],
                                  policy_name=policyname,
                                  apps=details['apps'],
                                  action=details['action'])
        f.write(content)
