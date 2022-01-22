def permutation(string):
  permutation(string,"")

def permutation(string, prefix):
  if len(string) == 0:
    print(prefix)
  else:
    for i in range(len(string)):
      rem = string[0:i] + string[i+1:]
      #print("rem: "+rem)
      #print("prefix: "+ prefix)
      permutation(rem,prefix+string[i])


permutation("ab","")