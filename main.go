package event_ruler

import (
	"errors"

	"quamina.net/go/quamina"
)

var (
	errInitFailure     = errors.New("failed to init pattern matcher")
	errInvalidPattern  = errors.New("invalid pattern")
	errMatchingFailure = errors.New("failed to match for payload")
	errUnexpected      = errors.New("unexpected error")
)

func Test_Event_Pattern(payload, pattern string) (bool, error) {
	q, err := quamina.New()
	if err != nil {
		return false, errInitFailure
	}

	const patternName = "default"
	err = q.AddPattern(patternName, pattern)
	if err != nil {
		return false, errInvalidPattern
	}

	matches, err := q.MatchesForEvent([]byte(payload))
	if err != nil {
		return false, errMatchingFailure
	}

	for _, m := range matches {
		if m == patternName {
			return true, nil
		}
	}

	return false, errUnexpected
}
