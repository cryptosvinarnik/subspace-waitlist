import time
from typing import Generator

import requests
from fake_useragent import UserAgent as ua
from loguru import logger


def join_waitlist(emails: str) -> Generator[int, None, None]:
    for i, email in enumerate(emails, start=1):
        resp = requests.post(
            "https://webflow.com/api/v1/form/61526a2af87a54e565b0ae92",
            data={
                "name": "Email+Form",
                "source": "https://subspace.network/",
                "test": "false",
                "fields[group[213814][256]]": "true",
                "fields[Email+Footer+2]": email,
                "dolphin": "false"
            },
            headers={
                "User-Agent": ua().random
            }
        )

        logger.info(f"{i}/{len(emails)}")

        yield resp.status_code

        time.sleep(6)
