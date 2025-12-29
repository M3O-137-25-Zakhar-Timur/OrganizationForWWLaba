from Zahar_pz.pz_3.Cipher import AtbashCipher, CipherManager, CaesarCipher, CipherDescriptor

print("=== Шифр Цезаря ===")
caesar = CaesarCipher("Кафедре 317 пламенный привет!")
print(f"Исходный текст: {caesar.text}")
print(f"Зашифрованный (shift=5): {caesar.encrypt()}")
print(f"Дешифрованный: {caesar.decrypt(caesar.encrypt())}")

caesar.text = "Питончик програем йоу йоу !!!"
print(f"\nНовый текст: {caesar.text}")
print(f"Автоматически зашифрованный: {caesar.encrypted}")


caesar.shift = 10
print(f"Зашифрованный (shift=10): {caesar.encrypted}")

print("\n=== Шифр Атбаш ===")
atbash = AtbashCipher("Хеллоу свага йоу мир!")
print(f"Исходный текст: {atbash.text}")
print(f"Зашифрованный: {atbash.encrypt()}")
print(f"Дешифрованный: {atbash.decrypt(atbash.encrypt())}")

atbash.text = "Хочу покушать роллов"
print(f"\nНовый текст: {atbash.text}")
print(f"Автоматически зашифрованный: {atbash.encrypted}")

print("\n=== Использование менеджера ===")
manager = CipherManager()

caesar_cipher = manager.add_caesar("my_caesar", "Хотеть не вредно", 7)
print(f"Цезарь: {caesar_cipher.text} -> {caesar_cipher.encrypt()}")

atbash_cipher = manager.add_atbash("my_atbash", "Плаке Плаке")
print(f"Атбаш: {atbash_cipher.text} -> {atbash_cipher.encrypt()}")

print("\n=== Прямое использование дескриптора ===")
descriptor = CipherDescriptor('caesar', key=4)
text = "Хочу получить пять по матану"
encrypted = descriptor.encrypt(text)
decrypted = descriptor.decrypt(encrypted)
print(f"Текст: {text}")
print(f"Зашифрованный (Цезарь, key=4): {encrypted}")
print(f"Дешифрованный: {decrypted}")

descriptor2 = CipherDescriptor('atbash')
encrypted2 = descriptor2.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"\nАлфавит в Атбаш: {encrypted2}")
