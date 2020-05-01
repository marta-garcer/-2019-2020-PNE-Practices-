a = "specie?mouse&chromo?16"
separate = a.split("&")   #We need to separate the specie and the chromosome
pair = separate[0].find("?")
specie = pair[1]
pairs = separate[1].find("?")
chromosome = pairs[1]
