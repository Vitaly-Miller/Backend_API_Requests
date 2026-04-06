# Шпаргалка по работе с response (Requests)

## BASIC INFO

```python
url            = response.request.url                 # 'https://api.example.com/endpoint'
method         = response.request.method              # 'POST'
status_code    = response.status_code                 # 201
response_time  = response.elapsed.total_seconds()     # 0.34567
```

## BODY RAW

```python
request_body_b    = response.request.body             # b'{"key": "value"}'  - bytes
request_body_str  = request_body_b.decode('utf-8')    #'{"key": "value"}'    - 'строка'

request_body      = json.loads(request_body_str)      # {"key": "value"}
response_body     = response.json()                   # {"key": "value"}
request_headers   = dict(response.request.headers)    # {"key": "value"}
response_headers  = dict(response.headers)            # {"key": "value"}
```

## BODY JSON (PRETTY)

```python
response_body_json = json.dumps(response.json(), indent=4)
```
```json
{
    "key_1": "value_1",
    "key_2": "value_2"
}
```
