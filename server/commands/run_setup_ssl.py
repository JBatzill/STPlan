#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from rest_server import ssl
from socket import gethostname
from general import config

ssl.create_key_certificate_pair(gethostname(), config.SSL_COUNTRY, config.SSL_COMPANY, \
    config.SSL_CERT_DURATION, os.path.join(MAIN_DIR, "..", config.SSL_KEY), os.path.join(MAIN_DIR, "..", config.SSL_CERT))