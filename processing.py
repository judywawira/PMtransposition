__author__ = 'judywawira'
import pandas as pd
import csv

#b1dobJames
#c1dobJames
#b3c3y2James
#c3dbmbJames
#b3dbmbJames

block = 'c3dbmbJames'
file= '/Users/judywawira/Electives/working/TransposedBlocks/' + block + '.csv'

def all_field_transposition(block,file):
    """
    Method that gets all the fields if a field is transposed, and checks if the transposition is present in all the three names
    """
    df = pd.read_csv(file,delimiter='|')
    mf = []
    for index,row in df.iterrows():
        if row['fntomid'] == 1 and row['lntofn'] ==1 and row['lntomid'] == 1:
            mf.append(row)
    outfile = str('/Users/judywawira/Electives/working/AllTransposed')+ block +'_all.csv'
    myfile = open(outfile, 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter='|')
    wr.writerow(mf)
    print len(mf)
    return 'Success'

def two_names(block,file):
    """
    Method to get transpositions that are two names only
    """
    df = pd.read_csv(file,delimiter='|')
    mf = []
    for index,row in df.iterrows():
        if (row['fntomid'] == 1 and row['lntofn'] ==1 ) or ( row['lntomid'] == 1 and row['fntomid'] == 1) or (row['lntofn'] ==1 and   row['lntomid'] == 1):
            mf.append(row)
    outfile = str('/Users/judywawira/Electives/working/AllTransposed')+ block +'_two.csv'
    myfile = open(outfile, 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter='|')
    wr.writerow(mf)
    print len(mf)
    print 'Success'


#all_field_transposition(block,file)
two_names(block,file)