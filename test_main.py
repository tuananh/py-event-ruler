#!/usr/bin/env python

import json
import pytest
from out import event_ruler


def test_simple():
    payload = json.dumps({"foo": True})

    pattern = json.dumps({"foo": [True]})

    assert event_ruler.test_event_pattern(payload, pattern) is True


def test_invalid_pattern():
    with pytest.raises(Exception):
        payload = json.dumps({"foo": True})
        event_ruler.test_event_pattern(payload, "invalid pattern")


def test_invalid_payload():
    with pytest.raises(Exception):
        event_ruler.test_event_pattern("invalid payload", json.dumps({"foo": ["bar"]}))


def test_nested_payload():
    payload = json.dumps(
        {
            "foo": {
                "bar": {"baz": "qux"},
                "fred": "thud",
            }
        }
    )

    pattern = json.dumps({"foo": {"bar": {"baz": ["qux"]}}})

    assert event_ruler.test_event_pattern(payload, pattern) is True
