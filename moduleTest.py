import matematikModule  # Module ' leri aktif eder

matematikModule.topla(8,12)
matematikModule.carp(9,7)

import matematikModule as mm # modülü program içi kullanım için yeniden isimlendirir

mm.cikar(80,40)
mm.bol(12,3)
print(mm.costumer["firsName"])

from matematikModule import topla   # modülün içinden topla fonksiyonunu alır sadece

topla(12,80)

from  matematikModule import costumer

print(costumer["age"])
