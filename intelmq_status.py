#!/usr/bin/env python

# Extracting intelmq status
# Poulain Damien 2020

import os
import re
import json
import subprocess

def intelmq_status():
    out = subprocess.Popen(["intelmqctl","list","queues-and-status"], stdout=subprocess.PIPE)
    output, err = out.communicate()

    bot_regex = r"Bot (.*) (.*) (.*)\."
    status_regex = r"Bot (.*) is running\."
    queue_regex = r"(.*) - ([0-9]*)"

    bot_names=[]

    bot_status = []
    output = output.decode("utf-8")
    for line in output.splitlines():
        temp_bot={}
        try:
            bot_search = re.search(bot_regex,line)
        except Exception as er:
            continue
        if bot_search:
            temp_bot['botname'] = bot_search.group(1)
            bot_names.append(temp_bot['botname'])
        else:
            continue

        status_search = re.search(status_regex,line)
        if status_search:
            temp_bot['status'] = 1
        else:
            temp_bot['status'] = 0

        bot_status.append(temp_bot)
    return bot_status


def main():
    print(json.dumps(intelmq_status()))


if __name__ == "__main__":
    main()
