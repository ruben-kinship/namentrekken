
#SOURCE: https://patrick.wagstrom.net/weblog/2007/11/28/christmas-name-drawing/

:::python
    #!/usr/bin/python

    from sets import Set
    import random

    names=['mom','dad','phil','petra','pete','patrick','kristina']
    invalidpairs={ 'mom': Set(['dad']),
                   'dad': Set(['mom']),
                   'phil': Set(['petra']),
                   'petra': Set(['phil','mom','dad']),
                   'patrick': Set(['kristina']),
                   'kristina': Set(['patrick','mom','dad'])}

    ok = False
    while not ok:
        try:
            # shuffle the names a bit more
            random.shuffle(names)
            pairings = {}
            availablenames = list(names)
            curinvalid = {}
            # cheat and make a copy of the names here
            for person in names:
                curinvalid[person]=Set(invalidpairs.get(person,Set()))
                curinvalid[person].add(person)
            # draw the names
            for person in names:
                pairings[person] = random.choice(list(Set(availablenames).difference(curinvalid.get(person,Set()))))
                availablenames.remove(pairings[person])
                curinvalid[pairings[person]].add(person) # eliminate A=>B, B=>A possibilites
            ok = True
        except IndexError:
            continue

    for key,val in pairings.iteritems():
        print "%s=>%s" % (key, val)
