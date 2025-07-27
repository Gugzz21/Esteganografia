from PIL import Image
import os


def texto_para_binario(data):
    """Converte texto para binário"""
    return ''.join(format(ord(i), '08b') for i in data)


def binario_para_texto(binary):
    """Converte binário para texto"""
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


def codificar_imagem(image_name, data, output_name):
    """Codifica dados na imagem"""
    try:
        img = Image.open(image_name)
        binary_data = texto_para_binario(data) + '11111111'  # Marcador de fim

        if len(binary_data) > img.width * img.height * 3:
            print("Erro: Imagem muito pequena para a mensagem!")
            return False

        pixels = list(img.getdata())
        data_index = 0

        for i in range(len(pixels)):
            pixel = list(pixels[i])

            for j in range(3):  # R, G, B
                if data_index < len(binary_data):
                    pixel[j] = pixel[j] & ~1 | int(binary_data[data_index])
                    data_index += 1

            pixels[i] = tuple(pixel)
            if data_index >= len(binary_data):
                break

        new_img = Image.new(img.mode, img.size)
        new_img.putdata(pixels)
        new_img.save(output_name)
        print(f"Mensagem ocultada com sucesso em {output_name}!")
        return True

    except Exception as e:
        print(f"Erro ao codificar: {e}")
        return False


def decodificar_imagem(nome_imagem):
    """Decodifica dados da imagem"""
    try:
        img = Image.open(nome_imagem)
        binary_data = []

        for pixel in img.getdata():
            for channel in pixel[:3]:  # R, G, B
                binary_data.append(str(channel & 1))

            # Verifica se encontrou o marcador de fim
            if len(binary_data) >= 8 and ''.join(binary_data[-8:]) == '11111111':
                break

        # Remove o marcador de fim
        binary_data = binary_data[:-8] if '11111111' in ''.join(binary_data) else binary_data
        message = binario_para_texto(''.join(binary_data))
        return message

    except Exception as e:
        print(f"Erro ao decodificar: {e}")
        return ""


def listar_aquivos(extensões=('.png', '.jpg', '.bmp')):
    """Lista arquivos de imagem na pasta atual"""
    files = [f for f in os.listdir() if f.lower().endswith(extensões)]
    if not files:
        print("Nenhuma imagem encontrada na pasta!")
        return []

    print("\nArquivos disponíveis:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    return files


def main():
    print("=== ESTEGANOGRAFIA SIMPLES ===")
    print("Arquivos devem estar na mesma pasta do projeto\n")

    while True:
        print("\n1. Ocultar mensagem em imagem")
        print("2. Extrair mensagem de imagem")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            files = listar_aquivos()
            if not files:
                continue

            try:
                num = int(input("Número da imagem para codificar: ")) - 1
                image_name = files[num]
            except:
                print("Opção inválida!")
                continue

            data = input("Digite a mensagem para ocultar: ")
            output_name = input("Nome do arquivo de saída (ex: output.png): ")

            if not output_name.lower().endswith(('.png', '.jpg', '.bmp')):
                output_name += '.png'

            codificar_imagem(image_name, data, output_name)

        elif choice == '2':
            files = listar_aquivos()
            if not files:
                continue

            try:
                num = int(input("Número da imagem para decodificar: ")) - 1
                image_name = files[num]
            except:
                print("Opção inválida!")
                continue

            message = decodificar_imagem(image_name)
            print(f"\nMensagem extraída: {message}")

        elif choice == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()