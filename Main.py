from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica


p = Pessoa(22, 'Rodrigo', 'Rua Sao Bernardo', 43)
pf = Fisica(22, 'Rodrigo', 'Rua Sao Bernardo', '845796281', '111.222.333-44', 39, 79, 1.74)
pj = Juridica(22, 'Rodrigo', 'Rua Sao Bernardo', '845796281', '29.458.021/0001-57', '02.232.2495-6', 5)

print(pf.getIMC())
pj.imprimeCNPJ()
