"""
DNS lookup client
"""
from datetime import datetime
import subprocess


class DNS:
    """
    DNS lookup client class
    """

    def __init__(self, domain) -> None:
        self.created = datetime.now()
        self.domain = domain
        self.ip = ""

    def valid_cache(self) -> bool:
        """
        Checks if the cached entry is valid.
        """
        cur = datetime.now()
        delta = (cur - self.created).total_seconds()
        if delta <= (30 + 5):
            return True
        return False

    def update(self, key_values) -> None:
        """
        Update the DNS object.
        """
        for key in key_values:
            if hasattr(self, key):
                setattr(self, key, key_values[key])

    @staticmethod
    def fetch(domain) -> str:
        """
        Executes the 'dig' command with the domain name.
        """
        command_line = f"dig {domain}"
        process = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stderr:
            return stderr
        return stdout

    def debug(self):
        """
        Prints out all the values for the DNS object/record.
        """
        msg = f"Created: {self.created}\nDomain: {self.domain}\nResults: {self.ip}"
        return msg

    def lookup(self) -> str:
        """
        Checks if the cached DNS results are valid, if so, returns it.
        If not, looks up the DNS record for the domain.
        """
        if self.ip and self.valid_cache():
            return self.ip

        self.ip = self.fetch(self.domain)
        self.created = datetime.now()

        return self.ip
