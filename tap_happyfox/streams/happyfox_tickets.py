import logging

import singer  # type: ignore

from tap_happyfox.streams.api import happyfox_api


def stream(api_key, api_code, categories):
    logging.info("Started happyfox_tickets pipeline.py")

    for category in categories:

        page_num = 1
        has_next = True

        while has_next:
            tickets, has_next = happyfox_api(
                api_key,
                api_code,
                category,
                page_num
            )
            for ticket in tickets:
                singer.write_record(
                    "happyfox_tickets",
                    {
                        "id": ticket["id"],
                        "subject": ticket["subject"],
                        "time_spent": ticket['time_spent'],
                        "first_message": ticket['first_message'].replace("\n", " "),
                        "messages_count": ticket['messages_count'],
                        "status__name": ticket['status']['name'],
                        "category__name": ticket['category']['name'],
                        "priority__id": ticket['priority']['id'],
                        "priority__name": ticket['priority']['name'],
                        "custom_fields": ticket['custom_fields'],
                        "created_at": ticket['created_at'],
                        "updated_at": ticket.get('last_updated_at', ''),
                        "last_staff_reply_at": ticket['last_staff_reply_at'],
                        "last_user_reply_at": ticket['last_user_reply_at'],
                        "sla_breaches": ticket['sla_breaches'],
                        "updates": ticket['updates'],
                        "assigned_to": ticket['assigned_to'],
                        "user": ticket['user'],
                        "unresponded": ticket['unresponded'],
                        "tags": ticket['tags'],
                    },
                )

            logging.info(
                "Happyfox tickets - category %s, page completed %s",
                category,
                page_num
            )

            page_num += 1

    logging.info("Completed happyfox_tickets.py")
