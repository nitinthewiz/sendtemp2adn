#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import adn

def get_temperature():
    """Returns the temperature in degrees C"""
    try:
        s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
        return float(s.split('=')[1][:-3])
    except:
        return 0

app = adn.Adn(access_token="<ADN_access_token>")
app.createPost(text="My temperature right now is " +str(get_temperature())+ " degC")
