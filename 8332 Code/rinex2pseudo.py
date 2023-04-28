import codecs
import bdsWeek as bw

# 输入接收机Rinex
# 输出接收机.txt

def cleanrx():
    f = codecs.open('./SEPT3360.22O', 'r')
    currentline = f.readline()
    while True:
        try:
            while currentline[0] != '>':
                currentline = f.readline()
                
            timestr = currentline[2:21]
            utcTOW = bw.getTimeinterval(timestr)[1] - 18
            
            currentline = f.readline()
            while currentline[0] == 'C' or currentline[0] == 'G':
                if currentline[0] =='C':
                    satnum = currentline[1:3]
                    if currentline[0] == 'C':
                        satnum = currentline[1:3]
                        B1C_pse = currentline[5:17]
                        B1I_pse = currentline[37:49]
                        B3I_pse = currentline[69:81]
                        output = ('{}\t  {}\t  {}\t  {}\t  {}\t\n').format(utcTOW, satnum, B1C_pse, B1I_pse, B3I_pse)            
                    txtname = '8332BDS.txt'  
                    g = codecs.open(txtname, 'a+')
                    g.write(output)
                    g.close()
                    
                elif currentline[0] =='G':
                    satnum = currentline[1:3]
                    L1C_pse = currentline[5:17]
                    L2C_pse = currentline[37:49]
                    output = ('{}\t  {}\t  {}\t  {}\t\n').format(utcTOW, satnum, L1C_pse, L2C_pse)            
                    txtname = '8332GPS.txt'  
                    h = codecs.open(txtname, 'a+')
                    h.write(output)
                    h.close()
                    
                currentline = f.readline()    
        except:
            print('End of Writing for 8332')
            break

cleanrx()