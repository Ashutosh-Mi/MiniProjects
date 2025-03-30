# Test log analyzer (Pandas practice)
import pandas as pd
logs = pd.read_csv("test_logs.csv")
buggy_logs = logs[logs["status"] == "FAIL"].groupby("test_file").count().sort_values(by="status", ascending=False)
print("Top buggy files:\n", buggy_logs.head())