import re

def parse_cleaning_instructions(instruction: str):
  steps = []
  
  fill_match = re.search(r"fill missing.*column\s+'(.+?)'.*?(mean|median|mode)?", instruction, re.IGNORECASE)
  
  if fill_match:
    column = fill_match.group(1)
    strategy = fill_match.group(2) if fill_match.group(2) else "mean"
    steps.append({"action": "fill_missing", "column":column, "strategy": strategy})
    
  if "drop_duplicates" in instruction.lower():
    steps.append({"action": "drop_duplicates"})
      
  encode_match = re.search(r"encode column\s+'(.+?)'.*?(label|onehot)?", instruction, re.IGNORECASE)
  if encode_match:
    column = encode_match.group(1)
    method = encode_match.group(2) if encode_match.group(2) else "label"
    steps.append({"action": "encode_columns", "column": column, "method": method})
      
  return steps