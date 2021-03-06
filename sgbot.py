# -*- coding: utf8 -*-

import asyncio
import logging

import openpyxl as xl
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnHlp = KeyboardButton('Help')
btnDon = KeyboardButton('Donate')

help_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(btnHlp, btnDon)

with open('token.txt') as tok:
    t_token = tok.read().strip()

bot = Bot(token=t_token)  # Токен тестового бота testingspamobot

dp: Dispatcher = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

greet_me = ['Хозяин', 'Повелитель', 'Иван Александрович', 'Мой создатель', 'Мой Руководитель']
boss_id = 799592984
gilmanov = 115061573
rumyancev = 981548325
shuev = 518362675

accepted_user = [799592984, 115061573, 981548325, 518362675, 403210867, 715905190]

wb = xl.load_workbook('table_summary_phase2.xlsx')
sheet_1 = wb['sheet1']
sheet_2 = wb['sheet2']
sheet_3 = wb['sheet3']
sheet_4 = wb['sheet4']
sheet_id = wb['sheet_id']

for i in sheet_id['A1':'B1']:
    id_prin = int(str(i[0].value))
    id_prov = int(str(i[1].value))

# общий метраж и кол-во ТП по установкам
for i in sheet_1['A1':'H1']:
    tp_30 = int(i[0].value)
    vol_30 = float(i[1].value)
    tp_110 = int(i[2].value)
    vol_110 = float(i[3].value)
    tp_60 = int(i[4].value)
    vol_60 = float(i[5].value)
    tp_70 = int(i[6].value)
    vol_70 = float(i[7].value)
# ------------------------------------------------

# Принятые работы по АИС журнал заявок
# 0-конструктив, 1-дув до, 2-испыт, 3-дув после, 5-констрТП,
# 4-обратка, 6-дувдоТП, 7-испытТП, 8дувпослТП,9- обраткаТП, 10-остаток метр, 11-остаток ТПконстр
constr_30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
constr_110 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
constr_60 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
constr_70 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in sheet_2['A1':'M4']:
    if str(i[12].value) == '30':
        constr_30[0] += float(str(i[0].value))
        constr_30[1] += float(str(i[1].value))
        constr_30[2] += float(str(i[2].value))
        constr_30[3] += float(str(i[3].value))
        constr_30[4] += float(str(i[4].value))
        constr_30[5] += int(str(i[5].value))
        constr_30[6] += int(str(i[6].value))
        constr_30[7] += int(str(i[7].value))
        constr_30[8] += int(str(i[8].value))
        constr_30[9] += int(str(i[9].value))
        constr_30[10] += float(str(i[10].value))
        constr_30[11] += int(str(i[11].value))
    if str(i[12].value) == '110':
        constr_110[0] += float(str(i[0].value))
        constr_110[1] += float(str(i[1].value))
        constr_110[2] += float(str(i[2].value))
        constr_110[3] += float(str(i[3].value))
        constr_110[4] += float(str(i[4].value))
        constr_110[5] += int(str(i[5].value))
        constr_110[6] += int(str(i[6].value))
        constr_110[7] += int(str(i[7].value))
        constr_110[8] += int(str(i[8].value))
        constr_110[9] += int(str(i[9].value))
        constr_110[10] += float(str(i[10].value))
        constr_110[11] += int(str(i[11].value))
    if str(i[12].value) == '60':
        constr_60[0] += float(str(i[0].value))
        constr_60[1] += float(str(i[1].value))
        constr_60[2] += float(str(i[2].value))
        constr_60[3] += float(str(i[3].value))
        constr_60[4] += float(str(i[4].value))
        constr_60[5] += int(str(i[5].value))
        constr_60[6] += int(str(i[6].value))
        constr_60[7] += int(str(i[7].value))
        constr_60[8] += int(str(i[8].value))
        constr_60[9] += int(str(i[9].value))
        constr_60[10] += float(str(i[10].value))
        constr_60[11] += int(str(i[11].value))
    if str(i[12].value) == '70':
        constr_70[0] += float(str(i[0].value))
        constr_70[1] += float(str(i[1].value))
        constr_70[2] += float(str(i[2].value))
        constr_70[3] += float(str(i[3].value))
        constr_70[4] += float(str(i[4].value))
        constr_70[5] += int(str(i[5].value))
        constr_70[6] += int(str(i[6].value))
        constr_70[7] += int(str(i[7].value))
        constr_70[8] += int(str(i[8].value))
        constr_70[9] += int(str(i[9].value))
        constr_70[10] += float(str(i[10].value))
        constr_70[11] += int(str(i[11].value))
