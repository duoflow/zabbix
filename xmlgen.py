import re
from datetime import datetime
import logging
import json

class XMLGenerator:
    def __init__(self):
        self.debugmode = 1
        self.xml = ""

    def Generate(self):
        hosts = {"bus001-oob": "10.250.4.10", "nss001-oob": "10.250.4.11", "nss002-oob": "10.250.4.12", "zks001-oob": "10.250.4.13", "zks002-oob": "10.250.4.14", "zks003-oob": "10.250.4.15", "zks004-oob": "10.250.4.16", "zks005-oob": "10.250.4.17", "sens001-oob": "10.250.4.18", "sens002-oob": "10.250.4.19", "pibs001-oob": "10.250.4.20", "pibs002-oob": "10.250.4.21", "pibs003-oob": "10.250.4.22", "pibs004-oob": "10.250.4.23", "esxi001-oob": "10.250.4.54", "esxi002-oob": "10.250.4.55", "esxi003-oob": "10.250.4.56", "esxi004-oob": "10.250.4.57", "esxi005-oob": "10.250.4.58", "esxi006-oob": "10.250.4.59", "esxi007-oob": "10.250.4.60", "esxi008-oob": "10.250.4.61", "esxi009-oob": "10.250.4.62", "esxi010-oob": "10.250.4.63", "esxi011-oob": "10.250.4.64", "esxi012-oob": "10.250.4.65", "esxi013-oob": "10.250.4.66", "esxi014-oob": "10.250.4.67", "esxi015-oob": "10.250.4.68", "esxi016-oob": "10.250.4.69", "esxi017-oob": "10.250.4.70", "esxi018-oob": "10.250.4.71"}  
        buffer = ""
        for hostname in hosts:
            ip = hosts[hostname]
            macro = "{$SNMP_SECNAME_CONTEXT}"
            template = """
                <host>
                    <host>{}.prod.dc01.cmu.local</host>
                    <name>{}.prod.dc01.cmu.local</name>
                    <proxy>
                        <name>zabbix-proxy-mysql</name>
                    </proxy>
                    <templates>
                        <template>
                            <name>Template Server Lenovo XCC SNMPv3</name>
                        </template>
                    </templates>
                    <groups>
                        <group>
                            <name>Templates/Server hardware</name>
                        </group>
                    </groups>
                    <interfaces>
                        <interface>
                            <type>SNMP</type>
                            <ip>{}</ip>
                            <dns>{}.prod.dc01.cmu.local</dns>
                            <port>161</port>
                            <interface_ref>if1</interface_ref>
                        </interface>
                    </interfaces>
                    <macros>
                        <macro>
                            <macro>{}</macro>
                            <value>USERID</value>
                        </macro>
                    </macros>
                    <inventory_mode>AUTOMATIC</inventory_mode>
                </host>""".format(hostname, hostname, ip, hostname, macro)
            buffer += template
        
        # compile file
        header = """
                <?xml version="1.0" encoding="UTF-8"?>
                <zabbix_export>
                    <version>4.4</version>
                    <date>2020-03-13T14:22:42Z</date>
                    <groups>
                        <group>
                            <name>Templates/Server hardware</name>
                        </group>
                    </groups>
                    <hosts>
                """
        footer = """
            </hosts>
        </zabbix_export>
        """
        self.xml = header + buffer + footer
        print(self.xml)
    
    def SaveToFile(self):
        try:
            f =  open("xml.xml","w+")
        except IOError:
            print("Error: I can\'t find file or read data")
        else:
            f.write(self.xml)
            f.close()

#
# start script
#
generator = XMLGenerator()
generator.Generate()
generator.SaveToFile()
