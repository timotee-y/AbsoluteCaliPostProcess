import xlrd, os
import codecs
from scipy.constants import speed_of_light

def open_xlsx(file, sheet):
    data = xlrd.open_workbook(file)
    table0 = data.sheet_by_name(sheet)
    nrows = table0.nrows
    return table0, nrows

# 输入模拟器和接收机数据的Excel表
# 输出接收机_频点_星号.txt

def calculate(freq, system):
    # try:
        table1, nrows1 = open_xlsx('rinexdata.xlsx', system)
        table2, nrows2 = open_xlsx('simdata.xlsx',freq)
        
        for i in range(0, nrows1 - 1):
            TOW1 = table1.row_values(i)[0]
            satnum1 = table1.row_values(i)[1]
            if system == 'BDS':
                if table1.row_values(i)[2] == '              ':
                    pseB1C = '0'
                else:
                    pseB1C = table1.row_values(i)[2]
                if table1.row_values(i)[3] == '              ' or table1.row_values(i)[3] == '  ':
                    pseB1I = '0'
                else:
                    pseB1I = table1.row_values(i)[3]
                if table1.row_values(i)[4] == '              ' or table1.row_values(i)[4] == '  ':
                    pseB3I = '0'
                else:
                    pseB3I = table1.row_values(i)[4]
                    
                for j in range(0, nrows2 - 1):
                    TOW2 = table2.row_values(j)[0]
                    satnum2 = table2.row_values(j)[1]
                    pse = table2.row_values(j)[2]

                    if TOW1 == TOW2 and satnum1 == satnum2:
                        # if freq == 'L1C':
                        #     delpse = - float(pse) + float(pseL1C) # 纯属偷懒
                        # elif freq == 'L2C':
                        #     delpse = - float(pse) + float(pseL2C)
                        if freq == 'B1I':
                            delpse = - float(pse) + float(pseB1I)
                        elif freq == 'B3I':
                            delpse = - float(pse) + float(pseB3I)
                        elif freq == 'B1C':
                            delpse = - float(pse) + float(pseB1C)
                        timeoffset = float(delpse) / speed_of_light * 1000000000

                        output = ('{}\t{}\t\n').format(TOW1, timeoffset)
                        txtname = freq + '_' + 'C' + str(int(satnum1)) + '.txt'
                        f = codecs.open('./Data/' + txtname, 'a+')
                        f.write(output)
                        f.close()
            elif system == 'GPS':
                if table1.row_values(i)[2] == '              ' or table1.row_values(i)[2] == '  ':
                    pseL1C = '0'
                else:
                    pseL1C = table1.row_values(i)[2]
                if table1.row_values(i)[3] == '              ' or table1.row_values(i)[3] == '  ':
                    pseL2C = '0'
                else:
                    pseL2C = table1.row_values(i)[3]
                    
                for j in range(0, nrows2 - 1):
                    TOW2 = table2.row_values(j)[0]
                    satnum2 = table2.row_values(j)[1]
                    pse = table2.row_values(j)[2]

                    if TOW1 == TOW2 and satnum1 == satnum2:
                        # if freq == 'L1C':
                        #     delpse = - float(pse) + float(pseL1C) # 纯属偷懒
                        # elif freq == 'L2C':
                        #     delpse = - float(pse) + float(pseL2C)
                        if freq == 'L1C':
                            delpse = - float(pse) + float(pseL1C)
                        elif freq == 'L2C':
                            delpse = - float(pse) + float(pseL2C)
                        timeoffset = float(delpse) / speed_of_light * 1000000000

                        output = ('{}\t{}\t\n').format(TOW1, timeoffset)
                        txtname = freq + '_' + 'G' + str(int(satnum1)) + '.txt'
                        f = codecs.open('./Data/' + txtname, 'a+')
                        f.write(output)
                        f.close()
        return True
                
    # except:
    #     return False
    
freqarr = ('B1I', 'B3I', 'B1C', 'L1C', 'L2C')
sysarr = ('GPS', 'BDS')
for i in range (0, 5):
    if i < 3:      
        state = calculate(freqarr[i], 'BDS')
        if state:
            print('Writing for {} done.'.format(freqarr[i]))
        else:
            print('Writing for {} ERROR !!!'.format(freqarr[i]))
    else:
        state = calculate(freqarr[i], 'GPS')
        if state:
            print('Writing for {} done.'.format(freqarr[i]))
        else:
            print('Writing for {} ERROR !!!'.format(freqarr[i]))
# state = calculate('L2C', 'GPS')
# if state:
#     print('Writing for {} done.'.format('L2C'))
# else:
#     print('Writing for {} ERROR !!!'.format('L2C'))
