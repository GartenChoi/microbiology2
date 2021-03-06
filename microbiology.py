import csv


# com1과 com2 비교
def compare(com1, com2):
    comf1 = open('data/%s_species.csv' % com1, 'r')
    comf2 = open('data/%s_species.csv' % com2, 'r')

    comd1 = {}
    comd2 = {}

    comwtxt = open('result/%s_vs_%s.txt' % (com1, com2), 'w', encoding='utf-8')

    for line in csv.reader(comf1):
        if line[0] == 'Taxon name' or line[0].startswith('PAC00') or line[0].startswith('KE1'): continue
        comd1[line[0]] = int(line[2])

    for line in csv.reader(comf2):
        if line[0] == 'Taxon name' or line[0].startswith('PAC00') or line[0].startswith('KE1'): continue
        try:
            ratio = int(line[2]) / comd1[line[0]] * 100
            # ratio = comd1[line[0]]/int(line[2])
            if ratio > 120:
                comwtxt.write('%s: %g%%로 증가함. %d -> %d \n' % (line[0], ratio, int(comd1[line[0]]), int(line[2])))
            elif ratio < 80:
                comwtxt.write('%s: %g%%로 감소함. %d -> %d \n' % (line[0], ratio, int(comd1[line[0]]),int(line[2])))
            del comd1[line[0]]
        except:
            comd2[line[0]] = int(line[2])
    for key,val in comd2.items():
        comwtxt.write('%s: %s에서 새로 검출됨. 0 -> %d \n' % (key, com2, val))
    for key,val in comd1.items():
        comwtxt.write('%s: %s에서 검출되지 않음. %d -> 0 \n' % (key, com2, val))

if __name__ == "__main__":
    compare('con', 'dn')
    compare('dn', 'con')
    compare('con', 'ex')
    compare('ex', 'con')
    compare('con', 'dnex')
    compare('dnex', 'con')
    compare('dn', 'dnex')
    compare('dnex', 'dn')
    compare('ex', 'dnex')
    compare('dnex', 'ex')
    compare('ex', 'dn')
    compare('dn', 'ex')