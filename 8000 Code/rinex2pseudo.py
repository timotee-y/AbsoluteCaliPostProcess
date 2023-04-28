import codecs
import bdsWeek as bw

# 输入接收机Rinex
# 输出接收机.txt

def cleanrx(rx, leapsecs):
    f = codecs.open('SEPT2930.22O')
    currentline = f.readline()
    while True:
        try:
            while currentline[0] != '>':
                currentline = f.readline()
                
            timestr = currentline[2:21]
            bdsTOW = bw.getTimeinterval(timestr) - leapsecs
            bdsTOW *= 1000
            
            currentline = f.readline()
            while currentline[0] == 'G':
                satnum = currentline[1:3]
                L1C_pse = currentline[5:17]
                # B2a_pse = currentline[37:49]
                # B1I_pse = currentline[69:81]
                # B3I_pse = currentline[101:113]
                output = ('{}\t{}\t{}\t\n').format(bdsTOW, satnum, L1C_pse)
                txtname = rx + '.txt'  
                g = codecs.open(txtname, 'a+')
                g.write(output)
                g.close()
                currentline = f.readline()
        except:
            print('End of Writing for {}'.format(rx))
            break

cleanrx('SEPT', 345600)