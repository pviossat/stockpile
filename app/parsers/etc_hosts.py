import re

from app.objects.secondclass.c_fact import Fact
from app.objects.secondclass.c_relationship import Relationship
from app.utility.base_parser import BaseParser


class Parser(BaseParser):

    def parse(self, blob):
        relationships = []
        for match in self.line(blob):
            values = self.parse_hosts_file_line(match)
            if values:
                for mp in self.mappers:
                    relationships.append(
                        Relationship(source=Fact(mp.source, values[0]),
                                     edge=mp.edge,
                                     target=Fact(mp.target, values[1]))
                    )
        return relationships

    @staticmethod
    def parse_hosts_file_line(line):
        """Given a line from the hosts file, returns a tuple of IPv4, hostname if available (None otherwise).
        Ignores localhost addresses and IPv6."""
        ip_host = None
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            ip_host_info = re.match(r'^^([\d.]+)\s+(\S+)$$', stripped)
            if ip_host_info:
                ip_addr = ip_host_info.group(1)
                hostname = ip_host_info.group(2)
                if not ip_addr.startswith("127"):
                    ip_host = (ip_addr, hostname)
        return ip_host
