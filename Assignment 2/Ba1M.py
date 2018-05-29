def NumberToPattern (index, k):
   if k == 1:
      return NumberToSymbol(index)
   PrefixIndex = index // 4 #get the prefixindex as 
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
