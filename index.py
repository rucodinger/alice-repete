def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    text = 'Привет! Я буду повторять всё, что ты мне скажешь. Для помощи скажи "помощь"'

    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        if 'помощь' in event['request']['original_utterance'].lower() or 'help' in event['request'][
            'original_utterance'].lower() or 'хелп' in event['request'][
            'original_utterance'].lower() or 'что ты умеешь' in event['request']['original_utterance'].lower():
            text = 'Привет! Я буду повторять всё, что ты мне скажешь'
        else:
            text = event['request']['original_utterance']
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text,
            # Don't finish the session after this response.
            'end_session': 'false'
        },
    }
