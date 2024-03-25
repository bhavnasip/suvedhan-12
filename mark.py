import pandas as pd
d={'Arun':65,'Bala':91,'Charan':74,'Dinesh':80,'Usha':85}
s=pd.Series(d)
print(s[s>75])
