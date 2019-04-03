Def character_Deletions(s)
S= ['A','A','B','A','A','B']
 If s.count(s[0])== Len(s)
 return Len(s)-1
 i =0
 n= Len(s)
 Pr = ' '
 Count = 0
 While (I < n) :
    If s[1] == Pr:
       Del s[1]
       Count +=1
     Pr = s[1]
     I += 1
return count
