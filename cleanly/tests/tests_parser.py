from cleanly.llm.parser import parse_cleaning_instructions

def test_parser_fill_and_drop():
  steps = parse_cleaning_instructions(
    "Fill missing values in column 'Age' with mean, drop duplicates"
  )
  assert any(step["action"] == "fill_missing" for step in steps)
  assert any(step["action"] == "drop_duplicates" for step in steps)