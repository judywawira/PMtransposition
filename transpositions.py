__author__ = 'judywawira'

#b1dobJames
#c1dobJames
#b3c3y2James
#c3dbmbJames
#b3dbmbJames

import pandas as pd
#infile = '/Users/judywawira/Electives/working/b1dobJames'
infile = '/linkage/transformation_manual_review/new calculation output/new_output_with_header.txt'
outfile = '/linkage/transformation_manual_review/new calculation output/new_output_with_header.txt.out'
block = 'all'

def gettransposition(infile,outfile):
    """
    Method to identify whether there is a transposition and the type of transposition
    """
    df = pd.read_csv(infile,delimiter = '|')
    df['transposed'] = (0)
    df['fntomid'] = 0
    df['lntofn'] = 0
    df['lntomid'] = 0

    rowcount = 0
    lntomidcount = 0
    lntofncount = 0
    fntomidcount = 0

    print len(df.index)
    for index,row in df.iterrows():
        ln1 = row['ln']
        ln2 = row['ln2']
        mid1 = row['mid']
        mid2=row['mid2']
        fn2 = row['fn2']
        fn1 = row['fn']

        #fn to mid
        if (fn1 == mid2 and fn1 != mid1) or (fn2 == mid1 and fn2 != mid2):
            df.ix[rowcount,'transposed'] = 1
            df.ix[rowcount,'fntomid'] = 1
            fntomidcount += 1

        #ln to fn
        if (ln1 == fn2 and ln1 != fn1) or (ln2 == fn1 and ln2 != fn2):
            df.ix[rowcount,'transposed'] = 1
            df.ix[rowcount,'lntofn'] = 1
            lntofncount += 1

        #ln to mid
        if (ln1 == mid2 and ln1 != mid1 ) or (ln2 == mid1 and ln2 != mid2) :
            df.ix[rowcount,'transposed']=1
            df.ix[rowcount,'lntomid'] = 1
            lntomidcount += 1

        rowcount += 1
        #print rowcount
    print fntomidcount,lntofncount,lntomidcount
    #transpositioncounts(fntomidcount,lntofncount,lntomidcount)
    df.to_csv(outfile,sep='|')

    writepreprocessedfile(outfile)
    return 'completed mapping!'

def transpositioncounts (fntomidcount,lntofncount,lntomidcount):
    """
    Method to write out a csv with the various counts
    """
    dfcount = pd.DataFrame()
    dfcount['fntomid'] = fntomidcount
    dfcount['lntomid'] = lntomidcount
    dfcount['lntofn'] = lntofncount
    outfile = str('/linkage/transformation_manual_review/new calculation output/') + block +'.csv'
    dfcount.to_csv(outfile,sep='|')

def writepreprocessedfile(infile):
    """
    Method to select the rows with transposed values and write them out into a new CSV
    """
    block = 'all'
    df = pd.read_csv(infile,delimiter='|')
    mf = df[df['transposed']==1]
    print len(mf.index)
    outfile = '/linkage/transformation_manual_review/new calculation output/new_output_with_header.txt.out'
    #outfile = str('/linkage/transformation_manual_review/new calculation output/')+ block + '.csv'
    mf.to_csv(outfile,sep='|')

gettransposition(infile,outfile)
