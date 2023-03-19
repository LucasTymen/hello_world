load_file_in_context('script.py')
try:
  total_price
except NameError:
  fail_tests("You didn't define `total_price`.")

if total_price == 20.0:
  fail_tests("Did you use the `+=` operator or just `=`?")

elif abs(109.00 - total_price) > 0.1:
  fail_tests("The `total_price` should be {} but it was {}.".format(109.00, total_price))
pass_tests()
