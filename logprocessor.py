import numpy as np, scipy.stats as st


def files2dict(files):
    logs = {}
    for f in files:
        with open(f, 'r') as fd:
            logs[f] = {}
            for line in fd.readlines():
                line = line.strip()
                if line.startswith("#") or line == "":
                    continue

                line = line.split()
                if logs[f].keys == []:
                    for field in line.split():
                        logs[f][field] = []
                    continue

                for i, results in line.split():
                    logs[f].keys()[i] = results

    return logs

def files2list(files):
    all_lines = []
    fields = {}
    for f in files:
        fields[f] = None
        with open(f,'r') as fd:
            for line in fd.readlines():
                line = line.strip()
                if line.startswith("#") or line == "":
                    continue

                line = line.split()
                if fields[f] == None:
                    fields[f] = ["FILE"]
                    fields[f] += line
                    continue
                all_lines.append([f]+line)
    return all_lines, fields


"""
sum of the "field" values of all lines for which the indexes are equal
"""
def sum_per_indexes(all_lines, fields_per_file, indexe, field):
    indexes = {}
    for f in fields_per_file:
        indexes[f] = []
        for i in indexe:
            indexes[f].append(fields_per_file[f].index(i))


    sums = {}
    #j'ai toutes les lignes, je veux la sum de "field" classées par indexes
    for line in all_lines:
        #je récup le field qui m'intéresse
        value_field_index_number = fields_per_file[line[0]].index(field)
        value = float(line[value_field_index_number])
        # je récupère les indexes associés
        value_index = []
        for i in indexes[line[0]]:
            value_index.append(line[i])
        # je l'insère dans le dict
        wk_sums = sums
        for i in value_index[:-1]:
            if i not in wk_sums:
                wk_sums[i] = {}
            wk_sums = wk_sums[i]
        wk_sums[value_index[-1]] = wk_sums.get(value_index[-1], 0) + value
    return sums

def mean_dict(sums):
    d = dict(sums)
    for x in d:
        if type(d[x]) is dict:
            d[x] = mean_dict(d[x])
        else:
            d[x] = d[x] / nb
    return d


def max_dict(d, indexes, keys=[]):
    # d = dict(d)
    maxes = {}
    for x in d:
        if type(d[x]) is dict:
            maxes.update(max_dict(d[x], indexes, keys+[x]))
        else:
            l = []
            for i in indexes:
                l.append(keys[i])
            wd = maxes
            for k in l[:-1]:
                if k not in wd:
                    wd[k] = {}
                wd = wd[k]
            wd[l[-1]] = max(wd.get(l[-1], -1), d[x])

            #print(d[x], keys+[x])
    return maxes

"""
sum of the "field" values of all lines for which the indexes are equal
"""
def means_per_indexes(all_lines, fields_per_file, indexe, field):
    indexes = {}
    for f in fields_per_file:
        indexes[f] = []
        for i in indexe:
            indexes[f].append(fields_per_file[f].index(i))


    sums = {}
    #j'ai toutes les lignes, je veux la sum de "field" classées par indexes
    for line in all_lines:
        #je récup le field qui m'intéresse
        value_field_index_number = fields_per_file[line[0]].index(field)
        value = float(line[value_field_index_number])
        # je récupère les indexes associés
        value_index = []
        for i in indexes[line[0]]:
            value_index.append(line[i])
        # je l'insère dans le dict
        wk_sums = sums
        for i in value_index[:-1]:
            if i not in wk_sums:
                wk_sums[i] = {}
            wk_sums = wk_sums[i]
        wk_sums[value_index[-1]] =\
        (wk_sums.get(value_index[-1], (0,0))[0] + value, wk_sums.get(value_index[-1], (0,0))[1] + 1)
    sums = mean_dict_tuple(sums)
    return sums

def mean_dict_tuple(sums):
    d = dict(sums)
    for x in d:
        if type(d[x]) is dict:
            d[x] = mean_dict_tuple(d[x])
        else:
            d[x] = d[x][0] / d[x][1]
    return d


def mean_dict(sums, nb):
    d = dict(sums)
    for x in d:
        if type(d[x]) is dict:
            d[x] = mean_dict(d[x])
        else:
            d[x] = d[x] / nb
    return d


def max_dict(d, indexes, keys=[]):
    # d = dict(d)
    maxes = {}
    for x in d:
        if type(d[x]) is dict:
            maxes.update(max_dict(d[x], indexes, keys+[x]))
        else:
            l = []
            for i in indexes:
                l.append(keys[i])
            wd = maxes
            for k in l[:-1]:
                if k not in wd:
                    wd[k] = {}
                wd = wd[k]
            wd[l[-1]] = max(wd.get(l[-1], -1), d[x])

            #print(d[x], keys+[x])
    return maxes


def list_per_indexes(all_lines, fields_per_file, indexe, field):
    indexes = {}
    for f in fields_per_file:
        indexes[f] = []
        for i in indexe:
            indexes[f].append(fields_per_file[f].index(i))


    sums = {}
    #j'ai toutes les lignes, je veux la sum de "field" classées par indexes
    for line in all_lines:
        #je récup le field qui m'intéresse
        value_field_index_number = fields_per_file[line[0]].index(field)
        value = float(line[value_field_index_number])
        # je récupère les indexes associés
        value_index = []
        for i in indexes[line[0]]:
            value_index.append(line[i])
        # je l'insère dans le dict
        wk_sums = sums
        for i in value_index[:-1]:
            if i not in wk_sums:
                wk_sums[i] = {}
            wk_sums = wk_sums[i]
        wk_sums[value_index[-1]] =\
        wk_sums.get(value_index[-1], []) + [value]
    return sums



def mustaches(sums):
    d = dict(sums)
    for x in d:
        if type(d[x]) is dict:
            d[x] = mustaches(d[x])
        else:
            d[x] = st.t.interval(0.95, len(d[x])-1, loc=np.mean(d[x]), scale=st.sem(d[x]))
    return d

def mustaches_per_indexes(all_lines, fields_per_file, indexe, field):
    d = list_per_indexes(all_lines, fields_per_file, indexe, field)
    m = mustaches(d)
    print(m)
    return m
