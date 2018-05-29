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

def NumberToPattern (index, k):
   if k == 1:
      return NumberToSymbol(index)
   PrefixIndex = index // 4
   r = index % 4
   symbol = NumberToSymbol(r)
   PrefixPattern = NumberToPattern(PrefixIndex, k-1)
   return PrefixPattern + symbol

def NumberToSymbol (s):
   if s == 0:
      return "A"
   if s == 1:
      return "C"
   if s == 2:
      return "G"
   if s == 3:
      return "T"

def ComputingFrequencies (Text, k):#Creates Frequency Array
   FrequencyArray = [0] * 4**k
   for i in range (0, len(Text) - k+1):
      Pattern = Text[i:k+i]
      j = PatternToNumber(Pattern)
      FrequencyArray[j] = FrequencyArray[j] + 1
   return FrequencyArray
   
def FasterFrequentWords (Text, k):#Returns all most frequent k-mers in given base sequence "text" and the their frequency at the end. 
   FrequentPatterns = []
   FrequencyArray = ComputingFrequencies (Text, k)
   maxCount = max(FrequencyArray)
   for i in range(0, len(FrequencyArray)):
      if FrequencyArray[i] == maxCount:
         Pattern = [NumberToPattern(i,k)]
         FrequentPatterns = FrequentPatterns + Pattern
   #return FrequentPatterns + ["all these", k, "-mers have been found", maxCount, "times."]
   return FrequentPatterns + [maxCount]
   
