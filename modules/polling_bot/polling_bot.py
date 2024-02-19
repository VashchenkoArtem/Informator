import aiogram
import modules.bot_create.bot_create as m_bot
import modules.create_dispatcher.create_dispatcher as m_dispatcher
import asyncio

async def main():
    await m_dispatcher.dp.start_polling(m_bot.bot)