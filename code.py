L = ['AANLAQGHQSRPHQR','AHSHSYTPTSSQPRP','ANLAQGHQSRPHQRP','APQNNVVSAPTYYTN','APTYYTNYTMPVYTN','AQGHQSRPHQRPSTM','ATSSSQTYAHSHSYT','AWQGNRPLYVQPGDP','CGECRGSGRTRFLLD','CKSCWRRFAPQNNVV','CRGSGRTRFLLDEDI','CSKCGNTGYKLKNGR','DDELPSYEDVIKEEE','DEDICPLCHGVGRII','DICPLCHGVGRIITQ','DTHDDELPSYEDVIK','DVIKEEERLQSQPPR','ECRGSGRTRFLLDED','EDICPLCHGVGRIIT','EDVIKEEERLQSQPP','ELPSYEDVIKEEERL','FLLDEDICPLCHGVG','FYCSKCGNTGYKLKN','GDPRLGGVLCGECRG','GECRGSGRTRFLLDE','GGVLCGECRGSGRTR','GHQSRPHQRPSTMPA','GNRPLYVQPGDPRLG','GNTGYKLKNGRSCKS','GRSCKSCWRRFAPQN','GRTRFLLDEDICPLC','GSGRTRFLLDEDICP','GVLCGECRGSGRTRF','GYKLKNGRSCKSCWR','HDDELPSYEDVIKEE','HQSRPHQRPSTMPAT','HSHSYTPTSSQPRPP','HSYTPTSSQPRPPPR','ICPLCHGVGRIITQP','IKEEERLQSQPPRPP','KCGNTGYKLKNGRSC','KDTHDDELPSYEDVI','KLKNGRSCKSCWRRF','KNGRSCKSCWRRFAP','KSCWRRFAPQNNVVS','LAQGHQSRPHQRPST','LCHGVGRIITQPQRY','LDEDICPLCHGVGRI','LGGVLCGECRGSGRT','LKNGRSCKSCWRRFA','LLDEDICPLCHGVGR','LPSYEDVIKEEERLQ','LPWTYPPRFYCSKCG','LQSQPPRPPRPAANL','LYVQPGDPRLGGVLC','MPATSSSQTYAHSHS','MPVYTNAWQGNRPLY','MSKDTHDDELPSYED','NAWQGNRPLYVQPGD','NGRSCKSCWRRFAPQ','NNVVSAPTYYTNYTM','NPSLPWTYPPRFYCS','NRPLYVQPGDPRLGG','NTGYKLKNGRSCKSC','NYTMPVYTNAWQGNR','PAANLAQGHQSRPHQ','PGDPRLGGVLCGECR','PHQRPSTMPATSSSQ','PLCHGVGRIITQPQR','PLYVQPGDPRLGGVL','PPPRPQQNPSLPWTY','PPRFYCSKCGNTGYK','PPRPAANLAQGHQSR','PPRPPRPAANLAQGH','PPRPQQNPSLPWTYP','PQQNPSLPWTYPPRF','PRFYCSKCGNTGYKL','PRLGGVLCGECRGSG','PRPAANLAQGHQSRP','PRPPPRPQQNPSLPW','PRPPRPAANLAQGHQ','PRPQQNPSLPWTYPP','PSLPWTYPPRFYCSK','PSYEDVIKEEERLQS','PTSSQPRPPPRPQQN','PTYYTNYTMPVYTNA','PVYTNAWQGNRPLYV','PWTYPPRFYCSKCGN','QGHQSRPHQRPSTMP','QGNRPLYVQPGDPRL','QNNVVSAPTYYTNYT','QNPSLPWTYPPRFYC','QPGDPRLGGVLCGEC','QPPRPPRPAANLAQG','QPRPPPRPQQNPSLP','QSQPPRPPRPAANLA','QSRPHQRPSTMPATS','QTYAHSHSYTPTSSQ','RFAPQNNVVSAPTYY','RFLLDEDICPLCHGV','RFYCSKCGNTGYKLK','RGSGRTRFLLDEDIC','RLGGVLCGECRGSGR','RLQSQPPRPPRPAAN','RPAANLAQGHQSRPH','RPHQRPSTMPATSSS','RPLYVQPGDPRLGGV','RPPRPAANLAQGHQS','RPQQNPSLPWTYPPR','RPSTMPATSSSQTYA','RSCKSCWRRFAPQNN','SCKSCWRRFAPQNNV','SCWRRFAPQNNVVSA','SGRTRFLLDEDICPL','SHSYTPTSSQPRPPP','SKCGNTGYKLKNGRS','SLPWTYPPRFYCSKC','SQPPRPPRPAANLAQ','SQPRPPPRPQQNPSL','SQTYAHSHSYTPTSS','SRPHQRPSTMPATSS','SSQTYAHSHSYTPTS','SSSQTYAHSHSYTPT','STMPATSSSQTYAHS','SYEDVIKEEERLQSQ','SYTPTSSQPRPPPRP','TGYKLKNGRSCKSCW','THDDELPSYEDVIKE','TMPVYTNAWQGNRPL','TNAWQGNRPLYVQPG','TNYTMPVYTNAWQGN','TRFLLDEDICPLCHG','TSSQPRPPPRPQQNP','TSSSQTYAHSHSYTP','TYAHSHSYTPTSSQP','TYPPRFYCSKCGNTG','TYYTNYTMPVYTNAW','VIKEEERLQSQPPRP','VQPGDPRLGGVLCGE','VSAPTYYTNYTMPVY','VVSAPTYYTNYTMPV','VYTNAWQGNRPLYVQ','WQGNRPLYVQPGDPR','WTYPPRFYCSKCGNT','YAHSHSYTPTSSQPR','YCSKCGNTGYKLKNG','YEDVIKEEERLQSQP','YKLKNGRSCKSCWRR','YTMPVYTNAWQGNRP','YTNAWQGNRPLYVQP','YTNYTMPVYTNAWQG','LCHGVGRIITQPQRY','YTPTSSQPRPPPRPQ','YVQPGDPRLGGVLCG','YYTNYTMPVYTNAWQ']


next={}
for s in L:
  for i in range(0,len(s)-5):
    next[s[i:i+5]]=s[i+5]
begin = 'MSKDT'
for s in L:
  if 
seq=begin

while True:
      if begin in next:
         n=next[begin]
         seq=seq+n
         begin=begin[1:5]+n
      else:
       break

print (seq)
