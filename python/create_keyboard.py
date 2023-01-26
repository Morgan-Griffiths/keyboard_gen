import json
import os
from keyboard_snippets import footer,header

action_output_dict = {
	0:'action',
	1:'action',
	2:'action',
	3:'action',
	4:'action',
	5:'action',
	6:'action',
	7:'action',
	8:'action',
	9:'action',
	10:'output',
	11:'action',
	12:'action',
	13:'action',
	14:'action',
	15:'action',
	16:'action',
	17:'action',
	18:'action',
	19:'action',
	20:'action',
	21:'action',
	22:'action',
	23:'action',
	24:'action',
	25:'action',
	26:'action',
	27:'action',
	28:'action',
	29:'action',
	30:'action',
	31:'action',
	32:'action',
	33:'action',
	34:'action',
	35:'action',
	36:'output',
	37:'action',
	38:'action',
	39:'action',
	40:'action',
	41:'action',
	42:'output',
	43:'output',
	44:'output',
	45:'action',
	46:'action',
	47:'action',
	48:'output',
	49:'action',
	50:'output',
	51:'output',
	52:'output',
	53:'output',
	54:'output',
	55:'output',
	56:'output',
	57:'output',
	58:'output',
	59:'output',
	60:'output',
	61:'output',
	62:'output',
	63:'output',
	64:'output',
	65:'output',
	66:'output',
	67:'output',
	68:'output',
	69:'output',
	70:'output',
	71:'output',
	72:'output',
	73:'output',
	74:'output',
	75:'output',
	76:'output',
	77:'output',
	78:'output',
	79:'output',
	80:'output',

}

uppercase_dictionary = {
	"A": 0,
	"B": 11,
	"C": 8,
	"D": 2,
	"E": 14,
	"F": 3,
	"G": 5,
	"H": 4,
	"I": 34,
	"J": 38,
	"K": 40,
	"L": 37,
	"M": 46,
	"N": 45,
	"O": 31,
	"P": 35,
	"Q": 12,
	"R": 15,
	"S": 1,
	"T": 17,
	"U": 32,
	"V": 9,
	"W": 13,
	"X": 7,
	"Y": 16,
	"Z": 6,
	"!": 18,
	"@": 19,
	"#": 20,
	"$": 21,
	"%": 23,
	"^": 22,
	"&": 26,
	"*": 28,
	"(": 25,
	")": 29,
	"_": 27,
	"+": 24,
	"{": 33,
	"}": 30,
	"|": 42,
	":": 41,
	"\"": 39,
	"<": 43,
	">": 47,
	"?": 44,
	"~": 50,
	"Key.space": 49,
	"Key.enter": 36,
	"Key.backspace": 51,
	"Key.tab": 48,
	# "Key.shift": 65,
	# "Key.esc": 53,
	# "Key.ctrl": 64,
	# "Key.alt": 66,
	# "Key.caps_lock": 67,
	# "Key.cmd": 68,
	# "Key.cmd_r": 69,
	# "Key.option": 70,
	# "Key.option_r": 71,
	# "Key.left": 123,
	# "Key.right": 124,
	# "Key.up": 126,
	# "Key.down": 125,
}

lowercase_dictionary = {
	"a": 0,
	"b": 11,
	"c": 8,
	"d": 2,
	"e": 14,
	"f": 3,
	"g": 5,
	"h": 4,
	"i": 34,
	"j": 38,
	"k": 40,
	"l": 37,
	"m": 46,
	"n": 45,
	"o": 31,
	"p": 35,
	"q": 12,
	"r": 15,
	"s": 1,
	"t": 17,
	"u": 32,
	"v": 9,
	"w": 13,
	"x": 7,
	"y": 16,
	"z": 6,
	'[': 33,
	"]": 30,
	"\\": 42,
	";": 41,
	"'": 39,
	",": 43,
	".": 47,
	"/": 44,
	"`": 50,
	"Key.space": 49,
	"Key.enter": 36,
	"Key.backspace": 51,
	"Key.tab": 48,
	# "Key.shift": 65,
	# "Key.esc": 53,
	# "Key.ctrl": 64,
	# "Key.alt": 66,
	# "Key.caps_lock": 67,
	# "Key.cmd": 68,
	# "Key.cmd_r": 69,
	# "Key.option": 70,
	# "Key.option_r": 71,
	# "Key.left": 123,
	# "Key.right": 124,
	# "Key.up": 126,
	# "Key.down": 125,
	}

modifier_to_key = {
	"Key.space": 'space',
	"Key.enter": '&#x000D;',
	"Key.backspace": '&#x0008;',
	"Key.tab": '&#x0009;',
}


indexToLowercase = {v: k for k, v in lowercase_dictionary.items()}
indexToUppercase = {v: k for k, v in uppercase_dictionary.items()}

def save_keyboard_layout(keyboard_layout):
	# Save the keyboard layout to a file
	with open('assets/keyboard_layout.keylayout','w') as f:
		f.write(keyboard_layout)
	with open(f'{os.path.expanduser("~")}/Library/Keyboard Layouts/custom_keyboard.keylayout','w') as f:
		f.write(keyboard_layout)

