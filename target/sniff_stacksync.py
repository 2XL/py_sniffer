from sniff import Sniff
import socket
import pcap


class StackSync(Sniff):
    def __init__(self, args):
        super(self.__class__, self).__init__(args)
        self.whoami = (self).__class__.__name__
        self.capture_filter_ips = [self.my_ip, self.sync_server_ip]
        self.capture_filter_ports = [self.sync_server_port, "5000", "8080"]

        self.live_capture.setfilter(
            "(port " + " || port ".join(self.capture_filter_ports) + ") && (host " + " && host ".join(self.capture_filter_ips) + ")",  # filter
        )

        print self.whoami

    def hello(self):
        print "{} say hello".format(self.whoami)

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)
