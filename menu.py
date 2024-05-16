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



SELMARK = '\033[104m\033[30m'
RESET = '\033[0m'
CLEAR = '\033[2J'
CUR0 = '\033[1;1H'
GREY = '\033[90m'

def menu(*items: list[str]):
	selected = 0
	while True:
		# Single draw call :3
		stdout.write(CLEAR + CUR0 + '\n'.join([SELMARK + item + ' <' + RESET if i == selected else item for i, item in enumerate(items)]) + f'\n{GREY}Use arrow keys to navigate{RESET}')
		
		c = getch()

		if c == b'\x03':
			raise KeyboardInterrupt
		
		if c == b'\xe0':
			c = getch().decode()
			if c == 'P': selected += 1
			elif c == 'H': selected -= 1
			selected = max(min(selected, len(items) - 1), 0)
		
		if c == b'\r':
			stdout.write(CLEAR + CUR0)
			return selected

if __name__ == '__main__':
	print(menu('farts', 'poops', 'shitss'))
