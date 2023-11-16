#Izveidot Python programmu, kas atkarībā no pašreizējās 
# stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)

import datetime

h=datetime.datetime.now().hour

#konkrēto sevicinājumu pasaka pēc noteiktās stundas
if 5<= h < 12:
    sveiciens = "LABRIT!"
elif 12<= h<18:
    sveiciens = "LABDIEN!"   
else:
    sveiciens="LABVAKAR!"   

print(sveiciens)      