def create_keyboard_layout(keyboard_layout:dict):
	def get_key(key):
		try:
			k = keyboard_layout[key]
			if k in modifier_to_key:
				return modifier_to_key[k]
			else:
				return k
		except:
			return key

	keyboard_content = f"""
			<keyMap index="0">
				<key code="0" action="{get_key('a')}"/>
				<key code="1" action="{get_key('b')}"/>
				<key code="2" action="{get_key('d')}"/>
				<key code="3" action="{get_key('f')}"/>
				<key code="4" action="{get_key('h')}"/>
				<key code="5" action="{get_key('g')}"/>
				<key code="6" action="{get_key('z')}"/>
				<key code="7" action="{get_key('x')}"/>
				<key code="8" action="{get_key('c')}"/>
				<key code="9" action="{get_key('v')}"/>
				<key code="10" output="§"/>
				<key code="11" action="{get_key('b')}"/>
				<key code="12" action="{get_key('q')}"/>
				<key code="13" action="{get_key('w')}"/>
				<key code="14" action="{get_key('e')}"/>
				<key code="15" action="{get_key('r')}"/>
				<key code="16" action="{get_key('y')}"/>
				<key code="17" action="{get_key('t')}"/>
				<key code="18" action="{get_key('1')}"/>
				<key code="19" action="{get_key('2')}"/>
				<key code="20" action="{get_key('3')}"/>
				<key code="21" action="{get_key('4')}"/>
				<key code="22" action="{get_key('6')}"/>
				<key code="23" action="{get_key('5')}"/>
				<key code="24" action="{get_key('=')}"/>
				<key code="25" action="{get_key('9')}"/>
				<key code="26" action="{get_key('7')}"/>
				<key code="27" action="{get_key('-')}"/>
				<key code="28" action="{get_key('8')}"/>
				<key code="29" action="{get_key('0')}"/>
				<key code="30" action="{get_key(']')}"/>
				<key code="31" action="{get_key('o')}"/>
				<key code="32" action="{get_key('u')}"/>
				<key code="33" action="{get_key('[')}"/>
				<key code="34" action="{get_key('i')}"/>
				<key code="35" action="{get_key('p')}"/>
				<key code="36" output="&#x000D;"/>
				<key code="37" action="{get_key('l')}"/>
				<key code="38" action="{get_key('j')}"/>
				<key code="39" action="&#x0027;"/>
				<key code="40" action="{get_key('k')}"/>
				<key code="41" action="{get_key(';')}"/>
				<key code="42" output="{get_key(chr(92))}"/>
				<key code="43" output="{get_key(',')}"/>
				<key code="44" output="{get_key('/')}"/>
				<key code="45" action="{get_key('n')}"/>
				<key code="46" action="{get_key('m')}"/>
				<key code="47" action="{get_key('.')}"/>
				<key code="48" output="&#x0009;"/>
				<key code="49" action="{get_key('Key.space')}"/>
				<key code="50" output="{get_key('`')}"/>
				<key code="51" output="&#x0008;"/>
				<key code="52" output="&#x0003;"/>
				<key code="53" output="&#x001B;"/>
				<key code="64" output="&#x0010;"/>
				<key code="65" output="{get_key('.')}"/>
				<key code="66" output="&#x001D;"/>
				<key code="67" output="{get_key('*')}"/>
				<key code="69" output="{get_key('+')}"/>
				<key code="70" output="&#x001C;"/>
				<key code="71" output="&#x001B;"/>
				<key code="72" output="&#x001F;"/>
				<key code="75" output="{get_key('/')}"/>
				<key code="76" output="&#x0003;"/>
				<key code="77" output="&#x001E;"/>
				<key code="78" output="{get_key('-')}"/>
				<key code="79" output="&#x0010;"/>
				<key code="80" output="&#x0010;"/>
				<key code="81" output="{get_key('=')}"/>
				<key code="82" output="{get_key('0')}"/>
				<key code="83" output="{get_key('1')}"/>
				<key code="84" output="{get_key('2')}"/>
				<key code="85" output="{get_key('3')}"/>
				<key code="86" output="{get_key('4')}"/>
				<key code="87" output="{get_key('5')}"/>
				<key code="88" output="{get_key('6')}"/>
				<key code="89" output="{get_key('7')}"/>
				<key code="91" output="{get_key('8')}"/>
				<key code="92" output="{get_key('9')}"/>
				<key code="96" output="&#x0010;"/>
				<key code="97" output="&#x0010;"/>
				<key code="98" output="&#x0010;"/>
				<key code="99" output="&#x0010;"/>
				<key code="100" output="&#x0010;"/>
				<key code="101" output="&#x0010;"/>
				<key code="102" output="&#x0010;"/>
				<key code="103" output="&#x0010;"/>
				<key code="104" output="&#x0010;"/>
				<key code="105" output="&#x0010;"/>
				<key code="106" output="&#x0010;"/>
				<key code="107" output="&#x0010;"/>
				<key code="108" output="&#x0010;"/>
				<key code="109" output="&#x0010;"/>
				<key code="110" output="&#x0010;"/>
				<key code="111" output="&#x0010;"/>
				<key code="112" output="&#x0010;"/>
				<key code="113" output="&#x0010;"/>
				<key code="114" output="&#x0005;"/>
				<key code="115" output="&#x0001;"/>
				<key code="116" output="&#x000B;"/>
				<key code="117" output="&#x007F;"/>
				<key code="118" output="&#x0010;"/>
				<key code="119" output="&#x0004;"/>
				<key code="120" output="&#x0010;"/>
				<key code="121" output="&#x000C;"/>
				<key code="122" output="&#x0010;"/>
				<key code="123" output="&#x001C;"/>
				<key code="124" output="&#x001D;"/>
				<key code="125" output="&#x001F;"/>
				<key code="126" output="&#x001E;"/>
			</keyMap>
			<keyMap index="1">
				<key code="0" action="{get_key('S')}"/>
				<key code="1" action="{get_key('A')}"/>
				<key code="2" action="{get_key('D')}"/>
				<key code="3" action="{get_key('F')}"/>
				<key code="4" action="{get_key('H')}"/>
				<key code="5" action="{get_key('G')}"/>
				<key code="6" action="{get_key('Z')}"/>
				<key code="7" action="{get_key('X')}"/>
				<key code="8" action="{get_key('C')}"/>
				<key code="9" action="{get_key('V')}"/>
				<key code="10" output="±"/>
				<key code="11" action="{get_key('B')}"/>
				<key code="12" action="{get_key('Q')}"/>
				<key code="13" action="{get_key('W')}"/>
				<key code="14" action="{get_key('E')}"/>
				<key code="15" action="{get_key('R')}"/>
				<key code="16" action="{get_key('Y')}"/>
				<key code="17" action="{get_key('T')}"/>
				<key code="18" action="{get_key('!')}"/>
				<key code="19" action="{get_key('@')}"/>
				<key code="20" action="{get_key('#')}"/>
				<key code="21" action="{get_key('$')}"/>
				<key code="22" action="{get_key('^')}"/>
				<key code="23" action="{get_key('%')}"/>
				<key code="24" action="{get_key('+')}"/>
				<key code="25" action="{get_key('(')}"/>
				<key code="26" action="&#x0026;"/>
				<key code="27" action="{get_key('_')}"/>
				<key code="28" action="{get_key('*')}"/>
				<key code="29" action="{get_key(')')}"/>
				<key code="30" action="{'}'}"/>
				<key code="31" action="{get_key('O')}"/>
				<key code="32" action="{get_key('U')}"/>
				<key code="33" action="{'{'}"/>
				<key code="34" action="{get_key('I')}"/>
				<key code="35" action="{get_key('P')}"/>
				<key code="36" output="&#x000D;"/>
				<key code="37" action="{get_key('L')}"/>
				<key code="38" action="{get_key('J')}"/>
				<key code="39" action="&#x0022;"/>
				<key code="40" action="{get_key('K')}"/>
				<key code="41" action="{get_key(':')}"/>
				<key code="42" action="{get_key('|')}"/>
				<key code="43" action="&#x003C;"/>
				<key code="44" output="{get_key('?')}"/>
				<key code="45" action="{get_key('N')}"/>
				<key code="46" action="{get_key('M')}"/>
				<key code="47" action="&#x003E;"/>
				<key code="48" output="&#x0009;"/>
				<key code="49" action="{get_key('Key.space')}"/>
				<key code="50" action="{get_key('~')}"/>
				<key code="51" output="&#x0008;"/>
				<key code="52" output="&#x0003;"/>
				<key code="53" output="&#x001B;"/>
				<key code="64" output="&#x0010;"/>
				<key code="65" output="{get_key('.')}"/>
				<key code="66" output="{get_key('*')}"/>
				<key code="67" output="{get_key('*')}"/>
				<key code="69" output="{get_key('+')}"/>
				<key code="70" output="{get_key('+')}"/>
				<key code="71" output="&#x001B;"/>
				<key code="72" output="{get_key('=')}"/>
				<key code="75" output="{get_key('/')}"/>
				<key code="76" output="&#x0003;"/>
				<key code="77" output="{get_key('/')}"/>
				<key code="78" output="{get_key('-')}"/>
				<key code="79" output="&#x0010;"/>
				<key code="80" output="&#x0010;"/>
				<key code="81" output="{get_key('=')}"/>
				<key code="82" output="{get_key('0')}"/>
				<key code="83" output="{get_key('1')}"/>
				<key code="84" output="{get_key('2')}"/>
				<key code="85" output="{get_key('3')}"/>
				<key code="86" output="{get_key('4')}"/>
				<key code="87" output="{get_key('5')}"/>
				<key code="88" output="{get_key('6')}"/>
				<key code="89" output="{get_key('7')}"/>
				<key code="91" output="{get_key('8')}"/>
				<key code="92" output="{get_key('9')}"/>
				<key code="96" output="&#x0010;"/>
				<key code="97" output="&#x0010;"/>
				<key code="98" output="&#x0010;"/>
				<key code="99" output="&#x0010;"/>
				<key code="100" output="&#x0010;"/>
				<key code="101" output="&#x0010;"/>
				<key code="102" output="&#x0010;"/>
				<key code="103" output="&#x0010;"/>
				<key code="104" output="&#x0010;"/>
				<key code="105" output="&#x0010;"/>
				<key code="106" output="&#x0010;"/>
				<key code="107" output="&#x0010;"/>
				<key code="108" output="&#x0010;"/>
				<key code="109" output="&#x0010;"/>
				<key code="110" output="&#x0010;"/>
				<key code="111" output="&#x0010;"/>
				<key code="112" output="&#x0010;"/>
				<key code="113" output="&#x0010;"/>
				<key code="114" output="&#x0005;"/>
				<key code="115" output="&#x0001;"/>
				<key code="116" output="&#x000B;"/>
				<key code="117" output="&#x007F;"/>
				<key code="118" output="&#x0010;"/>
				<key code="119" output="&#x0004;"/>
				<key code="120" output="&#x0010;"/>
				<key code="121" output="&#x000C;"/>
				<key code="122" output="&#x0010;"/>
				<key code="123" output="&#x001C;"/>
				<key code="124" output="&#x001D;"/>
				<key code="125" output="&#x001F;"/>
				<key code="126" output="&#x001E;"/>
			</keyMap>
			<keyMap index="2">
				<key code="0" action="{get_key('A')}"/>
				<key code="1" action="{get_key('S')}"/>
				<key code="2" action="{get_key('D')}"/>
				<key code="3" action="{get_key('F')}"/>
				<key code="4" action="{get_key('H')}"/>
				<key code="5" action="{get_key('G')}"/>
				<key code="6" action="{get_key('Z')}"/>
				<key code="7" action="{get_key('X')}"/>
				<key code="8" action="{get_key('C')}"/>
				<key code="9" action="{get_key('V')}"/>
				<key code="10" output="§"/>
				<key code="11" action="{get_key('B')}"/>
				<key code="12" action="{get_key('Q')}"/>
				<key code="13" action="{get_key('W')}"/>
				<key code="14" action="{get_key('E')}"/>
				<key code="15" action="{get_key('R')}"/>
				<key code="16" action="{get_key('Y')}"/>
				<key code="17" action="{get_key('T')}"/>
				<key code="18" action="{get_key('1')}"/>
				<key code="19" action="{get_key('2')}"/>
				<key code="20" action="{get_key('3')}"/>
				<key code="21" action="{get_key('4')}"/>
				<key code="22" action="{get_key('6')}"/>
				<key code="23" action="{get_key('5')}"/>
				<key code="24" action="{get_key('=')}"/>
				<key code="25" action="{get_key('9')}"/>
				<key code="26" action="{get_key('7')}"/>
				<key code="27" action="{get_key('-')}"/>
				<key code="28" action="{get_key('8')}"/>
				<key code="29" action="{get_key('0')}"/>
				<key code="30" output="{get_key(']')}"/>
				<key code="31" action="{get_key('O')}"/>
				<key code="32" action="{get_key('U')}"/>
				<key code="33" output="{get_key('[')}"/>
				<key code="34" action="{get_key('I')}"/>
				<key code="35" action="{get_key('P')}"/>
				<key code="36" output="&#x000D;"/>
				<key code="37" action="{get_key('L')}"/>
				<key code="38" action="{get_key('J')}"/>
				<key code="39" output="&#x0027;"/>
				<key code="40" action="{get_key('K')}"/>
				<key code="41" output="{get_key(';')}"/>
				<key code="42" output="{get_key(chr(39))}"/>
				<key code="43" output="{get_key(',')}"/>
				<key code="44" output="{get_key('/')}"/>
				<key code="45" action="{get_key('N')}"/>
				<key code="46" action="{get_key('M')}"/>
				<key code="47" output="{get_key('.')}"/>
				<key code="48" output="&#x0009;"/>
				<key code="49" action="{get_key('Key.space')}"/>
				<key code="50" output="{get_key('`')}"/>
				<key code="51" output="&#x0008;"/>
				<key code="52" output="&#x0003;"/>
				<key code="53" output="&#x001B;"/>
				<key code="64" output="&#x0010;"/>
				<key code="65" output="{get_key('.')}"/>
				<key code="66" output="&#x001D;"/>
				<key code="67" output="{get_key('*')}"/>
				<key code="69" output="{get_key('+')}"/>
				<key code="70" output="&#x001C;"/>
				<key code="71" output="&#x001B;"/>
				<key code="72" output="&#x001F;"/>
				<key code="75" output="{get_key('/')}"/>
				<key code="76" output="&#x0003;"/>
				<key code="77" output="&#x001E;"/>
				<key code="78" output="{get_key('-')}"/>
				<key code="79" output="&#x0010;"/>
				<key code="80" output="&#x0010;"/>
				<key code="81" output="{get_key('=')}"/>
				<key code="82" output="{get_key('0')}"/>
				<key code="83" output="{get_key('1')}"/>
				<key code="84" output="{get_key('2')}"/>
				<key code="85" output="{get_key('3')}"/>
				<key code="86" output="{get_key('4')}"/>
				<key code="87" output="{get_key('5')}"/>
				<key code="88" output="{get_key('6')}"/>
				<key code="89" output="{get_key('7')}"/>
				<key code="91" output="{get_key('8')}"/>
				<key code="92" output="{get_key('9')}"/>
				<key code="96" output="&#x0010;"/>
				<key code="97" output="&#x0010;"/>
				<key code="98" output="&#x0010;"/>
				<key code="99" output="&#x0010;"/>
				<key code="100" output="&#x0010;"/>
				<key code="101" output="&#x0010;"/>
				<key code="102" output="&#x0010;"/>
				<key code="103" output="&#x0010;"/>
				<key code="104" output="&#x0010;"/>
				<key code="105" output="&#x0010;"/>
				<key code="106" output="&#x0010;"/>
				<key code="107" output="&#x0010;"/>
				<key code="108" output="&#x0010;"/>
				<key code="109" output="&#x0010;"/>
				<key code="110" output="&#x0010;"/>
				<key code="111" output="&#x0010;"/>
				<key code="112" output="&#x0010;"/>
				<key code="113" output="&#x0010;"/>
				<key code="114" output="&#x0005;"/>
				<key code="115" output="&#x0001;"/>
				<key code="116" output="&#x000B;"/>
				<key code="117" output="&#x007F;"/>
				<key code="118" output="&#x0010;"/>
				<key code="119" output="&#x0004;"/>
				<key code="120" output="&#x0010;"/>
				<key code="121" output="&#x000C;"/>
				<key code="122" output="&#x0010;"/>
				<key code="123" output="&#x001C;"/>
				<key code="124" output="&#x001D;"/>
				<key code="125" output="&#x001F;"/>
				<key code="126" output="&#x001E;"/>
			</keyMap>  
	"""
	# print(keyboard_content)
	return header + keyboard_content + footer

