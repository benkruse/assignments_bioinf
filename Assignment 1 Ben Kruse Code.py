def generate_k_mer_list (Text, k):
   k_mer_list = []
   for a in range (0, len(Text)-k+1):
      k_mer_list  += [Text[a:k+a]]
   return k_mer_list

def generate_Counter_list (k_mer_list): #def generate_Counter_list (Text, k):
   Counter_list = []
   #k_mer_list = generate_k_mer_list (Text, k)
   for b in range (0, len(k_mer_list)):
      Counter = 0
      for c in k_mer_list[0:b+1]:
         if c == k_mer_list[b]:
            Counter += 1
      Counter_list += [Counter]
   return Counter_list

def most_frequent_k_mer (Text, k):
   k_mer_list = generate_k_mer_list (Text, k)
   Counter_list = generate_Counter_list (k_mer_list) #by using the already generated k_mer_list instead of creating a new one how it was programmed initially, a second creation of the k-mer list is avoided shortening runtime  
   most_frequent_k_mer_list = []
   for d in range (0, len(Counter_list)):
      if Counter_list[d] == max(Counter_list):
         most_frequent_k_mer_list += [[k_mer_list[d]] + [Counter_list[d]]]
   return most_frequent_k_mer_list
