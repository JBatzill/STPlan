#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from rest_server.security import create_key_certificate_pair
from socket import gethostname
from general import config
from logger import get_log_rest

get_log_rest().info("Creating new key - certificate pair ...")

create_key_certificate_pair(gethostname(), config.SSL_COUNTRY, config.SSL_COMPANY, \
    config.SSL_CERT_DURATION, os.path.join(MAIN_DIR, "..", config.SSL_KEY), os.path.join(MAIN_DIR, "..", config.SSL_CERT))

get_log_rest().info("Created new key - certificate pair!")
input()
