import os
from slack_sdk.webhook import WebhookClient


def notify(views):
    url = os.environ['WEBHOOK']
    webhook = WebhookClient(url)

    blocks = []
    for s in range(len(views)):
        title = views[s]['title']
        viewCount = views[s]['views']
        text = title + "\n:star::star::star::star: "
        text = text + str(viewCount) + "views"
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text
            }
        })

    response = webhook.send(text="fallback", blocks=blocks)
