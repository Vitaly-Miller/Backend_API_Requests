#                                                           info
## API variables and structures:
def api_info(response):
    import json

    # BASIC INFO
    url = response.request.url                                       # 'https://api.example.com/endpoint'
    method = response.request.method                                 # 'POST'
    status_code = response.status_code                               # 201
    response_time = response.elapsed.total_seconds()                 # 0.34567

    # Body RAW
    request_body_b = response.request.body                           # b'{"key_1": "value_1"}, {"key_2": "value_2"}
    request_body = json.loads(response.request.body)                 # {"key_1": "value_1"}, {"key_2": "value_2"}
    response_body = response.json()                                  # {"key_1": "value_1"}, {"key_2": "value_2"}
    request_headers = dict(response.request.headers)                 # {"key_1": "value_1"}, {"key_2": "value_2"}
    response_headers = dict(response.headers)                        # {"key_1": "value_1"}, {"key_2": "value_2"}

    # Body JSON
    response_body_json = json.dumps(response.json(), indent=4)       # {
                                                                     #    "key_1": "value_1"
                                                                     #    "key_2": "value_2"
                                                                     # }
