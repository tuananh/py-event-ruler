py-event-ruler
--------------

## Origin

I love EventBridge and their pattern matching.

The AWS SDK has an [API for testing event pattern](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TestEventPattern.html) with EventBridge sandbox. The problem is that you have to initialize AWS SDK client and make an API call for each test.

In my case, I want to do lots of pattern matching test without being afraid of hitting API rate limit from AWS.

AWS also releases an [open-source version of this pattern matching library in Java](https://github.com/aws/event-ruler) but in my case, I want to use Python because that's what my teammates are familiar with.

## Usage

```python
>>> from out import event_ruler
>>> event_ruler.test_event_pattern('{"foo":true}', '{"foo":[true]}')
True
```

## License

[MIT](./LICENSE)