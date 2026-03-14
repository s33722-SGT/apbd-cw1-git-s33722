#Zadania GIT

zad5:
nie byl fast-forward bo zmiany pojawily sie na galezi i na main

**1. Kiedy Git wykona fast-forward, a kiedy powstaje merge commit?**
fast - gdy na main nie ma zadnych zmian 
merge commit - gdy obie galezie zostaly zedytowane

**2. Czym w praktyce różni się merge od rebase?**
merge laczy zmiany tworzac nowy commit a rebase przypina galaz do mains

**3. W jaki sposób został rozwiązany konflikt w Twoim repozytorium?**
przy probie merge musialem usunac znaczniki bledu i doprowadzic kod do sensownego stanu, w metodzie przyjmujacej liste liczb return 0 w przypadku bledow jest sensowniejsze niz return None