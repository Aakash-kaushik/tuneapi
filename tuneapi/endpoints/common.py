# Copyright © 2024- Frello Technology Private Limited

from functools import cache

import tuneapi.utils as tu


@cache
def get_sub(
    base_url,
    tune_org_id: str,
    tune_api_key: str,
) -> tu.Subway:

    sess = tu.Subway._get_session()
    sess.headers.update({"x-tune-key": tune_api_key})
    if tune_org_id:
        sess.headers.update({"x-organization-id": tune_org_id})
    return tu.Subway(base_url, sess)