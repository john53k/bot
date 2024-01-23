from .. import SUDO



def sudo_only(f):
    async def wrapper(bot, m):
        if m.from_user.id not in SUDO:
            return
        else:
            return f(0,0)
    return wrapper