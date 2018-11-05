import csv

#com1과 com2 비교
def compare(com1,com2):
    comf1=open('data/%s_species.csv'%com1,'r')
    comf2=open('data/%s_species.csv'%com2,'r')

    comd1={}

    comw=open('result/%s_vs_%s.txt'%(com1,com2),'w',encoding='utf-8')

    for line in csv.reader(comf1):
        if line[2]=='Count':continue
        comd1[line[0]] = int(line[2])

    for line in csv.reader(comf2):
        if line[2]=='Count':continue
        try:
            ratio=comd1[line[0]]/int(line[2])
            if ratio>1.3 or ratio<0.7:
                comw.write('%s: %f만큼 변화함.\n'%(line[0],ratio-1))
            del comd1[line[0]]
        except:comw.write('%s: %s에서 새로 검출됨.\n'%(line[0],com2))
    for key in comd1.keys():
        comw.write('%s: %s에서 검출되지 않음\n'%(key,com2))

compare('con','dn')
compare('dnex','con')
compare('con','ex')