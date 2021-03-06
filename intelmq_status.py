#!/usr/bin/env python

# Extracting intelmq status
# Poulain Damien 2020

import os
import re
import json
import subprocess

def intelmq_status():
    out = subprocess.Popen(["intelmqctl","list","queues-and-status"], stdout=subprocess.PIPE)
    output = subprocess.check_output(('sort'), stdin=out.stdout)

    bot_regex = r"Bot (.*) (.*) (.*)\."
    status_regex = r"Bot (.*) is running\."
    queue_regex = r"(.*) - ([0-9]*)"

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
        status_search = re.search(status_regex,line)
        if status_search:
            temp_bot['status'] = 1
        else:
            if bot_search:
                temp_bot['status'] = 0
        if temp_bot == {}:
            continue
        bot_status.append(temp_bot)

        bot_status.append(temp_bot)
    for line in output.splitlines():
        for bots in bot_status:
            try:
                bot = bots["botname"]
                queue_regex = rf"\b(?=\w){bot}\b(?!\w)-(.*) - ([0-9]*)"
                queue_search = re.search(queue_regex,line)
                if queue_search:
                    bots[queue_search.group(1)] = int(queue_search.group(2))
            except Exception:
                pass
        continue

    return bot_status


def main():
    print(json.dumps(intelmq_status()))


if __name__ == "__main__":
    main()