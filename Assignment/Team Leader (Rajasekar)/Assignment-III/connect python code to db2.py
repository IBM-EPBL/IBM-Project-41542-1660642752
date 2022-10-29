# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:07:16 2022

@author: Kutty❤Mani😍
"""

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLservercertificate=DigiCertGlobalRootCA.crt; UID=nwc28246;PWD=tbVCM7HrTQm0DSbd", '', '')
print(conn)
print("connection successful...")