header = """ <?xml version="1.1" encoding="UTF-8"?>
<!DOCTYPE keyboard SYSTEM "file://localhost/System/Library/DTDs/KeyboardLayout.dtd">
<!--Last edited by Ukelele version 3.2.2.166 on 2017-02-16 at 16:36 (GMT+1)-->
<keyboard group="126" id="-14519" name="Morgan v1.2" maxout="1">
	<layouts>
		<layout first="0" last="17" mapSet="16c" modifiers="f4"/>
		<layout first="18" last="18" mapSet="994" modifiers="f4"/>
		<layout first="21" last="23" mapSet="994" modifiers="f4"/>
		<layout first="30" last="30" mapSet="994" modifiers="f4"/>
		<layout first="194" last="194" mapSet="994" modifiers="f4"/>
		<layout first="197" last="197" mapSet="994" modifiers="f4"/>
		<layout first="200" last="201" mapSet="994" modifiers="f4"/>
		<layout first="206" last="207" mapSet="994" modifiers="f4"/>
	</layouts>
	<modifierMap id="f4" defaultIndex="7">
		<keyMapSelect mapIndex="0">
			<modifier keys="command?"/>
			<modifier keys="anyShift? caps? command"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="1">
			<modifier keys="anyShift caps?"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="2">
			<modifier keys="caps"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="3">
			<modifier keys="anyOption"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="4">
			<modifier keys="anyShift caps? anyOption command?"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="5">
			<modifier keys="caps anyOption"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="6">
			<modifier keys="caps? anyOption command"/>
		</keyMapSelect>
		<keyMapSelect mapIndex="7">
			<modifier keys="anyShift caps? option? command? control"/>
			<modifier keys="shift? caps? anyOption command? control"/>
			<modifier keys="caps? anyOption? command? control"/>
		</keyMapSelect>
	</modifierMap>
	<keyMapSet id="16c">
"""

