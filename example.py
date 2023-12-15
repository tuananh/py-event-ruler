import json
from dist import event_ruler

payload = json.dumps({
    "foo": True
})

pattern = json.dumps({
    "foo": [True]
})

print(event_ruler.Test_Event_Pattern(payload, pattern))


try:
    # should throw error here
    event_ruler.Test_Event_Pattern(payload, 'invalid-pattern')
except Exception as e:
    print(e)