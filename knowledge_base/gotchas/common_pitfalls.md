# Частые ошибки при работе с asyncio

## 1. Забытый await
```python
# Неправильно ❌
async def main():
    asyncio.sleep(1)  # Корутина не будет выполнена!

# Правильно ✅
async def main():
    await asyncio.sleep(1)
```

## 2. Блокировка Event Loop
```python
# Неправильно ❌
async def blocking_code():
    time.sleep(1)  # Блокирует весь Event Loop!

# Правильно ✅
async def non_blocking_code():
    await asyncio.sleep(1)
```

## 3. Создание корутин без запуска
```python
# Неправильно ❌
async def main():
    background_task()  # Создаёт корутину, но не запускает её

# Правильно ✅
async def main():
    await background_task()  # или
    task = asyncio.create_task(background_task())
```

## 4. Неправильная обработка исключений
```python
# Неправильно ❌
task = asyncio.create_task(some_coroutine())
# Исключения в task будут потеряны!

# Правильно ✅
task = asyncio.create_task(some_coroutine())
try:
    await task
except Exception as e:
    print(f"Task failed: {e}")
```

## 5. Смешивание синхронного и асинхронного кода
```python
# Неправильно ❌
def sync_function():
    result = await async_operation()  # SyntaxError!

# Правильно ✅
async def async_function():
    result = await async_operation()
```

## Важные заметки
- Всегда проверяйте, что все корутины запущены
- Используйте `asyncio.gather()` для параллельного выполнения
- Не забывайте про обработку исключений
- Избегайте блокирующих операций в асинхронном коде

## Связанные концепции
- [[Event Loop]]
- [[Coroutines]]
- [[Exception Handling]]
