from csv_value_counter import transform
def test_transform():
 assert transform([{"x":"a"},{"x":"a"}], "x") == {"a":2}
