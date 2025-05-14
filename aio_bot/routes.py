from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from datetime import datetime
from aiogram.filters import Command
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback
import pytz
import aiohttp

router = Router()

# Часовой пояс по ТЗ
ADAK_TZ = pytz.timezone("America/Adak")


class TaskState(StatesGroup):
    message = State()
    tag = State()
    select_date = State()
    select_hour = State()
    select_minute = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(TaskState.message)
    await message.answer("Привет! Укажи <b>текст</b> задачи.")


# обработка текста и вызов тэга
@router.message(TaskState.message)
async def get_message(message: Message, state: FSMContext):
    await state.update_data(message_text=message.text)
    await state.set_state(TaskState.tag)
    await message.answer("Теперь укажите тег (или напишите '-' если не нужен):")


# обработка тэга и вызов календаря
@router.message(TaskState.tag)
async def get_tag(message: Message, state: FSMContext):
    tag = None if message.text.strip() == "-" else message.text.strip()
    await state.update_data(tag=tag)
    await state.set_state(TaskState.select_date)
    await message.answer("Выберите дату напоминания:",
                         reply_markup=await SimpleCalendar(locale="ru_RU.utf8").start_calendar())


# обработка выбранной даты из стадии календаря и вызов времени
@router.callback_query(SimpleCalendarCallback.filter())
async def process_date(callback_query: CallbackQuery, callback_data: CallbackData, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await state.update_data(date=date)
        await callback_query.message.edit_text("Выберите час напоминания:", reply_markup=hour_keyboard())
        await state.set_state(TaskState.select_hour)


# рисуем кнопки для выбора часов
def hour_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=str(h), callback_data=f"hour_{h}") for h in range(i, i + 6)]
        for i in range(0, 24, 6)
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# обработка часов
@router.callback_query(F.data.startswith("hour_"))
async def process_hour(callback: CallbackQuery, state: FSMContext):
    hour = int(callback.data.split("_")[1])
    await state.update_data(hour=hour)
    await callback.message.answer("Теперь выберите минуту напоминания:", reply_markup=minute_keyboard())
    await state.set_state(TaskState.select_minute)


# рисуем минуты
def minute_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=str(m), callback_data=f"minute_{m}") for m in range(i, i + 5)] for i in
        range(0, 60, 5)
    ])


# обработка минут
@router.callback_query(F.data.startswith("minute_"))
async def process_minute(callback: CallbackQuery, state: FSMContext):
    minute = int(callback.data.split("_")[1])
    data = await state.get_data()

    combined = datetime(
        year=data["date"].year,
        month=data["date"].month,
        day=data["date"].day,
        hour=data["hour"],
        minute=minute
    )
    notice_time = ADAK_TZ.localize(combined)
    await state.update_data(notice_time=notice_time)

    await callback.message.answer(f"Дата и время установлены: {notice_time.isoformat()}")

    payload = {
        "user_id": callback.from_user.id,
        "message": data["message_text"],
        "tag": data.get("tag", "без тэга"),
        "notice_time_date": notice_time.isoformat()
    }
    try:
        response_data = await create_task(payload)
        await callback.message.answer(f"Задача сохранена: {response_data}")

    except Exception as e:
        print(e)
        await callback.message.answer(f"произошла ошибка")

    await state.clear()


# запись собранных данных через дрф ручку в постгрес
async def create_task(data: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/api/tasks/create/", json=data) as response:
            result = await response.json()
            return result
