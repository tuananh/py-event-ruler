import json
from src.event_ruler import event_ruler

payload = json.dumps({
    "foo": True
})

pattern = json.dumps({
    "foo": [True]
})

print(event_ruler.test_event_pattern(payload, pattern))


try:
    # should throw error here
    event_ruler.test_event_pattern(payload, 'invalid-pattern')
except Exception as e:
    print(e)