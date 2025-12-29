from abc import ABC, abstractmethod
from typing import Optional, Union


class CipherDescriptor:
    """Дескриптор для управления шифрованием/дешифрованием текста"""

    def __init__(self, cipher_type: str = 'caesar', key: Optional[int] = None):
        self.cipher_type = cipher_type
        self.key = key
        self.storage_name = None

    def __set_name__(self, owner, name):
        self.storage_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name, "")

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")

        setattr(obj, self.storage_name, value)

        if hasattr(obj, 'update_encrypted'):
            obj.update_encrypted()

    def encrypt(self, text: str, **kwargs) -> str:
        """Шифрование текста"""
        if self.cipher_type == 'caesar':
            return self._caesar_cipher(text, **kwargs)
        elif self.cipher_type == 'atbash':
            return self._atbash_cipher(text)
        else:
            raise ValueError(f"Неизвестный тип шифра: {self.cipher_type}")

    def decrypt(self, text: str, **kwargs) -> str:
        """Дешифрование текста"""
        if self.cipher_type == 'caesar':
            return self._caesar_cipher(text, decrypt=True, **kwargs)
        elif self.cipher_type == 'atbash':
            return self._atbash_cipher(text)
        else:
            raise ValueError(f"Неизвестный тип шифра: {self.cipher_type}")

    def _caesar_cipher(self, text: str, key: Optional[int] = None,
                       decrypt: bool = False) -> str:
        """Реализация шифра Цезаря для кириллицы"""
        if key is None:
            key = self.key if self.key is not None else 3

        if decrypt:
            key = -key

        result = []
        for char in text:
            if 'А' <= char <= 'Я':
                shift = ord('А')
                result.append(chr((ord(char) - shift + key) % 32 + shift))
            elif 'а' <= char <= 'я':
                shift = ord('а')
                result.append(chr((ord(char) - shift + key) % 32 + shift))
            elif char == 'Ё':
                base = ord('Е') + 1 if key >= 0 else ord('Е')
                pos = (1 + key) % 33
                result.append('Ё' if pos == 1 else chr(ord('А') + pos - 1))
            elif char == 'ё':
                base = ord('е') + 1 if key >= 0 else ord('е')
                pos = (1 + key) % 33
                result.append('ё' if pos == 1 else chr(ord('а') + pos - 1))
            else:
                result.append(char)
        return ''.join(result)

    def _atbash_cipher(self, text: str) -> str:
        """Реализация шифра Атбаш для кириллицы"""
        result = []
        for char in text:
            if 'А' <= char <= 'Я':
                result.append(chr(ord('А') + ord('Я') - ord(char)))
            elif 'а' <= char <= 'я':
                result.append(chr(ord('а') + ord('я') - ord(char)))
            elif char == 'Ё':
                result.append('Э')
            elif char == 'ё':
                result.append('э')
            elif char == 'Э':
                result.append('Ё')
            elif char == 'э':
                result.append('ё')
            else:
                result.append(char)
        return ''.join(result)


class BaseCipher(ABC):
    """Абстрактный базовый класс для шифрования"""

    def __init__(self, text: str = ""):
        self._original_text = text
        self._encrypted_text = ""

    @abstractmethod
    def encrypt(self) -> str:
        pass

    @abstractmethod
    def decrypt(self) -> str:
        pass

    def update_encrypted(self):
        """Обновить зашифрованное представление"""
        self._encrypted_text = self.encrypt()


class CaesarCipher(BaseCipher):
    """Класс для шифра Цезаря"""

    text = CipherDescriptor('caesar', key=3)

    encrypted = CipherDescriptor('caesar', key=3)

    def __init__(self, text: str = "", shift: int = 3):
        self._shift = shift
        super().__init__(text)
        self.text = text

    @property
    def shift(self) -> int:
        return self._shift

    @shift.setter
    def shift(self, value: int):
        self._shift = value
        self.update_encrypted()

    def encrypt(self, text: Optional[str] = None) -> str:
        """Шифрование текста шифром Цезаря"""
        if text is None:
            text = self._original_text
        return CipherDescriptor('caesar', key=self._shift).encrypt(text)

    def decrypt(self, text: Optional[str] = None) -> str:
        """Дешифрование текста шифром Цезаря"""
        if text is None:
            text = self._encrypted_text
        return CipherDescriptor('caesar', key=self._shift).decrypt(text)

    def update_encrypted(self):
        """Обновить зашифрованное представление"""
        self._encrypted_text = self.encrypt(self._original_text)


class AtbashCipher(BaseCipher):
    """Класс для шифра Атбаш"""

    text = CipherDescriptor('atbash')

    encrypted = CipherDescriptor('atbash')

    def __init__(self, text: str = ""):
        super().__init__(text)
        self.text = text

    def encrypt(self, text: Optional[str] = None) -> str:
        """Шифрование текста шифром Атбаш"""
        if text is None:
            text = self._original_text
        return CipherDescriptor('atbash').encrypt(text)

    def decrypt(self, text: Optional[str] = None) -> str:
        """Дешифрование текста шифром Атбаш (симметрично шифрованию)"""
        if text is None:
            text = self._encrypted_text
        return CipherDescriptor('atbash').decrypt(text)

    def update_encrypted(self):
        """Обновить зашифрованное представление"""
        self._encrypted_text = self.encrypt(self._original_text)


class CipherManager:
    """Менеджер для работы с различными шифрами"""

    def __init__(self):
        self.ciphers = {}

    def add_caesar(self, name: str, text: str = "", shift: int = 3) -> CaesarCipher:
        """Добавить шифр Цезаря"""
        cipher = CaesarCipher(text, shift)
        self.ciphers[name] = cipher
        return cipher

    def add_atbash(self, name: str, text: str = "") -> AtbashCipher:
        """Добавить шифр Атбаш"""
        cipher = AtbashCipher(text)
        self.ciphers[name] = cipher
        return cipher

    def get_cipher(self, name: str) -> Union[CaesarCipher, AtbashCipher, None]:
        """Получить шифр по имени"""
        return self.ciphers.get(name)