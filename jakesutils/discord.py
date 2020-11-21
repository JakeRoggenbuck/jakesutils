def clean_mention(mention) -> str:
    return mention[3:-1]


def make_mention(_id) -> str:
    return f"<@!{_id}>"
