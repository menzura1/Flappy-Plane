# Flappy Plane 🛩️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)

Клон популярной игры Flappy Bird с самолетом вместо птицы, написанный на Python с использованием Pygame.

![Screenshot](https://github.com/menzura1/Flappy-Plane/blob/main/Screenshot_1.jpg)

## Особенности ✨

 -  Классический геймплей Flappy Bird с новым визуальным стилем
 -  Управляемый самолет с реалистичной физикой и анимацией
 -  Фоновая музыка и звуковые эффекты
 -  Система подсчета очков
 -  Адаптивный интерфейс под разные разрешения экрана

## Установка ⚙️

 1. Убедитесь, что у вас установлен Python 3.8+
 2. Установите модули:
  pip install pygame

 3.Запустите игру:
 python main.py
## Управление 🎮

Пробел(SPACE) или ЛКМ - прыжок/взлет
Пробел(SPACE) или ЛКМ - рестарт после проигрыша

## Структура проекта 📂

flappy-plane/
graphics/          # Графические ресурсы
├── environment/   # Фон и земля
├── obstacles/     # Препятствия
├── plane/         # Спрайты самолета
└── ui/            # Интерфейс
sounds/            # Звуковые эффекты
├── game song and jump song
code/
├── main.py            # Основной игровой цикл
├── settings.py        # Конфигурация игры
└── sprites.py         # Классы спрайтов
