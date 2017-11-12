from channels import Group


def ws_connect(message, room_name):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat-%s" % room_name).add(message.reply_channel)


def ws_disconnect(message, room_name):
    Group("chat-%s" % room_name).discard(message.reply_channel)