footer = """ 
		<keyMap index="3">
			<key code="0" action="ä"/>
			<key code="1" output="ß"/>
			<key code="2" output="đ"/>
			<key code="3" output="è"/>
			<key code="4" output="ù"/>
			<key code="5" output="é"/>
			<key code="6" output="à"/>
			<key code="7" output="á"/>
			<key code="8" output="ç"/>
			<key code="9" output="ì"/>
			<key code="10" output="§"/>
			<key code="11" output="í"/>
			<key code="12" action="æ"/>
			<key code="13" output="å"/>
			<key code="14" action="ë"/>
			<key code="15" output="ý"/>
			<key code="16" output="ÿ"/>
			<key code="17" output="þ"/>
			<key code="18" output="¡"/>
			<key code="19" output="ª"/>
			<key code="20" output="º"/>
			<key code="21" output="£"/>
			<key code="22" action="6 option"/>
			<key code="23" output="€"/>
			<key code="24" output="×"/>
			<key code="25" output="“"/>
			<key code="26" action="˚"/>
			<key code="27" action="©"/>
			<key code="28" output="„"/>
			<key code="29" output="”"/>
			<key code="30" output="»"/>
			<key code="31" action="ö"/>
			<key code="32" action="ü"/>
			<key code="33" output="«"/>
			<key code="34" action="ï"/>
			<key code="35" output="œ"/>
			<key code="36" output="&#x000D;"/>
			<key code="37" action="ø"/>
			<key code="38" output="ú"/>
			<key code="39" action="´"/>
			<key code="40" output="ĳ"/>
			<key code="41" output="°"/>
			<key code="42" output="¬"/>
			<key code="43" output="ò"/>
			<key code="44" output="¿"/>
			<key code="45" output="ñ"/>
			<key code="46" action="Ω"/>
			<key code="47" output="ó"/>
			<key code="48" output="&#x0009;"/>
			<key code="49" output=" "/>
			<key code="50" action="`"/>
			<key code="51" output="&#x0008;"/>
			<key code="52" output="&#x0003;"/>
			<key code="53" output="&#x001B;"/>
			<key code="64" output="&#x0010;"/>
			<key code="65" output=","/>
			<key code="66" output="&#x001D;"/>
			<key code="67" output="*"/>
			<key code="69" output="+"/>
			<key code="70" output="&#x001C;"/>
			<key code="71" output="&#x001B;"/>
			<key code="72" output="&#x001F;"/>
			<key code="75" output="/"/>
			<key code="76" output="&#x0003;"/>
			<key code="77" output="&#x001E;"/>
			<key code="78" output="-"/>
			<key code="79" output="&#x0010;"/>
			<key code="80" output="&#x0010;"/>
			<key code="81" output="="/>
			<key code="82" output="0"/>
			<key code="83" output="1"/>
			<key code="84" output="2"/>
			<key code="85" output="3"/>
			<key code="86" output="4"/>
			<key code="87" output="5"/>
			<key code="88" output="6"/>
			<key code="89" output="7"/>
			<key code="91" output="8"/>
			<key code="92" output="9"/>
			<key code="96" output="&#x0010;"/>
			<key code="97" output="&#x0010;"/>
			<key code="98" output="&#x0010;"/>
			<key code="99" output="&#x0010;"/>
			<key code="100" output="&#x0010;"/>
			<key code="101" output="&#x0010;"/>
			<key code="102" output="&#x0010;"/>
			<key code="103" output="&#x0010;"/>
			<key code="104" output="&#x0010;"/>
			<key code="105" output="&#x0010;"/>
			<key code="106" output="&#x0010;"/>
			<key code="107" output="&#x0010;"/>
			<key code="108" output="&#x0010;"/>
			<key code="109" output="&#x0010;"/>
			<key code="110" output="&#x0010;"/>
			<key code="111" output="&#x0010;"/>
			<key code="112" output="&#x0010;"/>
			<key code="113" output="&#x0010;"/>
			<key code="114" output="&#x0005;"/>
			<key code="115" output="&#x0001;"/>
			<key code="116" output="&#x000B;"/>
			<key code="117" output="&#x007F;"/>
			<key code="118" output="&#x0010;"/>
			<key code="119" output="&#x0004;"/>
			<key code="120" output="&#x0010;"/>
			<key code="121" output="&#x000C;"/>
			<key code="122" output="&#x0010;"/>
			<key code="123" output="&#x001C;"/>
			<key code="124" output="&#x001D;"/>
			<key code="125" output="&#x001F;"/>
			<key code="126" output="&#x001E;"/>
		</keyMap>
		<keyMap index="4">
			<key code="0" action="Ä"/>
			<key code="1" output="§"/>
			<key code="2" output="Đ"/>
			<key code="3" output="È"/>
			<key code="4" output="Ù"/>
			<key code="5" output="É"/>
			<key code="6" output="À"/>
			<key code="7" output="Á"/>
			<key code="8" output="Ç"/>
			<key code="9" output="Ì"/>
			<key code="10" output="±"/>
			<key code="11" output="Í"/>
			<key code="12" action="Æ"/>
			<key code="13" output="Å"/>
			<key code="14" action="Ë"/>
			<key code="15" output="Ý"/>
			<key code="16" output="Ÿ"/>
			<key code="17" output="Þ"/>
			<key code="18" output="¹"/>
			<key code="19" output="²"/>
			<key code="20" output="³"/>
			<key code="21" output="¥"/>
			<key code="22" action="ˇ"/>
			<key code="23" output="¢"/>
			<key code="24" output="÷"/>
			<key code="25" output="‘"/>
			<key code="26" action="¯"/>
			<key code="27" output="№"/>
			<key code="28" output="‚"/>
			<key code="29" output="’"/>
			<key code="30" output="›"/>
			<key code="31" action="Ö"/>
			<key code="32" action="Ü"/>
			<key code="33" output="‹"/>
			<key code="34" action="Ï"/>
			<key code="35" output="Œ"/>
			<key code="36" output="&#x000D;"/>
			<key code="37" action="Ø"/>
			<key code="38" output="Ú"/>
			<key code="39" action="¨"/>
			<key code="40" output="Ĳ"/>
			<key code="41" output="·"/>
			<key code="42" output="¦"/>
			<key code="43" output="Ò"/>
			<key code="44" output="…"/>
			<key code="45" output="Ñ"/>
			<key code="46" action="√"/>
			<key code="47" output="Ó"/>
			<key code="48" output="&#x0009;"/>
			<key code="49" output=" "/>
			<key code="50" action="~ option"/>
			<key code="51" output="&#x0008;"/>
			<key code="52" output="&#x0003;"/>
			<key code="53" output="&#x001B;"/>
			<key code="64" output="&#x0010;"/>
			<key code="65" output="."/>
			<key code="66" output="*"/>
			<key code="67" output="*"/>
			<key code="69" output="+"/>
			<key code="70" output="+"/>
			<key code="71" output="&#x001B;"/>
			<key code="72" output="="/>
			<key code="75" output="/"/>
			<key code="76" output="&#x0003;"/>
			<key code="77" output="/"/>
			<key code="78" output="-"/>
			<key code="79" output="&#x0010;"/>
			<key code="80" output="&#x0010;"/>
			<key code="81" output="="/>
			<key code="82" output="0"/>
			<key code="83" output="1"/>
			<key code="84" output="2"/>
			<key code="85" output="3"/>
			<key code="86" output="4"/>
			<key code="87" output="5"/>
			<key code="88" output="6"/>
			<key code="89" output="7"/>
			<key code="91" output="8"/>
			<key code="92" output="9"/>
			<key code="96" output="&#x0010;"/>
			<key code="97" output="&#x0010;"/>
			<key code="98" output="&#x0010;"/>
			<key code="99" output="&#x0010;"/>
			<key code="100" output="&#x0010;"/>
			<key code="101" output="&#x0010;"/>
			<key code="102" output="&#x0010;"/>
			<key code="103" output="&#x0010;"/>
			<key code="104" output="&#x0010;"/>
			<key code="105" output="&#x0010;"/>
			<key code="106" output="&#x0010;"/>
			<key code="107" output="&#x0010;"/>
			<key code="108" output="&#x0010;"/>
			<key code="109" output="&#x0010;"/>
			<key code="110" output="&#x0010;"/>
			<key code="111" output="&#x0010;"/>
			<key code="112" output="&#x0010;"/>
			<key code="113" output="&#x0010;"/>
			<key code="114" output="&#x0005;"/>
			<key code="115" output="&#x0001;"/>
			<key code="116" output="&#x000B;"/>
			<key code="117" output="&#x007F;"/>
			<key code="118" output="&#x0010;"/>
			<key code="119" output="&#x0004;"/>
			<key code="120" output="&#x0010;"/>
			<key code="121" output="&#x000C;"/>
			<key code="122" output="&#x0010;"/>
			<key code="123" output="&#x001C;"/>
			<key code="124" output="&#x001D;"/>
			<key code="125" output="&#x001F;"/>
			<key code="126" output="&#x001E;"/>
		</keyMap>
		<keyMap index="5">
			<key code="0" output="Ä"/>
			<key code="1" output="ß"/>
			<key code="2" output="Ð"/>
			<key code="3" output="È"/>
			<key code="4" output="Ù"/>
			<key code="5" output="É"/>
			<key code="6" output="À"/>
			<key code="7" output="Á"/>
			<key code="8" output="Ç"/>
			<key code="9" output="Ì"/>
			<key code="10" output="§"/>
			<key code="11" output="Í"/>
			<key code="12" action="Æ"/>
			<key code="13" output="Å"/>
			<key code="14" output="Ë"/>
			<key code="15" output="Ý"/>
			<key code="16" output="Ÿ"/>
			<key code="17" output="Þ"/>
			<key code="18" output="¡"/>
			<key code="19" output="ª"/>
			<key code="20" output="º"/>
			<key code="21" output="£"/>
			<key code="22" action="^"/>
			<key code="23" output="€"/>
			<key code="24" output="×"/>
			<key code="25" output="“"/>
			<key code="26" action="˚"/>
			<key code="27" action="©"/>
			<key code="28" output="„"/>
			<key code="29" output="”"/>
			<key code="30" output="»"/>
			<key code="31" output="Ö"/>
			<key code="32" output="Ü"/>
			<key code="33" output="«"/>
			<key code="34" output="Ï"/>
			<key code="35" output="Œ"/>
			<key code="36" output="&#x000D;"/>
			<key code="37" action="Ø"/>
			<key code="38" output="Ú"/>
			<key code="39" action="´"/>
			<key code="40" output="Ĳ"/>
			<key code="41" action="¨"/>
			<key code="42" output="¬"/>
			<key code="43" output="Ò"/>
			<key code="44" output="¿"/>
			<key code="45" output="Ñ"/>
			<key code="46" action="Ω"/>
			<key code="47" output="Ó"/>
			<key code="48" output="&#x0009;"/>
			<key code="49" output=" "/>
			<key code="50" action="`"/>
			<key code="51" output="&#x0008;"/>
			<key code="52" output="&#x0003;"/>
			<key code="53" output="&#x001B;"/>
			<key code="64" output="&#x0010;"/>
			<key code="65" output=","/>
			<key code="66" output="&#x001D;"/>
			<key code="67" output="*"/>
			<key code="69" output="+"/>
			<key code="70" output="&#x001C;"/>
			<key code="71" output="&#x001B;"/>
			<key code="72" output="&#x001F;"/>
			<key code="75" output="/"/>
			<key code="76" output="&#x0003;"/>
			<key code="77" output="&#x001E;"/>
			<key code="78" output="-"/>
			<key code="79" output="&#x0010;"/>
			<key code="80" output="&#x0010;"/>
			<key code="81" output="="/>
			<key code="82" output="0"/>
			<key code="83" output="1"/>
			<key code="84" output="2"/>
			<key code="85" output="3"/>
			<key code="86" output="4"/>
			<key code="87" output="5"/>
			<key code="88" output="6"/>
			<key code="89" output="7"/>
			<key code="91" output="8"/>
			<key code="92" output="9"/>
			<key code="96" output="&#x0010;"/>
			<key code="97" output="&#x0010;"/>
			<key code="98" output="&#x0010;"/>
			<key code="99" output="&#x0010;"/>
			<key code="100" output="&#x0010;"/>
			<key code="101" output="&#x0010;"/>
			<key code="102" output="&#x0010;"/>
			<key code="103" output="&#x0010;"/>
			<key code="104" output="&#x0010;"/>
			<key code="105" output="&#x0010;"/>
			<key code="106" output="&#x0010;"/>
			<key code="107" output="&#x0010;"/>
			<key code="108" output="&#x0010;"/>
			<key code="109" output="&#x0010;"/>
			<key code="110" output="&#x0010;"/>
			<key code="111" output="&#x0010;"/>
			<key code="112" output="&#x0010;"/>
			<key code="113" output="&#x0010;"/>
			<key code="114" output="&#x0005;"/>
			<key code="115" output="&#x0001;"/>
			<key code="116" output="&#x000B;"/>
			<key code="117" output="&#x007F;"/>
			<key code="118" output="&#x0010;"/>
			<key code="119" output="&#x0004;"/>
			<key code="120" output="&#x0010;"/>
			<key code="121" output="&#x000C;"/>
			<key code="122" output="&#x0010;"/>
			<key code="123" output="&#x001C;"/>
			<key code="124" output="&#x001D;"/>
			<key code="125" output="&#x001F;"/>
			<key code="126" output="&#x001E;"/>
		</keyMap>
		<keyMap index="6">
			<key code="0" output="å"/>
			<key code="1" output="ß"/>
			<key code="2" output="∂"/>
			<key code="3" output="ƒ"/>
			<key code="4" output="˙"/>
			<key code="5" output="©"/>
			<key code="6" output="Ω"/>
			<key code="7" output="≈"/>
			<key code="8" output="ç"/>
			<key code="9" output="√"/>
			<key code="10" output="§"/>
			<key code="11" output="∫"/>
			<key code="12" output="œ"/>
			<key code="13" output="∑"/>
			<key code="14" output="´"/>
			<key code="15" output="®"/>
			<key code="16" output="¥"/>
			<key code="17" output="†"/>
			<key code="18" output="¡"/>
			<key code="19" output="™"/>
			<key code="20" output="£"/>
			<key code="21" output="¢"/>
			<key code="22" output="§"/>
			<key code="23" output="∞"/>
			<key code="24" output="≠"/>
			<key code="25" output="ª"/>
			<key code="26" output="¶"/>
			<key code="27" output="–"/>
			<key code="28" output="•"/>
			<key code="29" output="º"/>
			<key code="30" output="‘"/>
			<key code="31" output="ø"/>
			<key code="32" output="¨"/>
			<key code="33" output="“"/>
			<key code="34" output="^"/>
			<key code="35" output="π"/>
			<key code="36" output="&#x000D;"/>
			<key code="37" output="¬"/>
			<key code="38" output="∆"/>
			<key code="39" output="æ"/>
			<key code="40" output="˚"/>
			<key code="41" output="…"/>
			<key code="42" output="«"/>
			<key code="43" output="≤"/>
			<key code="44" output="÷"/>
			<key code="45" output="~"/>
			<key code="46" output="µ"/>
			<key code="47" output="≥"/>
			<key code="48" output="&#x0009;"/>
			<key code="49" output=" "/>
			<key code="50" output="`"/>
			<key code="51" output="&#x0008;"/>
			<key code="52" output="&#x0003;"/>
			<key code="53" output="&#x001B;"/>
			<key code="64" output="&#x0010;"/>
			<key code="65" output="."/>
			<key code="66" output="&#x001D;"/>
			<key code="67" output="*"/>
			<key code="69" output="+"/>
			<key code="70" output="&#x001C;"/>
			<key code="71" output="&#x001B;"/>
			<key code="72" output="&#x001F;"/>
			<key code="75" output="/"/>
			<key code="76" output="&#x0003;"/>
			<key code="77" output="&#x001E;"/>
			<key code="78" output="-"/>
			<key code="79" output="&#x0010;"/>
			<key code="80" output="&#x0010;"/>
			<key code="81" output="="/>
			<key code="82" output="0"/>
			<key code="83" output="1"/>
			<key code="84" output="2"/>
			<key code="85" output="3"/>
			<key code="86" output="4"/>
			<key code="87" output="5"/>
			<key code="88" output="6"/>
			<key code="89" output="7"/>
			<key code="91" output="8"/>
			<key code="92" output="9"/>
			<key code="96" output="&#x0010;"/>
			<key code="97" output="&#x0010;"/>
			<key code="98" output="&#x0010;"/>
			<key code="99" output="&#x0010;"/>
			<key code="100" output="&#x0010;"/>
			<key code="101" output="&#x0010;"/>
			<key code="102" output="&#x0010;"/>
			<key code="103" output="&#x0010;"/>
			<key code="104" output="&#x0010;"/>
			<key code="105" output="&#x0010;"/>
			<key code="106" output="&#x0010;"/>
			<key code="107" output="&#x0010;"/>
			<key code="108" output="&#x0010;"/>
			<key code="109" output="&#x0010;"/>
			<key code="110" output="&#x0010;"/>
			<key code="111" output="&#x0010;"/>
			<key code="112" output="&#x0010;"/>
			<key code="113" output="&#x0010;"/>
			<key code="114" output="&#x0005;"/>
			<key code="115" output="&#x0001;"/>
			<key code="116" output="&#x000B;"/>
			<key code="117" output="&#x007F;"/>
			<key code="118" output="&#x0010;"/>
			<key code="119" output="&#x0004;"/>
			<key code="120" output="&#x0010;"/>
			<key code="121" output="&#x000C;"/>
			<key code="122" output="&#x0010;"/>
			<key code="123" output="&#x001C;"/>
			<key code="124" output="&#x001D;"/>
			<key code="125" output="&#x001F;"/>
			<key code="126" output="&#x001E;"/>
		</keyMap>
		<keyMap index="7">
			<key code="0" output="&#x0001;"/>
			<key code="1" output="&#x0013;"/>
			<key code="2" output="&#x0004;"/>
			<key code="3" output="&#x0006;"/>
			<key code="4" output="&#x0008;"/>
			<key code="5" output="&#x0007;"/>
			<key code="6" output="&#x001A;"/>
			<key code="7" output="&#x0018;"/>
			<key code="8" output="&#x0003;"/>
			<key code="9" output="&#x0016;"/>
			<key code="10" output="0"/>
			<key code="11" output="&#x0002;"/>
			<key code="12" output="&#x0011;"/>
			<key code="13" output="&#x0017;"/>
			<key code="14" output="&#x0005;"/>
			<key code="15" output="&#x0012;"/>
			<key code="16" output="&#x0019;"/>
			<key code="17" output="&#x0014;"/>
			<key code="18" output="1"/>
			<key code="19" output="2"/>
			<key code="20" output="3"/>
			<key code="21" output="4"/>
			<key code="22" output="6"/>
			<key code="23" output="5"/>
			<key code="24" action="="/>
			<key code="25" output="9"/>
			<key code="26" output="7"/>
			<key code="27" output="&#x001F;"/>
			<key code="28" output="8"/>
			<key code="29" output="0"/>
			<key code="30" output="&#x001D;"/>
			<key code="31" output="&#x000F;"/>
			<key code="32" output="&#x0015;"/>
			<key code="33" output="&#x001B;"/>
			<key code="34" output="&#x0009;"/>
			<key code="35" output="&#x0010;"/>
			<key code="36" output="&#x000D;"/>
			<key code="37" output="&#x000C;"/>
			<key code="38" output="&#x000A;"/>
			<key code="39" output="&#x0027;"/>
			<key code="40" output="&#x000B;"/>
			<key code="41" output=";"/>
			<key code="42" output="&#x001C;"/>
			<key code="43" output=","/>
			<key code="44" output="/"/>
			<key code="45" output="&#x000E;"/>
			<key code="46" output="&#x000D;"/>
			<key code="47" output="."/>
			<key code="48" output="&#x0009;"/>
			<key code="49" action="space"/>
			<key code="50" output="`"/>
			<key code="51" output="&#x0008;"/>
			<key code="52" output="&#x0003;"/>
			<key code="53" output="&#x001B;"/>
			<key code="64" output="&#x0010;"/>
			<key code="65" output="."/>
			<key code="66" output="&#x001D;"/>
			<key code="67" output="*"/>
			<key code="69" output="+"/>
			<key code="70" output="&#x001C;"/>
			<key code="71" output="&#x001B;"/>
			<key code="72" output="&#x001F;"/>
			<key code="75" output="/"/>
			<key code="76" output="&#x0003;"/>
			<key code="77" output="&#x001E;"/>
			<key code="78" output="-"/>
			<key code="79" output="&#x0010;"/>
			<key code="80" output="&#x0010;"/>
			<key code="81" output="="/>
			<key code="82" output="0"/>
			<key code="83" output="1"/>
			<key code="84" output="2"/>
			<key code="85" output="3"/>
			<key code="86" output="4"/>
			<key code="87" output="5"/>
			<key code="88" output="6"/>
			<key code="89" output="7"/>
			<key code="91" output="8"/>
			<key code="92" output="9"/>
			<key code="96" output="&#x0010;"/>
			<key code="97" output="&#x0010;"/>
			<key code="98" output="&#x0010;"/>
			<key code="99" output="&#x0010;"/>
			<key code="100" output="&#x0010;"/>
			<key code="101" output="&#x0010;"/>
			<key code="102" output="&#x0010;"/>
			<key code="103" output="&#x0010;"/>
			<key code="104" output="&#x0010;"/>
			<key code="105" output="&#x0010;"/>
			<key code="106" output="&#x0010;"/>
			<key code="107" output="&#x0010;"/>
			<key code="108" output="&#x0010;"/>
			<key code="109" output="&#x0010;"/>
			<key code="110" output="&#x0010;"/>
			<key code="111" output="&#x0010;"/>
			<key code="112" output="&#x0010;"/>
			<key code="113" output="&#x0010;"/>
			<key code="114" output="&#x0005;"/>
			<key code="115" output="&#x0001;"/>
			<key code="116" output="&#x000B;"/>
			<key code="117" output="&#x007F;"/>
			<key code="118" output="&#x0010;"/>
			<key code="119" output="&#x0004;"/>
			<key code="120" output="&#x0010;"/>
			<key code="121" output="&#x000C;"/>
			<key code="122" output="&#x0010;"/>
			<key code="123" output="&#x001C;"/>
			<key code="124" output="&#x001D;"/>
			<key code="125" output="&#x001F;"/>
			<key code="126" output="&#x001E;"/>
		</keyMap>
	</keyMapSet>
	<keyMapSet id="994">
		<keyMap index="0" baseMapSet="16c" baseIndex="0">
			<key code="24" output="^"/>
			<key code="30" output="["/>
			<key code="33" output="@"/>
			<key code="39" output=":"/>
			<key code="42" output="]"/>
			<key code="93" output="¥"/>
			<key code="94" output="_"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="1" baseMapSet="16c" baseIndex="1">
			<key code="19" output="&#x0022;"/>
			<key code="22" output="&#x0026;"/>
			<key code="24" output="~"/>
			<key code="25" output=")"/>
			<key code="26" output="&#x0027;"/>
			<key code="27" output="="/>
			<key code="28" output="("/>
			<key code="29" output="0"/>
			<key code="30" output="{"/>
			<key code="33" output="`"/>
			<key code="39" output="*"/>
			<key code="41" output="+"/>
			<key code="42" output="}"/>
			<key code="93" output="|"/>
			<key code="94" output="_"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="2" baseMapSet="16c" baseIndex="2">
			<key code="24" output="^"/>
			<key code="30" output="["/>
			<key code="33" output="@"/>
			<key code="39" output=":"/>
			<key code="42" output="]"/>
			<key code="93" output="¥"/>
			<key code="94" output="_"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="3" baseMapSet="16c" baseIndex="3">
			<key code="93" output="\"/>
			<key code="94" action="`"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="4" baseMapSet="16c" baseIndex="4">
			<key code="93" output="|"/>
			<key code="94" output="`"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="5" baseMapSet="16c" baseIndex="5">
			<key code="93" output="\"/>
			<key code="94" output="`"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="6" baseMapSet="16c" baseIndex="6">
			<key code="93" output="\"/>
			<key code="94" output="_"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
		<keyMap index="7" baseMapSet="16c" baseIndex="7">
			<key code="93" output="|"/>
			<key code="94" output="_"/>
			<key code="95" output=","/>
			<key code="102" action="space"/>
			<key code="104" action="space"/>
		</keyMap>
	</keyMapSet>
	<actions>
		<action id="!">
			<when state="none" output="!"/>
			<when state="dead: Ω" output="₁"/>
			<when state="dead: √" output="≠"/>
		</action>
		<action id="&#x0022;">
			<when state="none" output="&#x0022;"/>
			<when state="dead: Ω" output="₊"/>
			<when state="dead: √" output="″"/>
		</action>
		<action id="#">
			<when state="none" output="#"/>
			<when state="dead: ˇ" output="Ǯ"/>
			<when state="dead: Ω" output="₃"/>
		</action>
		<action id="$">
			<when state="none" output="$"/>
			<when state="dead: Ω" output="₄"/>
		</action>
		<action id="%">
			<when state="none" output="%"/>
			<when state="dead: Ω" output="₅"/>
			<when state="dead: √" output="‰"/>
		</action>
		<action id="&#x0026;">
			<when state="none" output="&#x0026;"/>
			<when state="dead: Ω" output="₇"/>
			<when state="dead: √" output="∧"/>
		</action>
		<action id="&#x0027;">
			<when state="none" output="&#x0027;"/>
			<when state="dead: Ω" output="₌"/>
			<when state="dead: √" output="′"/>
		</action>
		<action id="(">
			<when state="none" output="("/>
			<when state="dead: Ω" output="₉"/>
		</action>
		<action id=")">
			<when state="none" output=")"/>
			<when state="dead: Ω" output="₀"/>
		</action>
		<action id="*">
			<when state="none" output="*"/>
			<when state="dead: Ω" output="₈"/>
			<when state="dead: √" output="⊗"/>
		</action>
		<action id="+">
			<when state="none" output="+"/>
			<when state="dead: ©" output="⇔"/>
			<when state="dead: Ω" output="⁺"/>
			<when state="dead: √" output="⊕"/>
		</action>
		<action id="-">
			<when state="none" output="-"/>
			<when state="dead: Ω" output="⁻"/>
			<when state="dead: √" output="±"/>
		</action>
		<action id=".">
			<when state="none" output="."/>
			<when state="dead: √" output="⋅"/>
		</action>
		<action id="0">
			<when state="none" output="0"/>
			<when state="dead: Ω" output="⁰"/>
		</action>
		<action id="1">
			<when state="none" output="1"/>
			<when state="dead: ©" output="¼"/>
			<when state="dead: ¯" output="‐"/>
			<when state="dead: Ω" output="¹"/>
		</action>
		<action id="2">
			<when state="none" output="2"/>
			<when state="dead: ©" output="½"/>
			<when state="dead: ¯" output="–"/>
			<when state="dead: Ω" output="²"/>
		</action>
		<action id="3">
			<when state="none" output="3"/>
			<when state="dead: ©" output="¾"/>
			<when state="dead: ¯" output="—"/>
			<when state="dead: ˇ" output="ǯ"/>
			<when state="dead: Ω" output="³"/>
			<when state="dead: √" output="∛"/>
		</action>
		<action id="4">
			<when state="none" output="4"/>
			<when state="dead: ©" output="⅓"/>
			<when state="dead: Ω" output="⁴"/>
			<when state="dead: √" output="∜"/>
		</action>
		<action id="5">
			<when state="none" output="5"/>
			<when state="dead: ©" output="⅔"/>
			<when state="dead: ¯" output="¯"/>
			<when state="dead: ´" output="´"/>
			<when state="dead: ˇ" output="ˇ"/>
			<when state="dead: ˚" output="˚"/>
			<when state="dead: Ω" output="⁵"/>
		</action>
		<action id="6">
			<when state="none" output="6"/>
			<when state="dead: Ω" output="⁶"/>
		</action>
		<action id="6 option">
			<when state="none" next="dead: ^"/>
		</action>
		<action id="7">
			<when state="none" output="7"/>
			<when state="dead: Ω" output="⁷"/>
			<when state="dead: √" output="∡"/>
		</action>
		<action id="8">
			<when state="none" output="8"/>
			<when state="dead: Ω" output="⁸"/>
			<when state="dead: √" output="∠"/>
		</action>
		<action id="9">
			<when state="none" output="9"/>
			<when state="dead: Ω" output="⁹"/>
			<when state="dead: √" output="∟"/>
		</action>
		<action id=":">
			<when state="none" output=":"/>
			<when state="dead: √" output="∴"/>
		</action>
		<action id=";">
			<when state="none" output=";"/>
			<when state="dead: Ω" output="₋"/>
			<when state="dead: √" output="∵"/>
		</action>
		<action id="&#x003C;">
			<when state="none" output="&#x003C;"/>
			<when state="dead: √" output="≤"/>
		</action>
		<action id="=">
			<when state="none" output="="/>
			<when state="dead: ©" output="↔"/>
			<when state="dead: Ω" output="⁼"/>
			<when state="dead: √" output="≝"/>
		</action>
		<action id="&#x003E;">
			<when state="none" output="&#x003E;"/>
			<when state="dead: √" output="≥"/>
		</action>
		<action id="@">
			<when state="none" output="@"/>
			<when state="dead: Ω" output="₂"/>
		</action>
		<action id="A">
			<when state="none" output="A"/>
			<when state="dead: ^" output="Â"/>
			<when state="dead: `" output="À"/>
			<when state="dead: ~" output="Ã"/>
			<when state="dead: ¨" output="Ä"/>
			<when state="dead: ¯" output="Ā"/>
			<when state="dead: ´" output="Á"/>
			<when state="dead: ˇ" output="Ǎ"/>
			<when state="dead: ˚" output="Å"/>
			<when state="dead: Ω" output="Α"/>
			<when state="dead: √" output="∀"/>
		</action>
		<action id="B">
			<when state="none" output="B"/>
			<when state="dead: ¯" output="Ƀ"/>
			<when state="dead: ´" output="Ɓ"/>
			<when state="dead: Ω" output="Β"/>
			<when state="dead: √" output="⊇"/>
		</action>
		<action id="C">
			<when state="none" output="C"/>
			<when state="dead: ^" output="Ĉ"/>
			<when state="dead: ©" output="©"/>
			<when state="dead: ´" output="Ć"/>
			<when state="dead: ˇ" output="Č"/>
			<when state="dead: ˚" output="Ċ"/>
			<when state="dead: Ω" output="Χ"/>
			<when state="dead: √" output="ℂ"/>
		</action>
		<action id="D">
			<when state="none" output="D"/>
			<when state="dead: ¯" output="Đ"/>
			<when state="dead: ˇ" output="Ď"/>
			<when state="dead: Ω" output="Δ"/>
			<when state="dead: √" output="∇"/>
		</action>
		<action id="E">
			<when state="none" output="E"/>
			<when state="dead: ^" output="Ê"/>
			<when state="dead: `" output="È"/>
			<when state="dead: ¨" output="Ë"/>
			<when state="dead: ¯" output="Ē"/>
			<when state="dead: ´" output="É"/>
			<when state="dead: ˇ" output="Ě"/>
			<when state="dead: ˚" output="Ė"/>
			<when state="dead: Ω" output="Ε"/>
			<when state="dead: √" output="∃"/>
		</action>
		<action id="F">
			<when state="none" output="F"/>
			<when state="dead: Ω" output="Φ"/>
			<when state="dead: √" output="∎"/>
		</action>
		<action id="G">
			<when state="none" output="G"/>
			<when state="dead: ^" output="Ĝ"/>
			<when state="dead: ¯" output="Ḡ"/>
			<when state="dead: ´" output="Ǵ"/>
			<when state="dead: ˇ" output="Ǧ"/>
			<when state="dead: ˚" output="Ġ"/>
			<when state="dead: Ω" output="Γ"/>
			<when state="dead: √" output="⊃"/>
		</action>
		<action id="H">
			<when state="none" output="H"/>
			<when state="dead: ^" output="Ĥ"/>
			<when state="dead: ¨" output="Ḧ"/>
			<when state="dead: ©" output="⇐"/>
			<when state="dead: ¯" output="Ħ"/>
			<when state="dead: ˇ" output="Ȟ"/>
			<when state="dead: Ω" output="Θ"/>
			<when state="dead: √" output="⊅"/>
		</action>
		<action id="I">
			<when state="none" output="I"/>
			<when state="dead: ^" output="Î"/>
			<when state="dead: `" output="Ì"/>
			<when state="dead: ~" output="Ĩ"/>
			<when state="dead: ¨" output="Ï"/>
			<when state="dead: ©" output="⇗"/>
			<when state="dead: ¯" output="Ī"/>
			<when state="dead: ´" output="Í"/>
			<when state="dead: ˇ" output="Ǐ"/>
			<when state="dead: ˚" output="İ"/>
			<when state="dead: Ω" output="Η"/>
		</action>
		<action id="J">
			<when state="none" output="J"/>
			<when state="dead: ^" output="Ĵ"/>
			<when state="dead: ©" output="⇓"/>
			<when state="dead: Ω" output="Ι"/>
		</action>
		<action id="K">
			<when state="none" output="K"/>
			<when state="dead: ©" output="⇑"/>
			<when state="dead: ´" output="Ḱ"/>
			<when state="dead: ˇ" output="Ǩ"/>
			<when state="dead: Ω" output="Κ"/>
			<when state="dead: √" output="∌"/>
		</action>
		<action id="L">
			<when state="none" output="L"/>
			<when state="dead: ©" output="⇒"/>
			<when state="dead: ¯" output="Ḻ"/>
			<when state="dead: ´" output="Ł"/>
			<when state="dead: ˇ" output="Ľ"/>
			<when state="dead: Ω" output="Λ"/>
			<when state="dead: √" output="∦"/>
		</action>
		<action id="M">
			<when state="none" output="M"/>
			<when state="dead: ©" output="⇘"/>
			<when state="dead: ´" output="Ḿ"/>
			<when state="dead: Ω" output="Μ"/>
			<when state="dead: √" output="∉"/>
		</action>
		<action id="N">
			<when state="none" output="N"/>
			<when state="dead: ~" output="Ñ"/>
			<when state="dead: ©" output="⇙"/>
			<when state="dead: ´" output="Ń"/>
			<when state="dead: ˇ" output="Ň"/>
			<when state="dead: Ω" output="Ν"/>
			<when state="dead: √" output="ℕ"/>
		</action>
		<action id="O">
			<when state="none" output="O"/>
			<when state="dead: ^" output="Ô"/>
			<when state="dead: `" output="Ò"/>
			<when state="dead: ~" output="Õ"/>
			<when state="dead: ¨" output="Ö"/>
			<when state="dead: ¯" output="Ō"/>
			<when state="dead: ´" output="Ó"/>
			<when state="dead: ˇ" output="Ǒ"/>
			<when state="dead: Ω" output="Ο"/>
			<when state="dead: √" output="∅"/>
		</action>
		<action id="P">
			<when state="none" output="P"/>
			<when state="dead: ©" output="℗"/>
			<when state="dead: ´" output="Ṕ"/>
			<when state="dead: Ω" output="Π"/>
			<when state="dead: √" output="ℙ"/>
		</action>
		<action id="Q">
			<when state="none" output="Q"/>
			<when state="dead: Ω" output="Ω"/>
			<when state="dead: √" output="ℚ"/>
		</action>
		<action id="R">
			<when state="none" output="R"/>
			<when state="dead: ©" output="®"/>
			<when state="dead: ´" output="Ŕ"/>
			<when state="dead: ˇ" output="Ř"/>
			<when state="dead: Ω" output="Ρ"/>
			<when state="dead: √" output="ℝ"/>
		</action>
		<action id="S">
			<when state="none" output="S"/>
			<when state="dead: ^" output="Ŝ"/>
			<when state="dead: ©" output="℠"/>
			<when state="dead: ´" output="Ś"/>
			<when state="dead: ˇ" output="Š"/>
			<when state="dead: Ω" output="Σ"/>
			<when state="dead: √" output="∫"/>
		</action>
		<action id="T">
			<when state="none" output="T"/>
			<when state="dead: ©" output="™"/>
			<when state="dead: ¯" output="Ŧ"/>
			<when state="dead: ˇ" output="Ť"/>
			<when state="dead: Ω" output="Τ"/>
		</action>
		<action id="U">
			<when state="none" output="U"/>
			<when state="dead: ^" output="Û"/>
			<when state="dead: `" output="Ù"/>
			<when state="dead: ~" output="Ũ"/>
			<when state="dead: ¨" output="Ü"/>
			<when state="dead: ©" output="⇖"/>
			<when state="dead: ¯" output="Ū"/>
			<when state="dead: ´" output="Ú"/>
			<when state="dead: ˇ" output="Ǔ"/>
			<when state="dead: ˚" output="Ů"/>
			<when state="dead: Ω" output="Ω"/>
			<when state="dead: √" output="∖"/>
		</action>
		<action id="V">
			<when state="none" output="V"/>
			<when state="dead: Ω" output="Β"/>
		</action>
		<action id="W">
			<when state="none" output="W"/>
			<when state="dead: ^" output="Ŵ"/>
			<when state="dead: ¨" output="Ẅ"/>
			<when state="dead: ´" output="Ẃ"/>
			<when state="dead: Ω" output="Ψ"/>
		</action>
		<action id="X">
			<when state="none" output="X"/>
			<when state="dead: ¨" output="Ẍ"/>
			<when state="dead: Ω" output="Ξ"/>
			<when state="dead: √" output="∄"/>
		</action>
		<action id="Y">
			<when state="none" output="Y"/>
			<when state="dead: ^" output="Ŷ"/>
			<when state="dead: ~" output="Ỹ"/>
			<when state="dead: ¨" output="Ÿ"/>
			<when state="dead: ¯" output="Ȳ"/>
			<when state="dead: ´" output="Ý"/>
			<when state="dead: Ω" output="Υ"/>
		</action>
		<action id="Z">
			<when state="none" output="Z"/>
			<when state="dead: ´" output="Ź"/>
			<when state="dead: ˇ" output="Ž"/>
			<when state="dead: ˚" output="Ż"/>
			<when state="dead: Ω" output="Ζ"/>
			<when state="dead: √" output="ℤ"/>
		</action>
		<action id="[">
			<when state="none" output="["/>
			<when state="dead: Ω" output="⁽"/>
		</action>
		<action id="]">
			<when state="none" output="]"/>
			<when state="dead: Ω" output="⁾"/>
		</action>
		<action id="^">
			<when state="none" output="^"/>
			<when state="dead: Ω" output="₆"/>
			<when state="dead: √" output="℘"/>
		</action>
		<action id="_">
			<when state="none" output="_"/>
		</action>
		<action id="`">
			<when state="none" next="dead: `"/>
		</action>
		<action id="a">
			<when state="none" output="a"/>
			<when state="dead: ^" output="â"/>
			<when state="dead: `" output="à"/>
			<when state="dead: ~" output="ã"/>
			<when state="dead: ¨" output="ä"/>
			<when state="dead: ¯" output="ā"/>
			<when state="dead: ´" output="á"/>
			<when state="dead: ˇ" output="ǎ"/>
			<when state="dead: ˚" output="å"/>
			<when state="dead: Ω" output="α"/>
		</action>
		<action id="b">
			<when state="none" output="b"/>
			<when state="dead: ¯" output="ƀ"/>
			<when state="dead: ´" output="ɓ"/>
			<when state="dead: Ω" output="β"/>
			<when state="dead: √" output="⊆"/>
		</action>
		<action id="c">
			<when state="none" output="c"/>
			<when state="dead: ^" output="ĉ"/>
			<when state="dead: ©" output="©"/>
			<when state="dead: ´" output="ć"/>
			<when state="dead: ˇ" output="č"/>
			<when state="dead: ˚" output="ċ"/>
			<when state="dead: Ω" output="χ"/>
			<when state="dead: √" output="∝"/>
		</action>
		<action id="d">
			<when state="none" output="d"/>
			<when state="dead: ¯" output="đ"/>
			<when state="dead: ˇ" output="ď"/>
			<when state="dead: Ω" output="δ"/>
			<when state="dead: √" output="Δ"/>
		</action>
		<action id="e">
			<when state="none" output="e"/>
			<when state="dead: ^" output="ê"/>
			<when state="dead: `" output="è"/>
			<when state="dead: ¨" output="ë"/>
			<when state="dead: ¯" output="ē"/>
			<when state="dead: ´" output="é"/>
			<when state="dead: ˇ" output="ě"/>
			<when state="dead: ˚" output="ė"/>
			<when state="dead: Ω" output="ε"/>
		</action>
		<action id="f">
			<when state="none" output="f"/>
			<when state="dead: Ω" output="φ"/>
			<when state="dead: √" output="ƒ"/>
		</action>
		<action id="g">
			<when state="none" output="g"/>
			<when state="dead: ^" output="ĝ"/>
			<when state="dead: ¯" output="ḡ"/>
			<when state="dead: ´" output="ǵ"/>
			<when state="dead: ˇ" output="ǧ"/>
			<when state="dead: ˚" output="ġ"/>
			<when state="dead: Ω" output="γ"/>
			<when state="dead: √" output="⊂"/>
		</action>
		<action id="h">
			<when state="none" output="h"/>
			<when state="dead: ^" output="ĥ"/>
			<when state="dead: ¨" output="ḧ"/>
			<when state="dead: ©" output="←"/>
			<when state="dead: ¯" output="ħ"/>
			<when state="dead: ˇ" output="ȟ"/>
			<when state="dead: Ω" output="θ"/>
			<when state="dead: √" output="⊄"/>
		</action>
		<action id="i">
			<when state="none" output="i"/>
			<when state="dead: ^" output="î"/>
			<when state="dead: `" output="ì"/>
			<when state="dead: ~" output="ĩ"/>
			<when state="dead: ¨" output="ï"/>
			<when state="dead: ©" output="↗"/>
			<when state="dead: ¯" output="ī"/>
			<when state="dead: ´" output="í"/>
			<when state="dead: ˇ" output="ǐ"/>
			<when state="dead: Ω" output="η"/>
			<when state="dead: √" output="∞"/>
		</action>
		<action id="j">
			<when state="none" output="j"/>
			<when state="dead: ^" output="ĵ"/>
			<when state="dead: ©" output="↓"/>
			<when state="dead: ˇ" output="ǰ"/>
			<when state="dead: Ω" output="ι"/>
		</action>
		<action id="k">
			<when state="none" output="k"/>
			<when state="dead: ©" output="↑"/>
			<when state="dead: ´" output="ḱ"/>
			<when state="dead: ˇ" output="ǩ"/>
			<when state="dead: Ω" output="κ"/>
			<when state="dead: √" output="∋"/>
		</action>
		<action id="l">
			<when state="none" output="l"/>
			<when state="dead: ©" output="→"/>
			<when state="dead: ¯" output="ḻ"/>
			<when state="dead: ´" output="ł"/>
			<when state="dead: ˇ" output="ľ"/>
			<when state="dead: Ω" output="λ"/>
			<when state="dead: √" output="∥"/>
		</action>
		<action id="m">
			<when state="none" output="m"/>
			<when state="dead: ©" output="↘"/>
			<when state="dead: ´" output="ḿ"/>
			<when state="dead: Ω" output="μ"/>
			<when state="dead: √" output="∈"/>
		</action>
		<action id="n">
			<when state="none" output="n"/>
			<when state="dead: ~" output="ñ"/>
			<when state="dead: ©" output="↙"/>
			<when state="dead: ´" output="ń"/>
			<when state="dead: ˇ" output="ň"/>
			<when state="dead: Ω" output="ν"/>
			<when state="dead: √" output="ⁿ"/>
		</action>
		<action id="o">
			<when state="none" output="o"/>
			<when state="dead: ^" output="ô"/>
			<when state="dead: `" output="ò"/>
			<when state="dead: ~" output="õ"/>
			<when state="dead: ¨" output="ö"/>
			<when state="dead: ¯" output="ō"/>
			<when state="dead: ´" output="ó"/>
			<when state="dead: ˇ" output="ǒ"/>
			<when state="dead: Ω" output="ο"/>
			<when state="dead: √" output="∘"/>
		</action>
		<action id="p">
			<when state="none" output="p"/>
			<when state="dead: ©" output="℗"/>
			<when state="dead: ´" output="ṕ"/>
			<when state="dead: Ω" output="π"/>
			<when state="dead: √" output="∂"/>
		</action>
		<action id="q">
			<when state="none" output="q"/>
			<when state="dead: Ω" output="ω"/>
		</action>
		<action id="r">
			<when state="none" output="r"/>
			<when state="dead: ©" output="®"/>
			<when state="dead: ´" output="ŕ"/>
			<when state="dead: ˇ" output="ř"/>
			<when state="dead: Ω" output="ρ"/>
			<when state="dead: √" output="√"/>
		</action>
		<action id="s">
			<when state="none" output="s"/>
			<when state="dead: ^" output="ŝ"/>
			<when state="dead: ©" output="℠"/>
			<when state="dead: ´" output="ś"/>
			<when state="dead: ˇ" output="š"/>
			<when state="dead: Ω" output="σ"/>
			<when state="dead: √" output="∩"/>
		</action>
		<action id="space">
			<when state="none" output=" "/>
			<when state="dead: ^" output="^"/>
			<when state="dead: `" output="`"/>
			<when state="dead: ~" output="~"/>
			<when state="dead: ¨" output="¨"/>
			<when state="dead: ©" output="©"/>
			<when state="dead: ¯" output="¯"/>
			<when state="dead: ´" output="´"/>
			<when state="dead: ˇ" output="ˇ"/>
			<when state="dead: ˚" output="˚"/>
			<when state="dead: √" output="√"/>
		</action>
		<action id="t">
			<when state="none" output="t"/>
			<when state="dead: ¨" output="ẗ"/>
			<when state="dead: ©" output="™"/>
			<when state="dead: ¯" output="ŧ"/>
			<when state="dead: ˇ" output="ť"/>
			<when state="dead: Ω" output="τ"/>
		</action>
		<action id="u">
			<when state="none" output="u"/>
			<when state="dead: ^" output="û"/>
			<when state="dead: `" output="ù"/>
			<when state="dead: ~" output="ũ"/>
			<when state="dead: ¨" output="ü"/>
			<when state="dead: ©" output="↖"/>
			<when state="dead: ¯" output="ū"/>
			<when state="dead: ´" output="ú"/>
			<when state="dead: ˇ" output="ǔ"/>
			<when state="dead: ˚" output="ů"/>
			<when state="dead: Ω" output="ω"/>
			<when state="dead: √" output="∪"/>
		</action>
		<action id="v">
			<when state="none" output="v"/>
			<when state="dead: Ω" output="β"/>
		</action>
		<action id="w">
			<when state="none" output="w"/>
			<when state="dead: ^" output="ŵ"/>
			<when state="dead: ¨" output="ẅ"/>
			<when state="dead: ´" output="ẃ"/>
			<when state="dead: ˚" output="ẘ"/>
			<when state="dead: Ω" output="ψ"/>
		</action>
		<action id="x">
			<when state="none" output="x"/>
			<when state="dead: ¨" output="ẍ"/>
			<when state="dead: Ω" output="ξ"/>
		</action>
		<action id="y">
			<when state="none" output="y"/>
			<when state="dead: ^" output="ŷ"/>
			<when state="dead: ~" output="ỹ"/>
			<when state="dead: ¨" output="ÿ"/>
			<when state="dead: ¯" output="ȳ"/>
			<when state="dead: ´" output="ý"/>
			<when state="dead: ˚" output="ẙ"/>
			<when state="dead: Ω" output="υ"/>
		</action>
		<action id="z">
			<when state="none" output="z"/>
			<when state="dead: ´" output="ź"/>
			<when state="dead: ˇ" output="ž"/>
			<when state="dead: ˚" output="ż"/>
			<when state="dead: Ω" output="ζ"/>
			<when state="dead: √" output="↯"/>
		</action>
		<action id="{">
			<when state="none" output="{"/>
			<when state="dead: Ω" output="₍"/>
		</action>
		<action id="|">
			<when state="none" output="|"/>
			<when state="dead: √" output="∨"/>
		</action>
		<action id="}">
			<when state="none" output="}"/>
			<when state="dead: Ω" output="₎"/>
		</action>
		<action id="~">
			<when state="none" output="~"/>
			<when state="dead: √" output="≈"/>
		</action>
		<action id="~ option">
			<when state="none" next="dead: ~"/>
		</action>
		<action id="¨">
			<when state="none" next="dead: ¨"/>
		</action>
		<action id="©">
			<when state="none" next="dead: ©"/>
		</action>
		<action id="¯">
			<when state="none" next="dead: ¯"/>
		</action>
		<action id="´">
			<when state="none" next="dead: ´"/>
		</action>
		<action id="Ä">
			<when state="none" output="Ä"/>
			<when state="dead: `" output="Ą"/>
		</action>
		<action id="Æ">
			<when state="none" output="Æ"/>
			<when state="dead: ¯" output="Ǣ"/>
			<when state="dead: ´" output="Ǽ"/>
		</action>
		<action id="Ë">
			<when state="none" output="Ë"/>
			<when state="dead: `" output="Ę"/>
		</action>
		<action id="Ï">
			<when state="none" output="Ï"/>
			<when state="dead: `" output="Į"/>
		</action>
		<action id="Ö">
			<when state="none" output="Ö"/>
			<when state="dead: `" output="Ǫ"/>
		</action>
		<action id="Ø">
			<when state="none" output="Ø"/>
			<when state="dead: ´" output="Ǿ"/>
		</action>
		<action id="Ü">
			<when state="none" output="Ü"/>
			<when state="dead: `" output="Ų"/>
			<when state="dead: ˇ" output="Ǚ"/>
		</action>
		<action id="ä">
			<when state="none" output="ä"/>
			<when state="dead: `" output="ą"/>
		</action>
		<action id="æ">
			<when state="none" output="æ"/>
			<when state="dead: ¯" output="ǣ"/>
			<when state="dead: ´" output="ǽ"/>
		</action>
		<action id="ë">
			<when state="none" output="ë"/>
			<when state="dead: `" output="ę"/>
		</action>
		<action id="ï">
			<when state="none" output="ï"/>
			<when state="dead: `" output="į"/>
		</action>
		<action id="ö">
			<when state="none" output="ö"/>
			<when state="dead: `" output="ǫ"/>
		</action>
		<action id="ø">
			<when state="none" output="ø"/>
			<when state="dead: ´" output="ǿ"/>
		</action>
		<action id="ü">
			<when state="none" output="ü"/>
			<when state="dead: `" output="ų"/>
			<when state="dead: ˇ" output="ǚ"/>
		</action>
		<action id="ˇ">
			<when state="none" next="dead: ˇ"/>
		</action>
		<action id="˚">
			<when state="none" next="dead: ˚"/>
		</action>
		<action id="Ω">
			<when state="none" next="dead: Ω"/>
		</action>
		<action id="√">
			<when state="none" next="dead: √"/>
		</action>
	</actions>
	<terminators>
		<when state="dead: ^" output="^"/>
		<when state="dead: `" output="`"/>
		<when state="dead: ~" output="~"/>
		<when state="dead: ¨" output="¨"/>
		<when state="dead: ©" output="©"/>
		<when state="dead: ¯" output="¯"/>
		<when state="dead: ´" output="´"/>
		<when state="dead: ˇ" output="ˇ"/>
		<when state="dead: ˚" output="˚"/>
		<when state="dead: Ω" output="Ω"/>
		<when state="dead: √" output=" "/>
	</terminators>
</keyboard>
 """