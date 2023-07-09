from dotenv import load_dotenv
import os
import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dialog_flow import detect_intent_texts


def reply(event, vk_api, project_id):
    answer = detect_intent_texts(project_id, event.user_id, [event.text], "ru")
    if answer.intent.is_fallback:
        return

    vk_api.messages.send(
        user_id=event.user_id,
        message=answer.fulfillment_text,
        random_id=random.randint(1, 1000)
    )


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
    vk_api_token = os.getenv("VK_API_TOKEN")

    vk_session = vk.VkApi(token=vk_api_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply(event, vk_api, project_id)