# -----------------------------------------------

# сводка по стыкам
# 0-всего сварено, 1-контроль ПО, 2-годен ПО, 3-ремонтПО, 4-контрольСГ, 5-годенСГ, 6-РемонтСГ
joints_30 = [0, 0, 0, 0, 0, 0, 0]
joints_110 = [0, 0, 0, 0, 0, 0, 0]
joints_60 = [0, 0, 0, 0, 0, 0, 0]
joints_70 = [0, 0, 0, 0, 0, 0, 0]
for i in sheet_3['A1':'H4']:
    if str(i[7].value) == '30':
        joints_30[0] += int(str(i[0].value))
        joints_30[1] += int(str(i[1].value))
        joints_30[2] += int(str(i[2].value))
        joints_30[3] += int(str(i[3].value))
        joints_30[4] += int(str(i[4].value))
        joints_30[5] += int(str(i[5].value))
        joints_30[6] += int(str(i[6].value))
    if str(i[7].value) == '110':
        joints_110[0] += int(str(i[0].value))
        joints_110[1] += int(str(i[1].value))
        joints_110[2] += int(str(i[2].value))
        joints_110[3] += int(str(i[3].value))
        joints_110[4] += int(str(i[4].value))
        joints_110[5] += int(str(i[5].value))
        joints_110[6] += int(str(i[6].value))
    if str(i[7].value) == '60':
        joints_60[0] += int(str(i[0].value))
        joints_60[1] += int(str(i[1].value))
        joints_60[2] += int(str(i[2].value))
        joints_60[3] += int(str(i[3].value))
        joints_60[4] += int(str(i[4].value))
        joints_60[5] += int(str(i[5].value))
        joints_60[6] += int(str(i[6].value))
    if str(i[7].value) == '70':
        joints_70[0] += int(str(i[0].value))
        joints_70[1] += int(str(i[1].value))
        joints_70[2] += int(str(i[2].value))
        joints_70[3] += int(str(i[3].value))
        joints_70[4] += int(str(i[4].value))
        joints_70[5] += int(str(i[5].value))
        joints_70[6] += int(str(i[6].value))
# --------------------------------------------------
# выборка текста тестпакетов
install_tp = ['', '', '', '']
blowB_tp = ['', '', '', '']
test_tp = ['', '', '', '']
blowA_tp = ['', '', '', '']
reinst_tp = ['', '', '', '']
for i in sheet_4['A1':'F4']:
    if str(i[5].value) == '30':
        install_tp[0] += str(i[0].value)
        blowB_tp[0] += str(i[1].value)
        test_tp[0] += str(i[2].value)
        blowA_tp[0] += str(i[3].value)
        reinst_tp[0] += str(i[4].value)
    if str(i[5].value) == '110':
        install_tp[1] += str(i[0].value)
        blowB_tp[1] += str(i[1].value)
        test_tp[1] += str(i[2].value)
        blowA_tp[1] += str(i[3].value)
        reinst_tp[1] += str(i[4].value)
    if str(i[5].value) == '60':
        install_tp[2] += str(i[0].value)
        blowB_tp[2] += str(i[1].value)
        test_tp[2] += str(i[2].value)
        blowA_tp[2] += str(i[3].value)
        reinst_tp[2] += str(i[4].value)
    if str(i[5].value) == '70':
        install_tp[3] += str(i[0].value)
        blowB_tp[3] += str(i[1].value)
        test_tp[3] += str(i[2].value)
        blowA_tp[3] += str(i[3].value)
        reinst_tp[3] += str(i[4].value)
# -------------------------------------------------------

# 0-конструктив метр, 1- остаток 2-дувДО, 3- испы, 4-дув после, 5- обратка 6-ТПприятно констр, 7-остаток ТП
all_phase2 = [(constr_30[0] + constr_60[0] + constr_70[0] + constr_110[0]),
              (constr_30[10] + constr_60[10] + constr_70[10] + constr_110[10]),
              (constr_30[1] + constr_60[1] + constr_70[1] + constr_110[1]),
              (constr_30[2] + constr_60[2] + constr_70[2] + constr_110[2]),
              (constr_30[3] + constr_60[3] + constr_70[3] + constr_110[3]),
              (constr_30[4] + constr_60[4] + constr_70[4] + constr_110[4]),
              (constr_30[5] + constr_60[5] + constr_70[5] + constr_110[5]),
              (constr_30[11] + constr_60[11] + constr_70[11] + constr_110[11])]
