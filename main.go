package event_ruler

import (
	"errors"

	"quamina.net/go/quamina"
)

func Test_Event_Pattern(payload, pattern string) (bool, error) {
	q, err := quamina.New()
	if err != nil {
		return false, errors.New("event_ruler: failed to init pattern matcher")
	}

	const patternName = "default"
	err = q.AddPattern(patternName, pattern)
	if err != nil {
		return false, errors.New("event_ruler: fail to add patern")
	}

	matches, err := q.MatchesForEvent([]byte(payload))
	if err != nil {
		return false, errors.New("event_ruler: failed to match for payload")
	}

	for _, m := range matches {
		if m == patternName {
			return true, nil
		}
	}

	return false, errors.New("event_ruler: unexpected error")
}
