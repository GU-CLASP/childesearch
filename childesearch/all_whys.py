import pylangacq
import sys

# reader = pylangacq.Reader.from_files(
#     ["./data/030001.cha", "./data/030001.cha"], parallel=False
# )

reader = pylangacq.Reader.from_zip(sys.argv[1], parallel=False)

dt = [dict() for x in range(reader.n_files())]

for ix, file in enumerate(reader.file_paths()):
    # print(ix, "\t", file)
    dt[ix]["filename"] = file


for ix, x in enumerate(reader.utterances(by_files=True)):
    count = 0
    for iu, utt in enumerate(x):
        if any([tok.word.lower() == "why" for tok in utt.tokens]):
            print("{}\t{}\t{}\t{}".format(dt[ix]["filename"],
                                          iu,
                                          utt.participant,
                                          " ".join([t.word for t in utt.tokens])))

    
