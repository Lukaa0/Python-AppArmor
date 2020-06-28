#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import subprocess
import json
import os
import argparse


class AppArmorService:

    def get_profiles(self):
	    result = subprocess.run(['sudo','apparmor_status', '--json'], stdout=subprocess.PIPE)    
	    data = result.stdout.decode('utf-8')
	    p_status = json.loads(data)
	    return p_status



    def get_unconfined(self):
        result = subprocess.run(['sudo', 'aa-unconfined', '--paranoid'
                                ], stdout=subprocess.PIPE)
        data = result.stdout.decode('utf-8')
        lines = data.split('\n')
        apps = []
        for line in lines:
            app = line.split(' ')
            if len(app) > 1:
                apps.append((app[0], app[1]))

        return apps




    def disable_profile(self,profile):
        os.system('sudo ln -s ' + profile + ' /etc/apparmor.d/disable/')

