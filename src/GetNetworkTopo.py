import networkx as nx
import matplotlib.pyplot as plt
import matplotlib_fontja
import subprocess
import re
import json


class GetNetworkTopo:

    def __init__(self):
        self.interfaces = self.get_topology()
        self.graph = self.get_graph()

    def get_topology(self):
        command = """
        Get-NetIPConfiguration |
        Select-Object @{N='IP';E={$_.IPv4Address.IPAddress}},
        @{N='Gateway';E={$_.IPv4DefaultGateway.NextHop}} |
        ConvertTo-Json -Compress
        """

        result = subprocess.check_output(
            ["powershell", "-NoProfile", "-Command", command],
            text=True
        )

        adapters = json.loads(result)
        if isinstance(adapters, dict):
            adapters = [adapters]

        return [
            {
                "interface": a["IP"],
                "gateway": a.get("Gateway"),
                "devices": self.get_arp_device(a["IP"])
            }
            for a in adapters if a.get("IP")
        ]

    def get_arp_device(self, interface):
        output = subprocess.check_output(
            ["arp", "-a"], text=True, encoding="cp932"
        )

        devices = []
        current = False

        for line in output.splitlines():

            m = re.search(r"([\d.]+)\s+---", line)

            if m:
                current = m.group(1) == interface
                continue

            m = re.search(
                r"^\s*([\d.]+)\s+"
                r"([0-9a-fA-F]{2}(?:-[0-9a-fA-F]{2}){5})\s+"
                r"(dynamic|static|動的|静的)\s*$",
                line,
                re.IGNORECASE
            )

            if m and current:
                devices.append({
                    "ip": m.group(1),
                    "mac": m.group(2),
                    "type": m.group(3)
                })

        return devices

    def to_json(self):
        return json.dumps(self.interfaces, indent=4)
    
    
    def get_graph(self):
        nodes = [
            {"id": "self", "label": "My PC", "type": "self"}
        ]
        edges = []
        added = {"self"}
    
        for interface in self.interfaces:
            gateway = interface["gateway"]
    
            # デフォルトゲートウェイ
            if gateway and gateway not in added:
                nodes.append({
                    "id": gateway,
                    "label": "Default Gateway",
                    "type": "gateway"
                })
                edges.append({
                    "source": "self",
                    "target": gateway
                })
                added.add(gateway)
    
            # ARPで検出したデバイス
            for device in interface["devices"]:
                ip = device["ip"]
    
                if ip not in added:
                    nodes.append({
                        "id": ip,
                        "label": ip,
                        "type": "device",
                        "mac": device["mac"]
                    })
    
                    if gateway:
                        edges.append({
                            "source": gateway,
                            "target": ip
                        })
    
                    added.add(ip)
    
        return {
            "nodes": nodes,
            "edges": edges
        }
        
    



if __name__ == "__main__":
    network = GetNetworkTopo()
    print(network.to_json())
    print(network.get_graph())
    
