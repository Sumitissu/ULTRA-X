# COPYRIGHT © 2021 BY LEGENDX22

# made by @LEGENDX22
import inspect
from pathlib import Path
import os
def Var(var):
  result = os.environ.get(var, None)
  return result
cmd = os.environ.get('COMMAND_HAND_LER', ".")
from .import CMD_LIST
from .data.sudo_db import all_sudo

async def eor(event, msg):
  sudo = await all_sudo() if await all_sudo() else [12345]
  if event.sender_id in sudo:
    await event.reply(msg)
  else:
    await event.edit(msg)


def UltraX(**x):
  stack = inspect.stack()
  previous_stack_frame = stack[1]
  file_test = Path(previous_stack_frame.filename)
  file_test = file_test.stem.replace(".py", "")
  admin_only = x.get("admin_only", False)
  group_only = x.get("only_group", False)
  sudo = x.get("allow_sudo", False)
  incoming = x.get("incoming", False)
  outgoing = x.get("outgoing", False)
  pattern = x.get("pattern", False)
  if not incoming and not outgoing:
    x["outgoing"] = True
  if pattern:
    x["pattern"] = cmd + x["pattern"]
  if "admin_only" in x:
    del x["admin_only"]
  if "group_only" in x:
    del x["group_only"]
  if "allow_sudo" in x:
    del x["allow_sudo"]
  cmnd = pattern.replace("^", "").replace("(", "").replace(")", "").replace(".", "").replace("*", "").replace("$", "").replace("+", "").replace("?", "").replace("|", "")
  try:
    CMD_LIST[file_test].append(cmnd)
  except BaseException:
    CMD_LIST.update({file_test: [cmnd]})
  def decorator(func):
    test = True
    async def wrapper(event):
      sudos = await all_sudo()
      if not sudos:
        sudos = [12345]
      if sudo:
        if not event.out and not event.sender_id in sudos:
          return
      else:
        pass
      chat = await event.get_chat()
      if group_only and not event.is_group:
        return await eor(event, "This command for groups sir")
      if admin_only:
        try:
          rights = chat.admin_rights
        except:
          rights = False
        if not rights:
          return await eor(event, "this command for only admins sir")
      await func(event)
    bot.add_event_handler(wrapper, events.NewMessage(**x))
    return wrapper
  return decorator