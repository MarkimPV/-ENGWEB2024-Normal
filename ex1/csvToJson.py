
import csv
import json
 
def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath,'r',encoding="utf8") as csvf:
        csvReader = list(csv.reader(csvf, delimiter=";"))
        for rows in csvReader:
            print(1)
            dic = {"_id" : rows[0],
                "nAnuncio" : rows[1],
                "tipoprocedimento" : rows[2],
                "objectoContrato" : rows[3],
                "dataPublicacao" : rows[4],
                "dataCelebracaoContrato" : rows[5], 
                "precoContratual" : rows[6],
                "prazoExecucao" : rows[7],
                "NIPC_entidade_comunicante": rows[8],
                "entidade_comunicante": rows[9],
                "fundamentacao": rows[10]}
            data.append(dic)
        
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'C:\Users\marco\Desktop\UNI\EngWeb\ENGWEB2024-Normal\ENGWEB2024-Normal\ex1\contratos2024.csv'
jsonFilePath = r'C:\Users\marco\Desktop\UNI\EngWeb\ENGWEB2024-Normal\ENGWEB2024-Normal\ex1\contratos2024.json'


make_json(csvFilePath, jsonFilePath)