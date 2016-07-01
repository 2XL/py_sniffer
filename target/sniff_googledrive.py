from sniff import Sniff


class GoogleDrive(Sniff):

    def __init__(self, args):

        super(self.__class__, self).__init__(args)
        self.whoami = (self).__class__.__name__
        print "Platform is windows: %s " % self.platform_is_windows
        print "Sniff interface:     %s " % self.iface
        self.capture_filter_ips = [self.my_ip]
        self.capture_filter_ports = ["443"]

        self.live_capture.setfilter(
            "(port " + " || port ".join(self.capture_filter_ports) + ") && (host " + " && host ".join(self.capture_filter_ips) + ")",  # filter
        )


    def hello(self):
        print "{} say hello".format(self.whoami)

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)