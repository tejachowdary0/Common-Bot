from pyrogram.types import Message

def get_file_type(message: Message):
    if message.document:
        return "document"
    if message.video:
        return "video"
    if message.audio:
        return "audio"


def get_file_attr(message: Message):

    """
    Combine audio or video or document
    """

    media = message.audio or \
            message.video or \
            message.document

    return media
