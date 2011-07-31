#!/usr/bin/python

"""Example script of a screen scraper yahoo search results, the scraper was
adapted from a selenium IDE testcase, and selenium runs headless."""

# This script is a HACKISH EXAMPLE, it deliberately has not been tidied up
#   because have other things to do... 

from selenium import selenium
from lxml.etree import HTML
import sys
from subprocess import Popen
import atexit
import time
import os

search = sys.argv[1]

servers_log = file('servers.log', 'w')

def clean_up():
    headless_x.kill()
    sel_server.kill() 
    sel_server.wait()
    headless_x.wait()
atexit.register(clean_up)

# Bring up headless selenium
headless_x = Popen(['Xvfb', ':99', '-ac'], stdout=servers_log, stderr=servers_log) # headless X
sel_server = Popen(['java', '-jar', 'selenium-server-standalone-2.2.0.jar'], env=dict(os.environ, DISPLAY=':99'), stdout=servers_log, stderr=servers_log)

sel = selenium("localhost", 4444, "*chrome", "http://uk.yahoo.com/")
time.sleep(10)

for _ in range(10): # Wait for selenium to come up 
    try:
        sel.start()
    except Exception:
        import traceback
        print traceback.format_exc()
        time.sleep(2)
    else:
        break
else:
    raise Exception('Selenium failed to start')


## Do some searching

try:
    sel.open("/?p=us")
    sel.type("id=p_13838465-p", search)
    sel.click("id=search-submit")
    sel.wait_for_page_to_load("30000")
    tree = HTML(sel.get_html_source())
    results = tree.xpath('//*[@class="res"]/descendant::a/@href')
    print '\n'.join(results)
finally:
    sel.stop()


