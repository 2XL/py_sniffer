from target.sniff_box import Box as box
from target.sniff_dropbox import Dropbox as dropbox
from target.sniff_googledrive import GoogleDrive as googledrive
from target.sniff_owncloud import OwnCloud as ownloud
from target.sniff_stacksync import StackSync as stacksync
from threading import Thread
import psutil, os, time

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
        print "START CAPTURE PID: "
        self.register = True
        return self.target.capture()

    def rage_quit(self):
        self.register = False
        parent_pid = os.getpid()
        print "Quiting"
        parent_process = psutil.Process(parent_pid)
        for child in parent_process.children(recursive=True):
            child.kill()
        self.target.capture_quit()
        # time.sleep(5)
        print "Quit parent.kill()"
        parent_process.kill()


        # print "Quited"

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



