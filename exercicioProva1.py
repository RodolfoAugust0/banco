dicionario = {"P0000":{"descrição":"acesso aos parametros", "faixa de valores":"0 a 9999", "Página":"5-2"},
              "P0001":{"descrição":"Referencia de velocidade", "faixa de valores":"0 a 65535", "Página":"17-1"},
              "P0002":{"descrição":"velocidade de saida do motor", "faixa de valores":"0 a 65535", "Página":"17-1"},
              "P0003":{"descrição":"corrente do motor", "faixa de valores":"0 a 200.0 A", "Página":"17-1"},
              "P0004":{"descrição":"tensão barram CC(ud)", "faixa de valores":"0 a 2000 V", "Página":"17-1"},
              "P0005":{"descrição":"frequencia de saida", "faixa de valores":"0 a 500.0 Hz", "Página":"17-2"},
              "P0006":{"descrição":"Estado do inversos", "faixa de valores":"0 - ready/ 1- Run /2- Subtensão /3-Falha /4-Autoajuste /5-Configuração /6-Frenagem CC /7-Estado Dormir ", "Página":"17-2"},
              "P0007":{"descrição":"tensão de saida", "faixa de valores":"0 a 2000V", "Página":"17-3"},
              "P0009":{"descrição":"torque do motor", "faixa de valores":"-1000.0 a 1000.0 %", "Página":"17-3"},
              "P0010":{"descrição":"potencia de saida", "faixa de valores":"0 a 6553.5 kW", "Página":"17-4"},
              "P0011":{"descrição":"fator de potencia", "faixa de valores":"-1 a 1", "Página":"17-4"},
              }

for key in dicionario:
    print(key,'-->', dicionario[key])