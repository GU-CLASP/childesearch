import pandas as pd
import sys

df = pd.read_csv(
    sys.stdin,
    sep="\t",
)

# print("SUM")
# print("----------------")
# .drop(["m", "fn"], axis=1)
print(
    df[["m3", "why_pw_c", "why_pw_a", "because_pw_c", "because_pw_a"]]
    .groupby("m3")
    .mean()
    .multiply(1000)
    .to_csv(sep="\t")
)
print()
# print("STD")
# print("----------------")
# print(
#     df[["m3", "why_pw_c", "why_pw_a", "because_pw_c", "because_pw_a"]]
#     .groupby("m3")
#     .std()
#     .multiply(1000)
# )
