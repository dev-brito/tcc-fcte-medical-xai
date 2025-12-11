import os

train_val_txt = "./train_val_list.txt"
test_txt = "./test_list.txt"

def obter_ids_pacientes(txt_file):
    ids = set()
    with open(txt_file, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                paciente_id = linha.split("_")[0]
                ids.add(paciente_id)
    return ids

train_val_ids = obter_ids_pacientes(train_val_txt)
test_ids = obter_ids_pacientes(test_txt)

sobreposicao = train_val_ids & test_ids

if sobreposicao:
    print("Sobreposição de pacientes encontrada entre train/val e test:")
    for p in sorted(sobreposicao):
        print(p)
else:
    print("Nenhuma sobreposição de pacientes encontrada.")

