from target.sniff_box import Box as box
from target.sniff_dropbox import Dropbox as dropbox
from target.sniff_googledrive import GoogleDrive as googledrive
from target.sniff_owncloud import OwnCloud as ownloud
from target.sniff_stacksync import StackSync as stacksync
from threading import Thread


class Sniffer(Thread):

    def __init__(self, personal_cloud=None, config={}):
        super(Sniffer, self).__init__()
        print "constructor"
        self.target = None
        if personal_cloud is None:
            raise NotImplemented
        else:
            self.target = eval("{}".format(personal_cloud.lower()))(config)

    def run(self, interval=5):
        print "START CAPTURE PID:"
        self.register = True
        self.target.capture()
        print "Capturing"

    def quit(self):
        self.register = False
        self.target.stop_capture()
        self.cancel()

    def cancel(self):
        '''
        Cancels this thread class
        :return:
        '''
        self.cancelled = True

    def hello(self):
        #try:
        self.target.hello()
        return 0
        #    return 0  # successfully logged to personal cloud service
        # except Exception as ex:
        #     print ex.message
        #     print traceback.print_tb(None)
        #     return 1



