import pylangacq

reader = pylangacq.Reader.from_files(
    ["./data/030001.cha", "./data/030001.cha"], parallel=False
)

reader = pylangacq.Reader.from_zip(
    "https://childes.talkbank.org/data/Eng-UK/Lara.zip", parallel=False
)

print("-----")
print("Total files:", reader.n_files())

print("-----")
print("Files:")
for ix, file in enumerate(reader.file_paths()):
    print(ix, "\t", file)

print("-----")
print("Participant info:")
for ix, x in enumerate(reader.participants(by_files=True)):
    print(ix, "\t", x)

print("-----")
print("Age info (months):")
for ix, x in enumerate(reader.ages(participant="CHI", months=True)):
    print(ix, "\t", x)

print("-----")
print("Utterances:")
print("\ttotal #")
for ix, x in enumerate(reader.utterances(by_files=True)):
    print(ix, "\t", len(x))
print("\tby CHI #")
for ix, x in enumerate(reader.utterances(by_files=True, participants="CHI")):
    print(ix, "\t", len(x))
print("\t'why' by CHI #")
for ix, x in enumerate(reader.utterances(by_files=True, participants="CHI")):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "why" for tok in utt.tokens]):
            count += 1
    print(ix, "\t", count)
print("\t'why' by anyone #")
for ix, x in enumerate(reader.utterances(by_files=True)):
    count = 0
    for utt in x:
        if any([tok.word.lower() == "why" for tok in utt.tokens]):
            count += 1
    print(ix, "\t", count)


print("-----")
print("Words:")
print("\ttotal #")
for ix, x in enumerate(reader.words(by_files=True)):
    print(ix, "\t", len(x))
print("\tby CHI #")
for ix, x in enumerate(reader.words(by_files=True, participants="CHI")):
    print(ix, "\t", len(x))