# -----------------------------------------------------------------------------------------------------------------------
# ut_sheet---------------------
ut_control = [0, 0, 0, 0]
ut_accept = [0, 0, 0, 0]
ut_repair = [0, 0, 0, 0]
sheet_ut = wb['sheet_ut_sg']
for i in sheet_ut['A1':'D4']:
    if '30' in str(i[3].value):
        ut_control[0] += int(str(i[0].value))
        ut_accept[0] += int(str(i[1].value))
        ut_repair[0] += int(str(i[2].value))
    if '110' in str(i[3].value):
        ut_control[1] += int(str(i[0].value))
        ut_accept[1] += int(str(i[1].value))
        ut_repair[1] += int(str(i[2].value))
    if '60' in str(i[3].value):
        ut_control[2] += int(str(i[0].value))
        ut_accept[2] += int(str(i[1].value))
        ut_repair[2] += int(str(i[2].value))
    if '70' in str(i[3].value):
        ut_control[3] += int(str(i[0].value))
        ut_accept[3] += int(str(i[1].value))
        ut_repair[3] += int(str(i[2].value))


@dp.message_handler(commands='start')
async def start_using(message: types.Message):
    if message.from_user.id == 799592984:
        await message.answer('Привет. Работает', reply_markup=help_kb)

    else:
        await message.answer('Привет! Чтобы что-то узнать, нажми Help', reply_markup=help_kb)
        await bot.send_message(799592984, f'Кто-то нажал старт user_id - {message.from_user.id}, '
                                          f'user name - {message.from_user.username}')


date_of_change = '12.09.2021'


