import csv


# com1과 com2 비교
def compare(com1, com2):
    comf1 = open('data/%s_species.csv' % com1, 'r')
    comf2 = open('data/%s_species.csv' % com2, 'r')

    comd1 = {}
    coml2 = []

    comwtxt = open('result/%s_vs_%s.txt' % (com1, com2), 'w', encoding='utf-8')
    comwhtml = open('result/%s_vs_%s.html' % (com1, com2), 'w', encoding='utf-8')

    comwhtml.write('<html><head><style>.up{color:#800} .down{color:#008}</style></head><body>')

    for line in csv.reader(comf1):
        if line[2] == 'Count': continue
        comd1[line[0]] = int(line[2])

    for line in csv.reader(comf2):
        if line[2] == 'Count': continue
        try:
            ratio = int(line[2]) / comd1[line[0]] * 100 - 100
            # ratio = comd1[line[0]]/int(line[2])
            if ratio > 20:
                comwtxt.write('%s: %g%% 증가함.\n' % (line[0], ratio))
                comwhtml.write('<div class="up">%s: %g%% 증가함.</div>' % (line[0], ratio))
            elif ratio < -20:
                comwtxt.write('%s: %g%% 감소함.\n' % (line[0], - ratio))
                comwhtml.write('<div class="down">%s: %g%% 감소함.</div>' % (line[0], - ratio))
            del comd1[line[0]]
        except:
            coml2.append(line[0])
    for name in coml2:
        comwtxt.write('%s: %s에서 새로 검출됨.\n' % (name, com2))
        comwhtml.write('<div class="up">%s: %s에서 새로 검출됨.</div>' % (name, com2))
    for key in comd1.keys():
        comwtxt.write('%s: %s에서 검출되지 않음\n' % (key, com2))
        comwhtml.write('<div class="down">%s: %s에서 검출되지 않음</div>' % (key, com2))

    comwhtml.write('</body></html>')

if __name__ == "__main__":
    compare('con', 'dn')
    compare('dnex', 'con')
    compare('con', 'ex')
