#!/usr/bin/env python

import logging
import sys
sys.path.append('/opt/thug/src')
from ThugAPI import ThugAPI
log = logging.getLogger("Thug")

class ThugClient(ThugAPI):
        def __init__(self, *args):
                ThugAPI.__init__(self, args)

        def analyze(self):
                #self.log_init(url)
                self.set_useragent(user_agent)
                print self.get_useragent()
                self.run_remote(url)
                # self.set_log_output('/tmp/thug_output.txt')
                self.log_event()
                return log
