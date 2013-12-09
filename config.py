import ConfigParser
import os

class config(object):
    """wrapper for the LPW config file"""
    def __init__(self):
        self._configFile = 'lpw.config'
        self.numLEDs = 36
        self.http_port = 80
        self.http_ip = '0.0.0.0'
        try:
            with open(self._configFile) as f:
                self._loadConfig(f)
        except IOError:
            print 'Writing default config file'
            self._writeConfig()

    def _loadConfig(self, f):
        cfg = ConfigParser.RawConfigParser()
        cfg.readfp(f)
        self.numLEDs = cfg.getint('LEDStrip', 'numLEDs')
        self.http_ip = cfg.get('Network', 'http_ip')
        self.http_port = cfg.getint('Network', 'http_port')

    def _writeConfig(self):
        cfg = ConfigParser.RawConfigParser()
        cfg.add_section('LEDStrip')
        cfg.set('LEDStrip', 'numLEDs', self.numLEDs)
        cfg.add_section('Network')
        cfg.set('Network', 'http_ip', self.http_ip)
        cfg.set('Network', 'http_port', self.http_port)
        with open(self._configFile, 'wb') as configfile:
            cfg.write(configfile)



