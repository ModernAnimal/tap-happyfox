import datetime
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import timezone

import singer  # type: ignore

from tap_happyfox.streams.api import happyfox_api


def stream(api_key, api_code):
    logging.info("Started happyfox_tickets pipeline.py")

    page_num = 1
    has_next = True

    while has_next:
        tickets, has_next = happyfox_api(api_key, api_code, page_num)
        for ticket in tickets:
            singer.write_record(
                "gem_tickets",
                {
                    "id": ticket["id"],
                    "subject": ticket["subject"],
                    "time_spent": ticket['time_spent'],
                    "first_message": ticket['first_message'],
                    "messages_count": ticket['messages_count'],
                    "status__name": ticket['status']['name'],
                    "category__name": ticket['category']['name'],
                    "priority__id": ticket['priority']['id'],
                    "priority__name": ticket['priority']['name'],
                    "custom_fields": ticket['custom_fields'],
                    "created_at": ticket['created_at'],
                    "updated_at": ticket['updated_at'],
                    "last_staff_reply_at": ticket['last_staff_reply_at'],
                },
            )

        page_num += 1

        logging.info("Gem tickets page completed %s", page_num)

    logging.info("Completed gem_tickets.py")
