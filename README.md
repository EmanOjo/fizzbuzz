---
module: mark-induction

level: 3

methods:
  - team
  - pair
  - solo

tags:
  - wip
---

# FizzBuzz

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

> This is part of Academy's [technical curriculum for **The Mark**](https://github.com/WeAreAcademy/curriculum-mark). All parts of that curriculum, including this project, are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

FizzBuzz is a coding interview classic. In this project, you're going to write a solution for it and begin using TDD in the process.

## Exercise 1: Producing a solution for FizzBuzz

> 🎯 **Success criterion:** All the tests in `test_fizzbuzz.py` pass

FizzBuzz is both a common children's game and a (slightly clichéd) test of coding competence, which you can [read about on Wikipedia](https://en.wikipedia.org/wiki/Fizz_buzz). (Try to avoid reading too far up on it, though - you may stumble across a solution, which would undermine the learning of this exercise...)

Some specification tests have been written for you in `fizzbuzz_test.py` - it's your job to right the code to make the tests pass.

### Test-Driven Development

It may be the case that you want to add some additional tests. For example, one strategy might be to have a helper function, `to_fizzbuzz`, which returns the FizzBuzz representation of a number.

This is a great opportunity to try [test-driven development (TDD)](https://www.agilealliance.org/glossary/tdd/).

This could look like:

1. Writing a small, simple test for `to_fizzbuzz` _before you write any actual function code_ (e.g. `test_to_fizzbuzz_multiple_of_three`)
2. Writing the function `to_fizzbuzz` to make that test pass
3. Writing a further test (e.g. `test_to_fizzbuzz_multiple_of_five`)
4. Editing the function `to_fizzbuzz` to make this new test pass (and maintaining the pass from the previous test)

and so on, until you have confidence from your tests that your code works as intended.

## Exercise 2: Commentary and reflection

> 🎯 **Success criterion:** documented reflections.
