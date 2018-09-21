#!/usr/bin/python
filepath='/home/xxx/xxx'
with open(filepath+'CDAFILE_2017.BIN','rb') as f1:
    with open(filepath+'BC_MF_CDAPPTR.bin','wb') as fo1:
                with open(filepath+'BC_MF_CDANAME.bin','wb') as fo2:
                        with open(filepath+'BC_MF_CDACERT.bin','wb') as fo3:
                                with open(filepath+'BC_MF_CDAPID.bin','wb') as fo4:
                                        with open(filepath+'BC_MF_CDAASMT.bin','wb') as fo5:
                                                with open(filepath+'BC_MF_CDAGPPB.bin','wb') as fo6:
                                                        with open(filepath+'BC_MF_CDAAINF.bin','wb') as fo7:
                                                                with open(filepath+'BC_MF_CDANDB2.bin','wb') as fo8:
                                                                        with open(filepath+'BC_MF_CDAFTHR.bin','wb') as fo9:
                                                                                with open(filepath+'BC_MF_CDAADDR.bin','wb') as fo10:
                                                                                        b=f1.read(4)
                                                                                        count = int(b.encode('hex'), 16)
                                                                                        while count > 4:

                                                                                                w=f1.read(count-4)
                                                                                                if count==830:
                                                                                                
                                                                                                        m=fo1.write(b)
                                                                                                        n=fo1.write(w)
                                                                                                elif count==59:
                                                                                                
                                                                                                        m=fo2.write(b)
                                                                                                        n=fo2.write(w)
                                                                                                elif count==46:
                                                                                                
                                                                                                        m=fo3.write(b)
                                                                                                        n=fo3.write(w)
                                                                                                elif count==31:
                                                                                                
                                                                                                        m=fo4.write(b)
                                                                                                        n=fo4.write(w)
                                                                                                elif count==288:
                                                                                               
                                                                                                        m=fo5.write(b)
                                                                                                        n=fo5.write(w)
                                                                                                elif count==860:
                                                                                                
                                                                                                        m=fo6.write(b)
                                                                                                        n=fo6.write(w)
                                                                                                elif count==88:
                                                                                                
                                                                                                        m=fo7.write(b)
                                                                                                        n=fo7.write(w)
                                                                                                elif count==390:
                                                                                               
                                                                                                        m=fo8.write(b)
                                                                                                        n=fo8.write(w)
                                                                                                elif count==68:
                                                                                                
                                                                                                        m=fo9.write(b)
                                                                                                        n=fo9.write(w)
                                                                                                elif count==363:
                                                                                                
                                                                                                        m=fo10.write(b)
                                                                                                        n=fo10.write(w)
                                                                                                else: break
                                                                                                b=f1.read(4)
                                                                                                if b == "":
                                                                                                        count = 0
                                                                                                else:
                                                                                                        print count
                                                                                                        count = int(b.encode('hex'), 16)
