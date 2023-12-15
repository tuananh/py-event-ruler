py-event-ruler
--------------

## Origin

I love EventBridge and their pattern matching.

The AWS SDK has an [API for testing event pattern](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html) with EventBridge sandbox. While it's nice but you have to initialize AWS SDK client and make an API call.

In my case, I want to do lots of pattern matching test without being afraid of hitting API rate limit from AWS.

And while AWS releases an [open-source version of this in Java](https://github.com/aws/event-ruler), I want to use Python because that's what I usually use at work.

Hence, I wrote a quick dirty Python module for this.

## Usage

```python
>>> from out import event_ruler
>>> event_ruler.Test_Event_Pattern('{"foo":true}', '{"foo":[true]}')
True
```

## License

[MIT](./LICENSE)