import pylangacq
import sys

# reader = pylangacq.Reader.from_files(
#     ["./data/030001.cha", "./data/030001.cha"], parallel=False
# )

reader = pylangacq.Reader.from_zip(sys.argv[1], parallel=False)

# print("-----")
# print("Total files:", reader.n_files())
dt = [dict() for x in range(reader.n_files())]

# print("-----")
# print("Files:")
for ix, file in enumerate(reader.file_paths()):
    # print(ix, "\t", file)
    dt[ix]["filename"] = file


# print("-----")
# print("Participant info:")
for ix, x in enumerate(reader.participants(by_files=True)):
    # print(ix, "\t", x)
    dt[ix]["participants"] = x


# print("-----")
# print("Age info (months):")
for ix, x in enumerate(reader.ages(participant="CHI", months=True)):
    # print(ix, "\t", x)
    dt[ix]["months"] = x

# print("-----")
# print("Utterances:")
# print("\ttotal #")
for ix, x in enumerate(reader.utterances(by_files=True)):
    # print(ix, "\t", len(x))
    dt[ix]["utt_total"] = len(x)

# print("\tby CHI #")
for ix, x in enumerate(reader.utterances(by_files=True, participants="CHI")):
    # print(ix, "\t", len(x))
    dt[ix]["utt_chi"] = len(x)

# print("\t'why' by CHI #")
for ix, x in enumerate(reader.utterances(by_files=True, participants="CHI")):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "why" for tok in utt.tokens]):
            count += 1
    # print(ix, "\t", count)
    dt[ix]["utt_why_chi"] = count

# print("\t'why' by anyone #")
for ix, x in enumerate(reader.utterances(by_files=True)):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "why" for tok in utt.tokens]):
            count += 1
    # print(ix, "\t", count)
    dt[ix]["utt_why_all"] = count

# print("\t'because' by CHI #")
for ix, x in enumerate(reader.utterances(by_files=True, participants="CHI")):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "because" for tok in utt.tokens]):
            count += 1
    # print(ix, "\t", count)
    dt[ix]["utt_because_chi"] = count

# print("\t'because' by anyone #")
for ix, x in enumerate(reader.utterances(by_files=True)):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "because" for tok in utt.tokens]):
            count += 1
    # print(ix, "\t", count)
    dt[ix]["utt_because_all"] = count


# print("-----")
# print("Words:")
# print("\ttotal #")
# for ix, x in enumerate(reader.words(by_files=True)):
#     # print(ix, "\t", len(x))
#     dt[ix]["words_all"] = len(x)

# print("\tby CHI #")
for ix, x in enumerate(reader.words(by_files=True, participants="CHI")):
    # print(ix, "\t", len(x))
    dt[ix]["words_chi"] = len(x)
    count = 0
    for w in x:
        if w.lower() == "why":
            count += 1
    dt[ix]["words_why_chi"] = count
for ix, x in enumerate(reader.words(by_files=True)):
    # print(ix, "\t", len(x))
    dt[ix]["words_all"] = len(x)
    count = 0
    for w in x:
        if w.lower() == "why":
            count += 1
    dt[ix]["words_why_all"] = count

for ix, x in enumerate(reader.words(by_files=True, participants="CHI")):
    count = 0
    for w in x:
        if w.lower() == "because":
            count += 1
    dt[ix]["words_because_chi"] = count
for ix, x in enumerate(reader.words(by_files=True)):
    count = 0
    for w in x:
        if w.lower() == "because":
            count += 1
    dt[ix]["words_because_all"] = count

print(
    "\t".join(
        [
            "fn",
            "m",
            "m3",
            "w_c",
            "w_a",
            "why_c",
            "why_a",
            "why_pw_c",
            "why_pw_a",
            "because_c",
            "because_a",
            "because_pw_c",
            "because_pw_a",
        ]
    )
)

for row in dt:
    if (row["words_chi"] != 0) and (row["words_all"] - row["words_chi"] != 0):
        if row["months"]:
            print(
                "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
                    row["filename"],
                    row["months"],
                    (row["months"] // 3) * 3,
                    row["words_chi"],
                    (row["words_all"] - row["words_chi"]),
                    row["words_why_chi"],
                    (row["words_why_all"] - row["words_why_chi"]),
                    row["words_why_chi"] / row["words_chi"],
                    (row["words_why_all"] - row["words_why_chi"])
                    / (row["words_all"] - row["words_chi"]),
                    row["words_because_chi"],
                    (row["words_because_all"] - row["words_because_chi"]),
                    row["words_because_chi"] / row["words_chi"],
                    (row["words_because_all"] - row["words_because_chi"])
                    / (row["words_all"] - row["words_chi"]),
                )
            )
