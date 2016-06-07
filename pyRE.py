#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

tom_mail='<Tom Paris> tom@voyager.org'
someone_mail='someone@gmail.com'
bill_mail='bill.gates@microsoft.com'
re_mail=re.compile(r'^(<[a-zA-Z\s]*>)?[\s]*([a-zA-Z0-9-_\.]*@[a-zA-Z0-9]*\.[a-zA-Z]{1,5})$');

print(re_mail.match(someone_mail).groups())
print(re_mail.match(bill_mail).groups())
print(re_mail.match(tom_mail).groups())


