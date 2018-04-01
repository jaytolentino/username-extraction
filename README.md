# Username Extraction Problem Submission

This is a more detailed submission for a username extraction problem. Since this repo is public, I will refrain from adding too many details here about the project.

## To run

1. Clone this repository to your local machine.
2. Navigate into the main directory of this project. Replace the path below with your local path

```
$ cd your/path/to/username-extraction
```

3. You can simply run the project by calling the `autocomplete.py` script:

```
$ python ./autocomplete.py
```

4. You can also check out some of the tests used while developing this project by calling the test script:

```
$ python ./autocomplete.test.py
```

## Future Development

### Optimizing performance

This solution does cut out some unnecessary query calls by skipping any possible usernames before the last returned query value (since the last returned value would by the latest alphabetically). It would be good though to further examine possible areas to reduce the amount of recursion used since this does occasionally cause this `RuntimeError`:

```
RuntimeError: maximum recursion depth exceeded while calling a Python object
```

That error is avoided only in the "deeply recursive database" test by increasing the recursion limit, though there may be some opportunity to avoid it there.

### More test coverage

If I'd revisit this project, I'd add better test coverage around the different utility functions. There exist some for the `increment()` function mostly out of necessity while developing.

### Exploring support for other characters

A possible area for expansion is adding some support for other characters. The current character support (a-z) was dictated by the prompt, and I unfortunately didn't make it too easy to make that change in the future. But it could be interesting in a practical sense if this were used in the real world. Many sites do allow the use of uppercase, numbers, and some symbols (like '.').
