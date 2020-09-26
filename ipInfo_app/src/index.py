# -*- coding: utf8 -*-
import sys
import logging
import json
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def main_handler(event, context):
    logger.info(json.dumps(event))
    path = str(event['requestContext']['path']).lstrip().rstrip()
    logger.info(f'method: {event["requestContext"]["httpMethod"]}\r\n' +
                f'path: {path}')
    fn = {
        '=/ua': ua,
        '=/ip': ip
    }.get(path, ip)

    return fn(event, context)


def ip(event, context):
    return {"ip": event["requestContext"]["sourceIp"]}


def ua(event, context):
    return {"user-agent": event["headers"]["user-agent"]}
