import sys
import os
import pandas as pd

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 remove_nan.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train_no_nan.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def remove_nan(fd_in, fd_out):
    df = pd.read_csv(fd_in)

    # Drop rows with any NaN values
    df = df.dropna()

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(fd_out, index=False)

with open(f_input, 'r', encoding="utf8") as fd_in:
    with open(f_output, "w", encoding="utf8") as fd_out:
        remove_nan(fd_in, fd_out)

