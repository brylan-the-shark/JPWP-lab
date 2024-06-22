from sys import stdout



def _find_getch():
	try:
		import termios
	except ImportError:
		import msvcrt
		return msvcrt.getch

	# POSIX system. Create and return a getch that manipulates the tty.
	import sys, tty
	def _getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

	return _getch

getch = _find_getch()



interactive_mode = False

SELMARK = '\033[104m\033[30m'
RESET = '\033[0m'
CLEAR = '\033[2J'
CUR0 = '\033[1;1H'
GREY = '\033[90m'
ERR = '\033[91m'

def error(msg: str):
	stdout.write(ERR + msg + RESET + '\n')

def clear():
	stdout.write(CLEAR + CUR0)

def menu(*items: list[str], msg: str = None):
	if interactive_mode:
		selected = 0
		while True:
			# Single draw call :3
			stdout.write(CLEAR + CUR0 + '\n'.join([SELMARK + item + RESET + ' <' if i == selected else item for i, item in enumerate(items)]) + (f'\n{msg}' if msg else '') + f'\n{GREY}Use arrow keys to navigate, ENTER to select...{RESET}\n')
			
			c = getch()

			if c == b'\x03':
				raise KeyboardInterrupt
			
			if c == b'\xe0':
				c = getch().decode()
				if c == 'P': selected += 1
				elif c == 'H': selected -= 1
				selected = max(min(selected, len(items) - 1), 0)
			
			if c == b'\r':
				clear()
				return selected
	else:
		while True:
			stdout.write(CLEAR + CUR0 + '\n'.join([f'{i+1} {item}' for i, item in enumerate(items)]) + (f'\n{msg}' if msg else '') + f'\n{GREY}Type a number, ENTER to select...{RESET}\n')

			try:
				selected = int(input('> ')) - 1
			except ValueError as e:
				stdout.write(CLEAR + CUR0 + 'Must be a number\n')
				pause()
				continue

			if selected < 0 or selected >= len(items):
				stdout.write(CLEAR + CUR0 + 'There is no such option\n')
				pause()
				continue

			clear()
			return selected

def pause(msg: str = None):
	if interactive_mode:
		if msg:
			stdout.write(msg + '\n')
		else:
			stdout.write(f'{GREY}Press any key to continue...{RESET}\n')
		
		getch()
		clear()
	else:
		if msg:
			stdout.write(msg + '\n')
		else:
			stdout.write(f'{GREY}Press ENTER to continue...{RESET}\n')

		input()
		clear()
