# configurando um crontab

	::: parametros de tempo

		- minute(0-59) hour(0-23) day(1-31) month(1-12) weekday(0-6) command

	::: Digamos que queremos executar o comando /usr/bin/example às 12h30 todos os dias.

		29 0 * * * /usr/bin/example

		- Use valores separados por vírgula para especificar várias vezes. Por exemplo, a linha.

		0,14,29,44 * * * * /usr/bin/example2

		- Use valores separados por traço para especificar um intervalo de valores. Por exemplo, a linha.

		0 11 * 1-6 * /usr/bin/example3

		- Cron e Python virtualenv

		0,30 * * * * cd /home/myuser/myproject && venv/bin/python bot.py config/config.ini > /dev/null 2>&1