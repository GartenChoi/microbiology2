import csv


# com1과 com2 비교
def compare(com1, com2):
    comf1 = open('data/%s_species.csv' % com1, 'r')
    comf2 = open('data/%s_species.csv' % com2, 'r')

    comd1 = {}
    comd2 = {}

    comwtxt = open('result/%s_vs_%s.txt' % (com1, com2), 'w', encoding='utf-8')
    comwhtml = open('result/%s_vs_%s.html' % (com1, com2), 'w', encoding='utf-8')

    comwhtml.write('<html><head><style>.up{color:#800} .down{color:#008}</style></head><body>')

    for line in csv.reader(comf1):
        if line[2] == 'Count': continue
        comd1[line[0]] = int(line[2])

    for line in csv.reader(comf2):
        if line[2] == 'Count': continue
        try:
            ratio = int(line[2]) / comd1[line[0]] * 100
            # ratio = comd1[line[0]]/int(line[2])
            if ratio > 120:
                comwtxt.write('%s: %g%%로 증가함.\n' % (line[0], ratio))
                comwhtml.write('<div class="up">%s: %g%%로 증가함.</div>' % (line[0], ratio))
            elif ratio < 80:
                comwtxt.write('%s: %g%%로 감소함.\n' % (line[0], ratio))
                comwhtml.write('<div class="down">%s: %g%%로 감소함.</div>' % (line[0], ratio))
            del comd1[line[0]]
        except:
            comd2[line[0]] = int(line[2])
    for key,val in comd2.items():
        comwtxt.write('%s: %s에서 새로 검출됨. count %d \n' % (key, com2, val))
        comwhtml.write('<div class="up">%s: %s에서 새로 검출됨. count %d </div>' % (key, com2, val))
    for key,val in comd1.items():
        comwtxt.write('%s: %s에서 검출되지 않음. count %d \n' % (key, com2, val))
        comwhtml.write('<div class="down">%s: %s에서 검출되지 않음 count %d </div>' % (key, com2, val))

    comwhtml.write('</body></html>')

if __name__ == "__main__":
    compare('con', 'dn')
    compare('dnex', 'con')
    compare('con', 'ex')
