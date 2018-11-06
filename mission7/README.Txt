Ce programme a été réalisé par Théo Vanden Driessche et Guillaume van der Rest.


Ce programme utilise différente fonctions décrite ci-dessous:
readfile: prend le nom d'un fichier et retourne une liste de toute les lignes de ce fichier
get_words(line): prend un string, une ligne, en argument. Retourne une liste de tout les mots en enlevant la ponctuation
create_index(filename): Retourne un index de tout les mots contenu dans un fichier. (le numéro de la ligne dans laquelle un numéro est contenu)
get_lines: Prend une liste de mots et un index au format (create_index). Retourne les numéros de lignes dans lesquelles tout les mots de la liste ci trouvent.
get_words_same_line: Prend le numéro de ligne et un index au format(create_index). Retourne tout les mots contenus dans cette ligne.
