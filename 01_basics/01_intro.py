"""
Базовый пример использования asyncio.
Демонстрирует:
1. Создание корутины
2. Работу с event loop
3. Разницу между синхронным и асинхронным выполнением
"""

import asyncio
import time


async def async_sleep(seconds: int, name: str) -> None:
    """Асинхронная функция, которая симулирует некоторую работу."""
    print(f"[{name}] Начинаю работу...")
    await asyncio.sleep(seconds)
    print(f"[{name}] Завершаю работу после {seconds} секунд")


def sync_sleep(seconds: int, name: str) -> None:
    """Синхронная функция для сравнения."""
    print(f"[{name}] Начинаю работу...")
    time.sleep(seconds)
    print(f"[{name}] Завершаю работу после {seconds} секунд")


async def main():
    # Пример 1: Последовательное выполнение корутин
    print("\n=== Последовательное выполнение ===")
    start_time = time.time()
    
    await async_sleep(2, "Задача 1")
    await async_sleep(1, "Задача 2")
    
    print(f"Общее время выполнения: {time.time() - start_time:.2f} секунд")

    # Пример 2: Параллельное выполнение корутин
    print("\n=== Параллельное выполнение ===")
    start_time = time.time()
    
    # gather позволяет запускать корутины параллельно
    await asyncio.gather(
        async_sleep(2, "Задача 1"),
        async_sleep(1, "Задача 2")
    )
    
    print(f"Общее время выполнения: {time.time() - start_time:.2f} секунд")

    # Пример 3: Создание задач
    print("\n=== Создание задач ===")
    start_time = time.time()
    
    task1 = asyncio.create_task(async_sleep(2, "Задача 1"))
    task2 = asyncio.create_task(async_sleep(1, "Задача 2"))
    
    # Ждем завершения всех задач
    await task1
    await task2
    
    print(f"Общее время выполнения: {time.time() - start_time:.2f} секунд")


if __name__ == "__main__":
    # Запуск асинхронной программы
    asyncio.run(main())
