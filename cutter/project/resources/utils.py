import string
import random
from .SiteModel import SiteModel


def create_shortcut():
    """
    Generate new random site code
    """
    new_code = ''.join(random.choices(
        string.ascii_uppercase + string.ascii_lowercase + string.digits,
        k=6)
    )

    for item in SiteModel.query.all():
        if item.short_link == new_code:
            return create_shortcut()

    return new_code
