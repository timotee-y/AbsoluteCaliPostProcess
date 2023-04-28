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

# getSimData & 2'satnum.txt'
def calculation():
    table1, nrows1 = open_xlsx('simdata.xlsx', 'Sheet1')
    table2, nrows2 = open_xlsx('rinexdata.xlsx', 'Sheet1')

    # traverse rinex data
    for i in range(1, nrows1 - 1):
        TOW1 = table1.row_values(i)[0]
        satnum1 = table1.row_values(i)[1]
        pseu_sim = table1.row_values(i)[2]
        
        # traverse simulator data
        for j in range(0, nrows2 - 1):
            TOW2 = table2.row_values(j)[0]
            satnum2 = table2.row_values(j)[1]
            pse = table2.row_values(j)[2]

            if TOW1 == TOW2 and satnum1 == satnum2:
                delpse = float(pse) - float(pseu_sim)
                timeoffset = float(delpse) / speed_of_light * 1000000000

                output = ('{}\t{}\t\n').format(TOW1, timeoffset)
                txtname = './Data/' + 'G' + str(int(satnum1)) + '.txt'
                f = codecs.open(txtname, 'a+')
                f.write(output)
                f.close()
                
calculation()