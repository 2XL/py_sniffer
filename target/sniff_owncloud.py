from sniff import Sniff


class OwnCloud(Sniff):

    def __init__(self, args):

        super(self.__class__, self).__init__(args)
        self.whoami = (self).__class__.__name__
        print self.whoami
        self.capture_filter_ips = [self.my_ip, self.sync_server_ip]
        self.capture_filter_ports = [8080]

        self.live_capture.setfilter(
            "(port " + " || port ".join(self.capture_filter_ports) + ") && (host " + " && host ".join(self.capture_filter_ips) + ")",  # filter
        )



    def hello(self):
        print "{} say hello".format(self.whoami)

    def publish(self, src, tgt):
        print "{} say publish".format(self.whoami)

    def download(self, remote, local):
        print "{} say download".format(self.whoami)