import codecs
import bdsWeek as bw

# 输入接收机Rinex
# 输出接收机.txt

def cleanrx(rx, leapsecs):
    f = codecs.open('SEPT0970.23O')
    currentline = f.readline()
    while True:
        try:
            while currentline[0] != '>':
                currentline = f.readline()
                
            timestr = currentline[2:21]
            timevalue = bw.getTimeinterval(timestr)
            bdsTOW = timevalue[1] - leapsecs
            
            currentline = f.readline()
            while currentline[0] == 'C':
                satnum = currentline[1:3]
                B1C_pse = currentline[5:17]
                B2a_pse = currentline[37:49]
                B1I_pse = currentline[69:81]
                B3I_pse = currentline[101:113]
                
                output1 = ('{}\t{}\t{}\t{}\t{}\t{}\t\n').format(bdsTOW, satnum, B1C_pse, B2a_pse, B1I_pse, B3I_pse)
                txtname1 = rx + '.txt'  
                g = codecs.open(txtname1, 'a+')
                g.write(output1)
                g.close()
                
                currentline = f.readline()
        except:
            print('End of Writing for {}'.format(rx))
            break

cleanrx('SEPT', 18)