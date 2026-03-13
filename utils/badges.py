import os

BADGE_PATH = "assets/badges"

def get_badge_icons(member):

    icons = []

    flags = member.public_flags

    if member.premium_since:
        icons.append(os.path.join(BADGE_PATH,"booster.png"))

    if flags.active_developer:
        icons.append(os.path.join(BADGE_PATH,"active_dev.png"))

    if flags.early_supporter:
        icons.append(os.path.join(BADGE_PATH,"early_supporter.png"))

    if flags.bug_hunter:
        icons.append(os.path.join(BADGE_PATH,"bug_hunter.png"))

    return icons