# Flappy Plane 🛩️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)

Клон популярной игры Flappy Bird с самолетом вместо птицы, написанный на Python с использованием Pygame.

![Gameplay Screenshot]([URL=https://fastpic.org/view/125/2025/0702/c50014ea282731622a6ae6c15661969d.png.html][IMG]https://i125.fastpic.org/thumb/2025/0702/9d/c50014ea282731622a6ae6c15661969d.jpeg[/IMG][/URL])

## Особенности ✨

-  Классический геймплей Flappy Bird с новым визуальным стилем
-  Управляемый самолет с реалистичной физикой и анимацией
-  Фоновая музыка и звуковые эффекты
-  Система подсчета очков
-  Адаптивный интерфейс под разные разрешения экрана

## Установка ⚙️

1. Убедитесь, что у вас установлен Python 3.8+
2. Установите зависимости:
   ```bash
   pip install pygame
3.Запустите игру:
python main.py
## Управление 🎮

Пробел или ЛКМ - прыжок/взлет
Пробел или ЛКМ - рестарт после проигрыша

Структура проекта 📂

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
