"""
Este programa es un software gratuito: puede redistribuirlo y / o modificarlo
En los términos de la licencia pública general de GNU Affer, según lo publicado por
la Fundación Software Free, ya sea la versión 3 de la licencia, o
(a su opción) cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil,
Pero sin ninguna garantía;Sin ni siquiera la garantía implícita de
Comercibilidad o aptitud para un propósito particular.Ver el
Licencia pública general de GNU AFFERO para más detalles.

Debería haber recibido una copia de la licencia pública general de GNU AFFERO.
junto con este programa.Si no, consulte
"""

import os
import asyncio
from bot import bot
from config import Config
from pyrogram import idle
from helpers.log import LOGGER
from helpers.utils import start_stream
from assets.user import group_call, USER
from pyrogram.errors import UserAlreadyParticipant


if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
else:
    for f in os.listdir("./downloads"):
        os.remove(f"./downloads/{f}")

async def main():
    await bot.start()
    Config.BOT_USERNAME = (await bot.get_me()).username
    await group_call.start()
    LOGGER.warning(f"{Config.BOT_USERNAME} Comenzó con éxito !")
    if Config.IS_NONSTOP_STREAM:
        await start_stream()
    try:
        await USER.join_chat("AsmSafone")
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        pass
    await idle()
    LOGGER.warning("Video Player Bot se detuvo !")
    await bot.stop()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())



