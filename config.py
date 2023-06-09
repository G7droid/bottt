# Bot token.
BOT_TOKEN = "6035120091:AAEQrXTWCumF466TrqMiMqMDLgJdSakKtrs"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 11909799
API_HASH = "63240e7d1fc46729a38fc97cb75fb68e"

# CHAT DE ERROS
LOG_CHAT = -1001603734200

# LOGS DE COMPRAS E ADD SALDO-1001603734200
ADMIN_CHAT = -1001791754293

# CHAT DE COMPRAS PARA CLIENTE
CLIENT_CHAT = -1001791754293
# Quantas atualiza��es podem ser tratadas em paralelo.
# N�o use valores altos para servidores low-end.
WORKERS = 20

# Os administradores podem acessar o painel e adicionar novos materiais ao bot.
ADMINS = [5967245836]

# Sudoers t�m acesso total ao servidor e podem executar comandos.
SUDOERS = [1898183014]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []
