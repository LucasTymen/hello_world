load_file_in_context('script.py')

expected_string = "The wind, which had hitherto carried us along with amazing rapidity, sank at sunset to a light breeze; the soft air just ruffled the water and caused a pleasant motion among the trees as we approached the shore, from which it wafted the most delightful scent of flowers and hay."

try:
  full_equality('message', expected_string)
except NameError:
  fail_tests("`message` needs to be defined.")

pass_tests()
