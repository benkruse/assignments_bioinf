def PatternToNumber(pattern):
   if pattern == "":
      return 0
   symbol = pattern[-1]
   prefix = pattern[0:len(pattern)-1]
   return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber (s):
   if s == "A":
      return 0
   elif s == "C":
      return 1
   elif s == "G":
      return 2
   elif s == "T":
      return 3

def ComputingFrequencies (Text, k):#Creates Frequency Array
   FrequencyArray = [0] * 4**k
   for i in range (0, len(Text) - k+1):
      Pattern = Text[i:k+i]
      j = PatternToNumber(Pattern)
      FrequencyArray[j] = FrequencyArray[j] + 1
   return FrequencyArray
