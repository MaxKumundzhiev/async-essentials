
## Что такое Asyncio
- библиотека для написания конкуретных задач
- учитывая опыт Twisted, Tornado, Tulip, greenlet и прочих (переключали контекст неявно)
- привнес синтаксис async/await 
- прослойка между расширениями, работающими на функциях обратног вызова async/await

## Что такое стандарт Asyncio
- фундамент для асинхронных фреймворков
- Базовые абстракции (Future / Coroutine / Task / AbstractEventLoop)
- Высокоуровневый API
- Низкоуровневый API


## Высокоуровневый API
- Слпрограммы (coroutine / generator coroutine), задачи (Task)
- Потоки (streams), примитивы для синхронизации, Queues
- API для работы с процессами и межпроцессного взаисодействия

## Низкоуровневый API
- Loop, Asyncio.Future
- Транспорты и протоколы


## Awaitable objects 
- awaitable objects это обьекты с словом await, означает, что текущая сопрограмма переключит контекс и будет ожидать, пока выражение не будет выполнено  
- три основных типа awaitable objects: coroutine / task / future

```python
class Timer:
    def __init__(self, coroutine):
        self.coroutine = coroutine
        self.spent = 0
    
    def __await__(self):
        started = time.monotonic()
        result = yield from self.coroutine.__await__()
        self.spent = time.monotonic() - started
        return result

async def main():
    t = Timer(asyncio.sleep(1, "foo"))
    res = await t
    print(res)
    print(res.spent)
```

## Что такое обьект coroutine 
- Обьект, который имеет ряд инструкций, умеет зранить свое состояние и может переключать контекст (передавать управление)

## Что такое функция coroutine
- функция, которая возвращает обькт coroutine
- Определяется коючевым словом async def
- Может слдержать клбчевые слова: await, async for, async with

```python
import asyncio

# common version
async def coroutine():  # coroutine function
    print("boom")
    await asyncio.sleep(1)
    print("shakaka")

coro = coroutine()  # coroutine object


# older version
@asyncio.coroutine
async def coroutine():  # coroutine function
    print("boom")
    yield from asyncio.sleep(1)
    print("shakaka")

coro = coroutine()  # coroutine object
```

## Как запустить сопрограмму явно
- asyncio.run() - запускает event loop лжидания окончания работы ассинхронной функции, завершение работы event loop и отмена всех поражденных асинхронных задач
- await - запуск из асинхронного кода с явным пепеключением контекста await

```python
import asyncio

async def get_text():
    print("foobuzz")

async def say_text():
    text = await get_text()
    await asyncio.sleep(1)
    return text

result = asyncio.run(say_text())
print(result)
```

## Как запустить сопрограмму в фоновом режиме
- asyncio.create_task() - запускает задачи в фоновом режиме

```python
async def get_text(delay, text):
    await asyncio.sleep(delay)
    return text

async def say_text():
    task1 = asyncio.create_task(get_text(1, "yep"))
    task2 = asyncio.create_task(get_text(1, "yoho"))
    await task1
    await task2
    return " ".join([task1.result(), task2.result()])

result = asyncio.run(say_text())
print(result)
```

## Что такое Task и зачем он нужен
- Представляет из себя сопрограмму, запущенную или запланированную для запуска в цикле событий
- Позволяет запускать задачи в фоном режиме
- Создается при помощи asyncio.create_task() или loop.create_task()
- Абстракция, позволяющая отменить/прервать выполнение сопрограммы при помощи cancel()

## Посмотрим пример - считаем курс доллара для пользователя
```python
import asyncio
from random import randint

rate = randint(1, 99)

async def handler(reader, writer):
    writer.write(f"Rate is {rate}")
    await writer.drain()
    writer.close()


async def main():
    server = await asyncio.start_server(handler, "127.0.0.1", 8080)
    async with server:
        await server.serve_forever()

asyncio.run(main())
```

## Что такое Future и зачем он нужен
- Специальный низкоуровневый Awaitable обьект, представляющий конечный результат выполнения асинхронной операции
- Позволяет использовать низкоуровневый код, реализованный на колбэках с высокоуровневым кодом на async/await
- Создается при помощи loop.create_future()
... # 17:26 https://www.youtube.com/watch?v=rYQk3PW16bE