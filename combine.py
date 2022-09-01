def read(filename):
  words = set()
  with open(filename, 'r') as fin:
    for line in fin:
      if line.rstrip():
        words.add(line.rstrip())
  return words

def main():
  filenames = (
    "goto456/baidu_stopwords.txt",
    "goto456/cn_stopwords.txt",
    "goto456/hit_stopwords.txt",
    "goto456/scu_stopwords.txt",
  )
  out_file = "stopwords.txt"

  total = set()
  for filename in filenames:
    words = read(filename)
    print("Read {} words from file: {}".format(len(words), filename))
    total = total | words

  print("Save {} words to file: {}".format(len(total), out_file))
  with open(out_file, 'w') as fout:
    for w in sorted(total):
      fout.write(w+'\n')
  print("Better to have a look at the combined file and modify accordingly.")
  print("Finished!")

if __name__ == "__main__":
  main()
