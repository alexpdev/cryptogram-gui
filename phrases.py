import pickle

Gwords = pickle.load(open("Gwords/gwords.pickle","rb"))
Pwords = pickle.load(open("Gwords/pwords.pickle","rb"))
Phrases = {
    "O FLQBX BGX IQQND O DGQSPH GCYX PONXH BQ LXCH. BGCB'D CPFCAD IXXU JA LXCDQU RQL FLOBOUZ. TXQTPX FQU'B FLOBX BGX IQQND O FCUB. DQ O GCYX BQ HQ OB RQL JADXPR. - W.D.PXFOD": {"A":"Y"},
    "M DBQZ RT GNTYEMUDKMND DEUD XOXKTBLX EUDXN RX. EX NUMZ M AUN FXMLC KMZMYWQBWN XOXKTBLX EUNL'D RXD RX TXD -KBZLXT ZULCXKIMXQZ":{"O":"V"},
    "TXBR ROQX AB AVXQ BVA. HY GBV KHDAQX AB ABB IVNO UFZHNQ GBV IUG RFHX VL IUTXHE BOAQM LQBLKQ'D IHDAUTPD. - UXX KUXFQMD":{"T":"K"},
    "PAO XN XNVZ MKPMOZ LMCD JN JAD XNNL PADW JAD XNNLQDKK LTWVZ? TJ'S AMLXKO DYDL UNL JADB.": {"X":"D"},
    "JLX WUCXV DWQ KXJ. JLX HWVX DWQ VXPUEIX DWQ TPOOWJ SEO WO JLX EOJXVOXJ. -NXFEO GHEJL" : {"W":"O"},
    "NAS VHV HY WJY MA OXYJ MA MAAF? HY'M FHWNY EJZADJ HY'M XZYJDFAAF. VJIJUEJD HM NJDJ EJZADJ HY'M TKFJ. -VD. MJKMM":{"A":"O"}
}

short_words = ["THE","OF","AND","TO","IN","A","IS","THAT","FOR","IT","AS","WAS","WITH","BE","BY","ON","NOT","HE","I","THIS","ARE","OR","HIS","FROM","AT","WHICH","BUT","HAVE","AN","HAD","THEY","YOU","WERE","THEIR","ONE","ALL","WE","CAN","HER","HAS","THERE","BEEN","IF","MORE","WHEN","WILL","WOULD","WHO","SO","NO","SHE","OTHER","ITS","MAY","THESE","WHAT","THEM","THAN","SOME","HIM","TIME","INTO","ONLY","DO","SUCH","MY","NEW","ABOUT","OUT","ALSO","TWO","ANY","UP","FIRST","COULD","OUR","THEN","MOST","SEE","ME","SHOULD","AFTER","SAID","YOUR","VERY","BETWEEN","MADE","MANY","OVER","LIKE","THOSE","DID","NOW","EVEN","WELL","WHERE","MUST","PEOPLE","THROUGH","HOW","SAME","WORK","BEING","BECAUSE","MAN","LIFE","BEFORE","EACH","MUCH","UNDER","YEARS","WAY","GREAT","STATE","BOTH","USE","UPON","OWN","USED","HOWEVER","US","PART","GOOD","WORLD","MAKE","THREE","WHILE","LONG","DAY","WITHOUT","JUST","MEN","GENERAL","DURING","ANOTHER","LITTLE","FOUND","HERE","SYSTEM","DOES"]
