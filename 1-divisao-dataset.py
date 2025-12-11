import os
import shutil

base_dir = "."
images_dir = os.path.join(base_dir, "images")
all_images_dir = os.path.join(images_dir, "all_images")

train_txt = os.path.join(base_dir, "train_val_list.txt")
test_txt = os.path.join(base_dir, "test_list.txt")

chestx_dir = os.path.join(images_dir, "ChestX-ray8")
train_dir = os.path.join(chestx_dir, "train")
test_dir = os.path.join(chestx_dir, "test")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

def copiar_imagens(lista_txt, destino):
    copiados, faltando = 0, 0
    with open(lista_txt, "r") as f:
        imagens = [linha.strip() for linha in f if linha.strip()]

    for img in imagens:
        src = os.path.join(all_images_dir, img)
        dst = os.path.join(destino, img)

        if os.path.exists(src):
            shutil.copy2(src, dst)
            copiados += 1
        else:
            print(f"Arquivo não encontrado: {src}")
            faltando += 1
    return copiados, faltando

print("Iniciando cópia...")
train_copiados, train_faltando = copiar_imagens(train_txt, train_dir)
test_copiados, test_faltando = copiar_imagens(test_txt, test_dir)

print("\nFinalizado!")
print(f"Train: {train_copiados} copiadas, {train_faltando} faltando")
print(f"Test:  {test_copiados} copiadas, {test_faltando} faltando")

