from pyrogram.types import Message

def get_media_file_name(message: Message):
    """
    Pass Message object of audio or document or sticker or video or animation to get file_name.
    """

    media = message.audio or \
            message.document or \
            message.sticker or \
            message.video or \
            message.animation

    if media and media.file_name:
        return media.file_name
    else:
        return None


def get_media_file_size(message: Message):
    """
    Pass Message object of audio or document or photo or sticker or video or animation or voice or video_note to get file_size.
    """

    media = message.audio or \
            message.document or \
            message.photo or \
            message.sticker or \
            message.video or \
            message.animation or \
            message.voice or \
            message.video_note

    if media and media.file_size:
        return media.file_size
    else:
        return None

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