@dp.message_handler()
async def help_msg(message: types.Message):
    if message.from_user.id in accepted_user:
        if message.text == 'Help':
            writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
            Btn_Phase2 = InlineKeyboardButton('Сводка по Фазе 2', callback_data='/phase2')
            Btn_30 = InlineKeyboardButton('Сводка по 3-30', callback_data='/3_30')
            Btn_110 = InlineKeyboardButton('Сводка по 3-110', callback_data='/3_110')
            Btn_70 = InlineKeyboardButton('Сводка по 2-70', callback_data='/2_70')
            Btn_60 = InlineKeyboardButton('Сводка по 2-60', callback_data='/2_60')
            write_kb = InlineKeyboardMarkup().add(Btn_Phase2).add(Btn_30).add(Btn_110).add(Btn_70).add(Btn_60).add(
                writeBtn)
            await message.answer('Выбери, что тебе нужно:', reply_markup=write_kb)
            await message.answer(
                f'Alpha_test_1. ver. 0.35 date \n Любая информация является справочной, '
                f'разработчик не несет ответственности за достоверность.',
                reply_markup=help_kb)
        if message.text == 'Donate':
            await message.answer('В тестовом режиме функция не работает. Жми HELP.')
            await message.answer(f'ver. 0.36 date 23.10.21 ', reply_markup=help_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await message.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


# приём файлов обновлений---------------
@dp.message_handler(content_types=['document'])
async def handle_docs_42(message: types.document):
    if message.from_user.id == 799592984:
        if message.document.file_name == 'table_summary_phase2.xlsx':
            try:
                file_info = await bot.get_file(message.document.file_id)
                downloaded_file = await bot.download_file(file_info.file_path)
                print(message.document.file_name)
                print(downloaded_file)
                with open('table_summary_phase2.xlsx', 'wb') as new_file:
                    new_file.write(downloaded_file.getvalue())
                await message.answer('Сохранил')
            except Exception as e:
                await message.answer(e)
        elif message.document.file_name == 'summary_phase2.xlsx':
            try:
                file_info = await bot.get_file(message.document.file_id)
                downloaded_file = await bot.download_file(file_info.file_path)
                print(message.document.file_name)
                print(downloaded_file)
                with open('summary_phase2.xlsx', 'wb') as new_file:
                    new_file.write(downloaded_file.getvalue())
                await message.answer('Сохранил')
            except Exception as e:
                await message.answer(e)


# ----------------------------------------------

@dp.callback_query_handler(lambda c: c.data == '/phase2')
async def process_callback_horo(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in accepted_user:
        if callback_query.from_user.id != 799592984:
            await bot.send_message(799592984, f'Кто-то нажал сводку user_id - {callback_query.from_user.id}, '
                                              f'user name - {callback_query.from_user.username}')
        Btn_summary = InlineKeyboardButton('Скачать сводную таблицу по ТП', callback_data='/sum_phase_2')
        summary_kb = InlineKeyboardMarkup().add(Btn_summary)
        await bot.send_message(callback_query.from_user.id, f'Сводка по ФАЗЕ 2:\n'
                                                            f'Конструктив принято  -  {round(all_phase2[0], 3)} м., остаток {round(all_phase2[1])} m.,  \n'
                                                            f'ТП на коструктив принято - {all_phase2[6]}шт., остаток ТП {all_phase2[7]}шт.\n\n'
                                                            f'Продувка перед испытаниями принято - {all_phase2[2]} m.\n'
                                                            f'ТП продувка перед испытаниями принято - {round((constr_30[6] + constr_60[6] + constr_70[6] + constr_110[6]), 3)}шт.\n\n'
                                                            f'Испытания на прочность и плотность принято - {round(all_phase2[3], 3)} m.\n'
                                                            f'ТП испытания на прочность и плотность принято - {(constr_30[7] + constr_60[7] + constr_70[7] + constr_110[7])}шт.\n\n'
                                                            f'Продувка после испытаний - {all_phase2[4]} m.\n'
                                                            f'ТП продувка после испытаний принято - {(constr_30[8] + constr_60[8] + constr_70[8] + constr_110[8])}шт.\n\n'
                                                            f'Обратная сборка принято - {round(all_phase2[5], 3)} m.\n'
                                                            f'ТП по обратной сборке принято - {(constr_30[9] + constr_60[9] + constr_70[9] + constr_110[9])}шт.\n\n'
                                                            f'Стыков сварено по ФАЗЕ 2: - {int((joints_30[0] + joints_110[0] + joints_60[0] + joints_70[0]))}ст.\n\n'
                                                            f'Принято на проверку ИД ТП - {id_prin} шт.\n'
                                                            f'Проверено ИД ТП - {id_prov} шт.\n',
                               reply_markup=summary_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/sum_phase_2')
async def process_callback_horo(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != 799592984:
        await bot.send_message(799592984, f'Кто-то качает сводную таблицу user_id - {callback_query.from_user.id}, '
                                          f'user name - {callback_query.from_user.username}')
    if callback_query.from_user.id in accepted_user:
        await bot.send_document(callback_query.from_user.id, open(r'summary_phase2.xlsx', 'rb'))


@dp.callback_query_handler(lambda c: c.data == '/3_30')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != 799592984:
        await bot.send_message(799592984, f'Кто-то нажал 30 user_id - {callback_query.from_user.id}, '
                                          f'user name - {callback_query.from_user.username}')
    Btn_TP = InlineKeyboardButton('Принятые тест-пакеты по 3-30', callback_data='/3_30_tp')
    tp_kb = InlineKeyboardMarkup().add(Btn_TP)
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'Установка 3-30:\n'
                                                            f'Конструктив принято - {constr_30[0]} m., остаток - {constr_30[10]}m. \n'
                                                            f'ТП на конструктив принято - {constr_30[5]}шт., остаток {constr_30[11]}шт.\n\n'
                                                            f'Продувка перед испытаниями принято - {constr_30[1]} m.\n'
                                                            f'ТП продувка перед испытаниями принято - {constr_30[6]} шт.\n\n'
                                                            f'Проведение испытаний на прочность и плотность принято - {constr_30[2]} m. \n'
                                                            f'ТП испытания на прочность и плотность принято {constr_30[7]}шт.\n\n'
                                                            f'Продувка после испытаний - {constr_30[3]} m. \n'
                                                            f'ТП продувка после испытаний принято - {constr_30[8]} шт.\n\n'
                                                            f'Обратная сборка принято - {constr_30[4]}м.\n'
                                                            f'ТП обратная сборка принято - {constr_30[9]}шт.\n\n'
                                                            f'Сварено всего - {joints_30[0]}ст.\n'
                                                            f'проконтролировано ПО - {joints_30[1]}ст.  '
                                                            f'проконтролировано СГ - {joints_30[4]}ст.\n'
                                                            f'годен по результатам ПО - {joints_30[2]}ст.,\n  годен по результатам СГ - {joints_30[5]}ст.\n'
                                                            f'не годен по результатам ПО - {joints_30[3]}ст.,\n не годен по результатам СГ - {joints_30[6]}ст.\n\n'
                                                            f'Контроль УЗК СГ - {ut_control[0]} шт.\n'
                                                            f'Годен УЗК СГ - {ut_accept[0]} шт., Не годен - {ut_repair[0]} шт.\n\n',
                               reply_markup=tp_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/3_30_tp')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'ТП Конструктив принято - {install_tp[0]} \n'
                                                            f'ТП Продувка перед испытаниями принято - {blowB_tp[0]}\n'
                                                            f'ТП испытания на прочность и плотность принято - {test_tp[0]}\n'
                                                            f'ТП продувка после испытаний принято - {blowA_tp[0]}\n'
                                                            f'ТП обратная сборка принято - {reinst_tp[0]}\n')
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/3_110')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != 799592984:
        await bot.send_message(799592984, f'Кто-то нажал 110 user_id - {callback_query.from_user.id}, '
                                          f'user name - {callback_query.from_user.username}')
    if callback_query.from_user.id == rumyancev:
        await bot.send_message(rumyancev,
                               'Василий Михайлович, по своей установке могли бы и сами быть в курсе всех принятых работ! ;-)')
        await asyncio.sleep(8)
    Btn_TP = InlineKeyboardButton('Принятые тест-пакеты по 3-110', callback_data='/3_110_tp')
    tp_kb = InlineKeyboardMarkup().add(Btn_TP)
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'Установка 3-110:\n'
                                                            f'Конструктив принято - {constr_110[0]} m., остаток - {constr_110[10]}m. \n'
                                                            f'ТП на конструктив принято - {constr_110[5]}шт., остаток {constr_110[11]}шт.\n\n'
                                                            f'Продувка перед испытаниями принято - {constr_110[1]} m.\n'
                                                            f'ТП продувка перед испытаниями принято - {constr_110[6]} шт.\n\n'
                                                            f'Проведение испытаний на прочность и плотность принято - {constr_110[2]} m. \n'
                                                            f'ТП испытания на прочность и плотность принято {constr_110[7]}шт.\n\n'
                                                            f'Продувка после испытаний - {constr_110[3]} m. \n'
                                                            f'ТП продувка после испытаний принято - {constr_110[8]} шт.\n\n'
                                                            f'Обратная сборка принято - {constr_110[4]}м.\n'
                                                            f'ТП обратная сборка принято - {constr_110[9]}шт.\n\n'
                                                            f'Сварено всего - {joints_110[0]}ст.\n'
                                                            f'проконтролировано ПО - {joints_110[1]}ст.  '
                                                            f'проконтролировано СГ - {joints_110[4]}ст.\n'
                                                            f'годен по результатам ПО - {joints_110[2]}ст., \n годен по результатам СГ - {joints_110[5]}ст.\n'
                                                            f'не годен по результатам ПО - {joints_110[3]}ст.,\n не годен по результатам СГ - {joints_110[6]}ст.\n\n'
                                                            f'Контроль УЗК СГ - {ut_control[1]} шт.\n'
                                                            f'Годен УЗК СГ - {ut_accept[1]} шт., Не годен - {ut_repair[1]} шт.\n\n',
                               reply_markup=tp_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/3_110_tp')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'ТП Конструктив принято - {install_tp[1]} \n'
                                                            f'ТП Продувка перед испытаниями принято - {blowB_tp[1]}\n'
                                                            f'ТП испытания на прочность и плотность принято - {test_tp[1]}\n'
                                                            f'ТП продувка после испытаний принято - {blowA_tp[1]}\n'
                                                            f'ТП обратная сборка принято - {reinst_tp[1]}\n')
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/2_70')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != 799592984:
        await bot.send_message(799592984, f'Кто-то нажал 70 user_id - {callback_query.from_user.id}, '
                                          f'user name - {callback_query.from_user.username}')
    Btn_TP = InlineKeyboardButton('Принятые тест-пакеты по 2-70', callback_data='/2_70_tp')
    tp_kb = InlineKeyboardMarkup().add(Btn_TP)
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'Установка 2-70:\n'
                                                            f'Конструктив принято - {constr_70[0]} m., остаток - {constr_70[10]}m. \n'
                                                            f'ТП на конструктив принято - {constr_70[5]}шт., остаток {constr_70[11]}шт.\n\n'
                                                            f'Продувка перед испытаниями принято - {constr_70[1]} m.\n'
                                                            f'ТП продувка перед испытаниями принято - {constr_70[6]} шт.\n\n'
                                                            f'Проведение испытаний на прочность и плотность принято - {constr_70[2]} m. \n'
                                                            f'ТП испытания на прочность и плотность принято {constr_70[7]}шт.\n\n'
                                                            f'Продувка после испытаний - {constr_70[3]} m. \n'
                                                            f'ТП продувка после испытаний принято - {constr_70[8]} шт.\n\n'
                                                            f'Обратная сборка принято - {constr_70[4]}м.\n'
                                                            f'ТП обратная сборка принято - {constr_70[9]}шт.\n\n'
                                                            f'Сварено всего - {joints_70[0]}ст.\n'
                                                            f'проконтролировано СГ - {joints_70[4]}ст.\n'
                                                            f'годен по результатам ПО - {joints_70[2]}ст.,\n  годен по результатам СГ - {joints_70[5]}ст.\n'
                                                            f'не годен по результатам ПО - {joints_70[3]}ст., \nне годен по результатам СГ - {joints_70[6]}ст.\n\n'
                                                            f'Контроль УЗК СГ - {ut_control[3]} шт.\n'
                                                            f'Годен УЗК СГ - {ut_accept[3]} шт., Не годен - {ut_repair[3]} шт.\n\n',
                               reply_markup=tp_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/2_70_tp')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'ТП Конструктив принято - {install_tp[3]} \n'
                                                            f'ТП Продувка перед испытаниями принято - {blowB_tp[3]}\n'
                                                            f'ТП испытания на прочность и плотность принято - {test_tp[3]}\n'
                                                            f'ТП продувка после испытаний принято - {blowA_tp[3]}\n'
                                                            f'ТП обратная сборка принято - {reinst_tp[3]}\n')
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/2_60')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id != 799592984:
        await bot.send_message(799592984, f'Кто-то нажал 60 user_id - {callback_query.from_user.id}, '
                                          f'user name - {callback_query.from_user.username}')
    Btn_TP = InlineKeyboardButton('Принятые тест-пакеты по 2-60', callback_data='/2_60_tp')
    tp_kb = InlineKeyboardMarkup().add(Btn_TP)
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'Установка 2-60:\n'
                                                            f'Конструктив принято - {constr_60[0]} m., остаток - {constr_60[10]}m. \n'
                                                            f'ТП на конструктив принято - {constr_60[5]}шт., остаток {constr_60[11]}шт.\n\n'
                                                            f'Продувка перед испытаниями принято - {constr_60[1]} m.\n'
                                                            f'ТП продувка перед испытаниями принято - {constr_60[6]} шт.\n\n'
                                                            f'Проведение испытаний на прочность и плотность принято - {constr_60[2]} m. \n'
                                                            f'ТП испытания на прочность и плотность принято {constr_60[7]}шт.\n\n'
                                                            f'Продувка после испытаний - {constr_60[3]} m. \n'
                                                            f'ТП продувка после испытаний принято - {constr_60[8]} шт.\n'
                                                            f'Обратная сборка принято - {constr_60[4]}м.\n'
                                                            f'ТП обратная сборка принято - {constr_60[9]}шт.\n\n'
                                                            f'Сварено всего - {joints_60[0]}ст.\n'
                                                            f'проконтролировано ПО - {joints_60[1]}ст.  '
                                                            f'проконтролировано СГ - {joints_60[4]}ст.\n'
                                                            f'годен по результатам ПО - {joints_60[2]}ст., \n годен по результатам СГ - {joints_60[5]}ст.\n'
                                                            f'не годен по результатам ПО - {joints_60[3]}ст.,\n не годен по результатам СГ - {joints_60[6]}ст.\n\n'
                                                            f'Контроль УЗК СГ - {ut_control[2]} шт.\n'
                                                            f'Годен УЗК СГ - {ut_accept[2]} шт., Не годен - {ut_repair[2]} шт.\n\n',
                               reply_markup=tp_kb)
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


@dp.callback_query_handler(lambda c: c.data == '/2_60_tp')
async def callback_weather(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in accepted_user:
        await bot.send_message(callback_query.from_user.id, f'ТП Конструктив принято - {install_tp[2]} \n'
                                                            f'ТП Продувка перед испытаниями принято - {blowB_tp[2]}\n'
                                                            f'ТП испытания на прочность и плотность принято - {test_tp[2]}\n'
                                                            f'ТП продувка после испытаний принято - {blowA_tp[2]}\n'
                                                            f'ТП обратная сборка принято - {reinst_tp[2]}\n')
    else:
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')
        acc_kb = InlineKeyboardMarkup().add(writeBtn)
        await callback_query.answer('Для предоставления доступа обратитесь к разработчику', reply_markup=acc_kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
