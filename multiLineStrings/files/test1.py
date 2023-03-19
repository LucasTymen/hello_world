load_file_in_context('script.py')

try:
  to_you
except NameError:
  fail_tests("Did you define a string called `to_you`?")

expected_string = """
    Stranger, if you passing meet me and desire to speak to me, why
      should you not speak to me?
    And why should I not speak to you?
"""

if set(to_you.split()) != set(expected_string.split()):
  fail_tests("Did you set `to_you` to the given Whitman poem?")

pass_tests()
