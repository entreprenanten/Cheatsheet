import os
import pathlib
from datetime import datetime

from markupsafe import Markup

from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('vim', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'vim'
information = {
	'tool': 'Vim',
	'title': 'Vim Cheatsheet',
	'subtitle': 'This site is a reference for the text editor Vim',
	'description': 'Vim is a contaction of Vi IMproved and is a clone of the text-editor Vi but with additions. It is a highly configurable text-editor with an initial released version seeing the world in 1991. It is mainly designed as a command-line application but also comes in a GUI version.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '✔',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Vim', [
				helper.characteristics.get('text-editor'),
			])
	],
	'topic_uris': [
		'text-editor',
	],
}
general_info_text = ''
general_info_text_lead = ''
general_info_links = {}
general_info = [
	Markup('Commands written with brackets has two options for invocation, e.g <kbd>:h[elp]</kbd> can be invoked with either <kbd>:h</kbd> or <kbd>:help</kbd>'),
]
general_info_flag = True
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading': helper.set_folder('Global'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c93076668a524adc87b633e7b3f02d37',
		'info': {
			"You can run the command vimtutor in a terminal to learn the first Vim commands.",
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('623f8b7d31c74315b00e57340ea041fb')[0]),
					'flag': helper.set_entry_command_string(':h[elp] keyword'),

					'description': Markup('Open help for keyword'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bb5779a2aae44e6790bacfc82548da43')[0]),
					'flag': helper.set_entry_command_string(':sav[eas] file'),

					'description': Markup('Save file as'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cb74376473ed4a579d9affb65857157a')[0]),
					'flag': helper.set_entry_command_string(':clo[se]'),

					'description': Markup('Close current pane'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a30ca15ac33a4c1b80c273167a858cab')[0]),
					'flag': helper.set_entry_command_string(':ter[minal]'),

					'description': Markup('Open a terminal window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ae4e33ed841e458e9ec3bb988773c5b2')[0]),
					'flag': helper.set_entry_command_string('K'),

					'description': Markup('Open man page for word under the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Cursor Movement'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('8350e158415a40c884b820ec6c71d844')[0]),
		'info': {
			'Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.'
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('bec1d24064a64e4cbe02f796d7078101')[0]),
					'flag': helper.set_entry_command_string('h'),

					'description': Markup('Move cursor left'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('510f3bf369f3432fb64e84869351c8c7')[0]),
					'flag': helper.set_entry_command_string('j'),

					'description': Markup('Move cursor down'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0d285069f0794fd6bf1dec3c4499ded1')[0]),
					'flag': helper.set_entry_command_string('k'),

					'description': Markup('Move cursor up'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2d6a442a695c4a719ee4661ddf41db01')[0]),
					'flag': helper.set_entry_command_string('l'),

					'description': Markup('Nove cursor right'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0e8c9352ed7c4e42895fd09a01106674')[0]),
					'flag': helper.set_entry_command_string('H'),

					'description': Markup('Move to top of screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2d0fcdd0d14f406799aa2283f11047ad')[0]),
					'flag': helper.set_entry_command_string('M'),

					'description': Markup('Move to middle of screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6752ec2ea0bf48628211a731b7a028e1')[0]),
					'flag': helper.set_entry_command_string('L'),

					'description': Markup('Move to bottom of screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('68d1440f45a54a0da3ca8fe6366d148e')[0]),
					'flag': helper.set_entry_command_string('w'),

					'description': Markup('Jump forwards to the start of a word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('766a4ad2fccd441e9f1d9f35117da1f6')[0]),
					'flag': helper.set_entry_command_string('W'),

					'description': Markup('Jump forwards to the start of a word (words can contain punctuation)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fe0bfe1308c34d8b83b0889009549f91')[0]),
					'flag': helper.set_entry_command_string('e'),

					'description': Markup('Jump forwards to the end of a word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ce5e6a1ca5514acea031ed59449cf7d7')[0]),
					'flag': helper.set_entry_command_string('E'),

					'description': Markup('Jump forwards to the end of a word (words can contain punctuation)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('88d1a9baaf8947ea862d1964f9885d97')[0]),
					'flag': helper.set_entry_command_string('b'),

					'description': Markup('Jump backwards to the start of a word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0d2f922e8c1840d19bc1773a1507063a')[0]),
					'flag': helper.set_entry_command_string('B'),

					'description': Markup('Jump backwards to the start of a word (words can contain punctuation)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('625fb684cdd04023a609ced01d0491da')[0]),
					'flag': helper.set_entry_command_string('%'),
					'description': Markup('Move to matching character (default supported pairs: \'()\', \'{}\', \'[]\' - use :h matchpairs in vim for more info)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7e555ca169524fe49bfaac433a596cc4')[0]),
					'flag': helper.set_entry_command_string('0'),

					'description': Markup('Jump to the start of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e4c5e31bfa5e4e61ab6c9b41833b51e6')[0]),
					'flag': helper.set_entry_command_string('^'),

					'description': Markup('Jump to the first non-blank character of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2af22212b18c426a96089e1b20768f85')[0]),
					'flag': helper.set_entry_command_string('$'),

					'description': Markup('Jump to the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2abaded425c34406947db38f5b9c838f')[0]),
					'flag': helper.set_entry_command_string('g_'),

					'description': Markup('Jump to the last non-blank character of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c4f6dd7ae4ad40788b166fe700aa0a35')[0]),
					'flag': helper.set_entry_command_string('gg'),

					'description': Markup('Go to the first line of the document'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e5e25bce737d45189d0973a44a6bb5bb')[0]),
					'flag': helper.set_entry_command_string('G'),

					'description': Markup('Go to the last line of the document'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('13746e1df4ce4d83ae105e95aa7723f4')[0]),
					'flag': Markup(helper.set_entry_command_string('5gg</kbd> or <kbd>5G')),

					'description': Markup('Go to line 5'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a1366e0a08174d14b4fa4523608362b3')[0]),
					'flag': helper.set_entry_command_string('fx'),

					'description': Markup('Jump to next occurrence of character x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('565f3093bf5445cc954106537b77b7aa')[0]),
					'flag': helper.set_entry_command_string('tx'),

					'description': Markup('Jump to before next occurrence of character x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cb02049632534c77a2d9b3c5ca4eef1a')[0]),
					'flag': helper.set_entry_command_string('Fx'),

					'description': Markup('Jump to previous occurence of character x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('39b212e7309f4b3e9380b379088a506b')[0]),
					'flag': helper.set_entry_command_string('Tx'),

					'description': Markup('Jump to after previous occurence of character x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f5afeaa7071244cba41d9d2ced53f1de')[0]),
					'flag': helper.set_entry_command_string(';'),

					'description': Markup('Repeat previous f, t, F or T movement'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('45b32411f8854f84b11192008b7b7672')[0]),
					'flag': helper.set_entry_command_string(','),

					'description': Markup('Repeat previous f, t, F or T movement, backwards'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2070b1ae25584fb7af993afa8061dd96')[0]),
					'flag': helper.set_entry_command_string('}'),

					'description': Markup('Jump to next paragraph (or function/block, when editing code)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('902f2db218df467d8aef2af91cad295b')[0]),
					'flag': helper.set_entry_command_string('{'),

					'description': Markup('Jump to previous paragraph (or function/block, when editing code)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b484a56eab0d432fbbdf8d90f3169bec')[0]),
					'flag': helper.set_entry_command_string('zz'),

					'description': Markup('Center cursor on screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5946983e060d45c692b6f80b65c7dab6')[0]),
					'flag': helper.set_entry_command_string('Ctrl + e'),

					'description': Markup('Move screen down one line (without moving cursor)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0170ce184097464ea6b8eae308236ca4')[0]),
					'flag': helper.set_entry_command_string('Ctrl + y'),

					'description': Markup('Move screen up one line (without moving cursor)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('df7096b2bfc34ee99acaf8c8f8bfa142')[0]),
					'flag': helper.set_entry_command_string('Ctrl + b'),

					'description': Markup('Move back one full screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1965825cd15f48ba877e706340e0285e')[0]),
					'flag': helper.set_entry_command_string('Ctrl + f'),

					'description': Markup('Move forward one full screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d8072fccb3f040629a8f7f63207cbf3c')[0]),
					'flag': helper.set_entry_command_string('Ctrl + d'),

					'description': Markup('Move forward 1/2 a screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c0bca914d09e4a7b981605e3ba651e5a')[0]),
					'flag': helper.set_entry_command_string('Ctrl + u'),

					'description': Markup('Move back 1/2 a screen'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Insert mode'),
		'subtitle': 'Inserting/Appending Text',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c420950f49f24ad691bfee8697fd29c4',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c2e578afc7324d68b5323d31a8bd3964')[0]),
					'flag': helper.set_entry_command_string('i'),

					'description': Markup('Insert before the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bf7eee46e132410ea03316458669f91c')[0]),
					'flag': helper.set_entry_command_string('I'),

					'description': Markup('Insert at the beginning of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b9e8d5e7ee9d4a97b2ab7b14652c6e29')[0]),
					'flag': helper.set_entry_command_string('a'),

					'description': Markup('Insert (append) after the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('23c9ffdf16f0490d9203e4690fc27aef')[0]),
					'flag': helper.set_entry_command_string('A'),

					'description': Markup('Insert (append) at the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1c4a3a24c1504dc2a073f28eb6606130')[0]),
					'flag': helper.set_entry_command_string('o'),

					'description': Markup('Append (open) a new line below the current line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1d4a3eda19904fc88c0cfc6b83784497')[0]),
					'flag': helper.set_entry_command_string('O'),

					'description': Markup('Append (open) a new line above the current line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c4dbc5201fb146d9bcb74575688600bc')[0]),
					'flag': helper.set_entry_command_string('ea'),

					'description': Markup('Insert (append) at the end of the word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b967b081d49c4edd9094d590771a6cdf')[0]),
					'flag': helper.set_entry_command_string('Ctrl + h'),

					'description': Markup('Delete the character before the cursor during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('30a046922eec46c29024b719548a4367')[0]),
					'flag': helper.set_entry_command_string('Ctrl + w'),

					'description': Markup('Delete word before the cursor during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c10383110ac64f8b9e786f1988c32259')[0]),
					'flag': helper.set_entry_command_string('Ctrl + j'),

					'description': Markup('Begin new line during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('02bacd78a2504c9db83e03f34765519a')[0]),
					'flag': helper.set_entry_command_string('Ctrl + t'),

					'description': Markup('Indent (move right) line one shiftwidth during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d5926ecf3df94c0d8f3434801e450766')[0]),
					'flag': helper.set_entry_command_string('Ctrl + d'),

					'description': Markup('De-indent (move left) line one shiftwidth during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('85010d1627cd4eb096d70e6f68c2a2fb')[0]),
					'flag': helper.set_entry_command_string('Ctrl + n'),

					'description': Markup('Insert (auto-complete) next match before the cursor during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('471548d83b9d4a6b9e6d5a560424178f')[0]),
					'flag': helper.set_entry_command_string('Ctrl + p'),

					'description': Markup('Insert (auto-complete) previous match before the cursor during insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fd0f622bd43940539877e017f9b38c9d')[0]),
					'flag': helper.set_entry_command_string('Ctrl + rx'),

					'description': Markup('Insert the contents of register x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e55ba736004e4648a28c3b9d1478727d')[0]),
					'flag': helper.set_entry_command_string('Esc'),

					'description': Markup('Exit insert mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Editing'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '8c0f5c3acbcb4cac9f909ca62dfe6ffa',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a1158e97583b479c97041e4541358466')[0]),
					'flag': helper.set_entry_command_string('r'),

					'description': Markup('Replace a single character'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('45f5381607e945f997f8c31d987f4319')[0]),
					'flag': helper.set_entry_command_string('J'),

					'description': Markup('JJoin line below to the current one with one space in between'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('04a4facf6c8f4a7cb3e3ea13847b9157')[0]),
					'flag': helper.set_entry_command_string('gJ'),

					'description': Markup('Join line below to the current one without space in between'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('73d1620a31ed41088b3596131692a2b5')[0]),
					'flag': helper.set_entry_command_string('gwip'),

					'description': Markup('Reflow paragraph'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b3302ea4aef24e81b36350ddc9db6330')[0]),
					'flag': helper.set_entry_command_string('g~'),

					'description': Markup('Switch case up to motion'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1db64d5693bf4c349b4e4447254ad6f6')[0]),
					'flag': helper.set_entry_command_string('gu'),

					'description': Markup('Change to lowercase up to motion'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0fabfc7995bd48d7a917652cbcdfba56')[0]),
					'flag': helper.set_entry_command_string('gU'),

					'description': Markup('Change to uppercase up to motion'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('885aaf418c7742958aa7be4c22f0f9a2')[0]),
					'flag': helper.set_entry_command_string('cc'),

					'description': Markup('Change (replace) entire line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f518de48a3074f4f870e4808f0d5249f')[0]),
					'flag': helper.set_entry_command_string('C'),

					'description': Markup('Change (replace) to the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b673d64375354deba5a9a5021bca9fbc')[0]),
					'flag': helper.set_entry_command_string('c$'),

					'description': Markup('Change (replace) to the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5c41c9f4c3584f27a40befa986360534')[0]),
					'flag': helper.set_entry_command_string('ciw'),

					'description': Markup('Change (replace) entire word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6013a76ea8854f09afa4da7049b05c90')[0]),
					'flag': helper.set_entry_command_string('cw'),

					'description': Markup('Change (replace) to the end of the word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a6c6d1ddb14d4d33ab3b661e21b7b636')[0]),
					'flag': helper.set_entry_command_string('s'),

					'description': Markup('Delete character and substitute text'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('71612e817bdd4188be36368e0c3d4325')[0]),
					'flag': helper.set_entry_command_string('S'),

					'description': Markup('Delete line and substitute text (same as cc)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e30cec89b2bc4464b53870d61e7fc322')[0]),
					'flag': helper.set_entry_command_string('xp'),

					'description': Markup('Transpose two letters (delete and paste)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('3babc1298f2d448992285414ded852d6')[0]),
					'flag': helper.set_entry_command_string('u'),

					'description': Markup('Undo'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a51aba39320448e588ececfc68b6fb56')[0]),
					'flag': helper.set_entry_command_string('U'),

					'description': Markup('Restore (undo) last changed line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('60f05ad543064a5ea5c9330aea00171e')[0]),
					'flag': helper.set_entry_command_string('Ctrl + r'),

					'description': Markup('Redo'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bf688dafeabf4337a35e950b0856124d')[0]),
					'flag': helper.set_entry_command_string('.'),

					'description': Markup('Repeat last command'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Visual Mode'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('a8b5eab8a57b485f9dc7ca68261d7d89')[0]),
		'info': {
			'When selecting a block with ab or aB, alternatively you can use ( or {'
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('bf663c89e49f49e2a23358ba5941e660')[0]),
					'flag': helper.set_entry_command_string('v'),

					'description': Markup('Start visual mode, mark lines, then do a command (like y-yank)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('38c3a8069d6a4654be3cc6ecc450ffe3')[0]),
					'flag': helper.set_entry_command_string('V'),

					'description': Markup('Start linewise visual mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ecdb1fa37b31440095fd7a97ce72ae2c')[0]),
					'flag': helper.set_entry_command_string('o'),

					'description': Markup('Move to other end of marked area'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('09e971e085704a2a93562ea73e410144')[0]),
					'flag': helper.set_entry_command_string('Ctrl + v'),

					'description': Markup('Start visual block mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('36ce6dc6ba714453ab5ba3ac620f6963')[0]),
					'flag': helper.set_entry_command_string('O'),

					'description': Markup('Move to other corner of block'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('11febf07337f48289476a7541a4790d3')[0]),
					'flag': helper.set_entry_command_string('aw'),

					'description': Markup('Mark a word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1fc335a696cc43b2855cf52a305d47f0')[0]),
					'flag': helper.set_entry_command_string('ab'),

					'description': Markup('A block with ()'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5950dcb8a9fb4ea5bc3764723ae242a9')[0]),

					'flag': helper.set_entry_command_string('aB'),
					'description': Markup('A block with {}'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('abb79e36162249168c95dd0205d5589a')[0]),
					'flag': helper.set_entry_command_string('at'),

					'description': Markup('A block with <> tags'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('09a930147b4b4454ba8132d2730ae503')[0]),
					'flag': helper.set_entry_command_string('ib'),

					'description': Markup('Inner block with ()'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2c74118e6dba45e5959e23554071b5e9')[0]),

					'flag': helper.set_entry_command_string('iB'),
					'description': Markup('Inner block with {}'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('43398bd33a774f83b98ba247bc992a8e')[0]),
					'flag': helper.set_entry_command_string('it'),

					'description': Markup('Inner block with <> tags'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('09e1f94dfd3b4249b61b97292f24c205')[0]),
					'flag': helper.set_entry_command_string('Esc'),

					'description': Markup('Exit visual mode'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Visual Commands'),
		'subtitle': 'Commands applicable in Visual Mode',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '3ce9788016614aa98023eecf2b78c75a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('97a9cff06c93418fae72640d889d7d47')[0]),
					'flag': helper.set_entry_command_string('>'),

					'description': Markup('Shift text right'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4b61642c2db5490b8570970fb6565450')[0]),
					'flag': helper.set_entry_command_string('<'),

					'description': Markup('Shift text left'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('37d32b1bc4e6447cb0c18c728c0978ab')[0]),
					'flag': helper.set_entry_command_string('y'),

					'description': Markup('Yank (copy) marked text'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ddf352904a4c4ec08167b485f92484a4')[0]),
					'flag': helper.set_entry_command_string('d'),

					'description': Markup('Delete marked text'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('035cf2462eff414baf0be3238f168d50')[0]),
					'flag': helper.set_entry_command_string('~'),

					'description': Markup('Switch case'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fbfa65cd0ef54a3c81fbe91d465f8000')[0]),
					'flag': helper.set_entry_command_string('u'),

					'description': Markup('Change marked text to lowercase'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0c583ad4b2b644c4a0214af707c602da')[0]),
					'flag': helper.set_entry_command_string('U'),

					'description': Markup('Change marked text to uppercase'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},

			]
		}
	},
	{
		'heading': helper.set_folder('Registers'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('bfeb48fb477342adae82b8e698f32b06')[0]),
		'info': {
			'Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.',
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2fdd5bcfa476493a90a1f2b6c2ef5449')[0]),
					'flag': helper.set_entry_command_string(':reg[isters]'),

					'description': Markup('Show registers content'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cfdf49d6810b48d6957c5bebfdf1df4a')[0]),
					'flag': helper.set_entry_command_string('"xy'),

					'description': Markup('Yank into register x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f6fa5a34d3c04e3bb12484344d25a2d5')[0]),
					'flag': helper.set_entry_command_string('"xp'),

					'description': Markup('Paste contents of register x'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4e3e97b9ce564113a17765a4fa6e442a')[0]),
					'flag': helper.set_entry_command_string('"+y'),

					'description': Markup('Yank into the system clipboard register'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('46c5be38ac5444dea2075cb306d3f8fc')[0]),
					'flag': helper.set_entry_command_string('"+p'),

					'description': Markup('Paste from the system clipboard register'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Special Registers'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '53a2ef778486454090f7d28f3e5d737d',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e7a9dfd8be604fb2959ad68542ec45a9')[0]),
					'flag': helper.set_entry_command_string('0'),

					'description': Markup('Last yank'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4b306dcb664b464f9c4fe6fa6e030081')[0]),
					'flag': helper.set_entry_command_string('"'),

					'description': Markup('Unnamed register, last delete or yank'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c773ecbb316349c59779b88ce9635f1f')[0]),
					'flag': helper.set_entry_command_string('%'),

					'description': Markup('Current file name'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('60c8b8a6f89f4e0db016a3eba454d673')[0]),
					'flag': helper.set_entry_command_string('#'),

					'description': Markup('Alternate file name'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4ede54f370f94afbb35794790106f4da')[0]),
					'flag': helper.set_entry_command_string('*'),

					'description': Markup('Clipboard contents (X11 primary)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d47d974dbbd74b209cfdde68c91e02d2')[0]),
					'flag': helper.set_entry_command_string('+'),

					'description': Markup('Clipboard contents (X11 clipboard)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c9ffc89fecbc46c0b1357ba6d3295bad')[0]),
					'flag': helper.set_entry_command_string('/'),

					'description': Markup('Last search pattern'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4825c1c258dd486fb1d6970d522533e5')[0]),
					'flag': helper.set_entry_command_string(':'),

					'description': Markup('Last command-line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('312550118afe4de897ff30869f6e8920')[0]),
					'flag': helper.set_entry_command_string('.'),

					'description': Markup('Last inserted text'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b517416b73194a9ab401923615542c53')[0]),
					'flag': helper.set_entry_command_string('-'),

					'description': Markup('Last small (less than a line) delete'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7a25c29f3b4445a283f6a3d79dc1cce1')[0]),
					'flag': helper.set_entry_command_string('='),

					'description': Markup('Expression register'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b4ae9616c6b84b28ac9ad214a9a7c901')[0]),
					'flag': helper.set_entry_command_string('_'),

					'description': Markup('Black hole register'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Marks and Positions'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('adb318476a4e4f7dbe6afe491a7a9e08')[0]),
		'': {
			'To jump to a mark you can either use a backtick (`) or an apostrophe (\'). Using an apostrophe jumps to the beginning (first non-black) of the line holding the mark.',
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b7e5deb150124a3f9904a225af2f5857')[0]),
					'flag': helper.set_entry_command_string(':marks'),

					'description': Markup('List of marks'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9273fb1ba6af46ba8ce09fc5e3287c2a')[0]),
					'flag': helper.set_entry_command_string('ma'),

					'description': Markup('Set current position for mark A'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a82e0999e8fa4ff5af266f797003a0a9')[0]),
					'flag': helper.set_entry_command_string('`a'),

					'description': Markup('Jump to position of mark A'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5202bca2d804d88a078e9f3a90b9215')[0]),
					'flag': helper.set_entry_command_string('y`a'),

					'description': Markup('Yank text to position of mark A'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('469c1cf1166744188ddb84e61e9abcaf')[0]),
					'flag': helper.set_entry_command_string('`0'),

					'description': Markup('Go to the position where Vim was previously exited'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('18f09310bfa0442fa6ea501a66db3dfe')[0]),
					'flag': helper.set_entry_command_string('`"'),

					'description': Markup('Go to the position when last editing this file'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ede687bb4b024eee8e4d7d94d9b8df76')[0]),
					'flag': helper.set_entry_command_string('`.'),

					'description': Markup('Go to the position of the last change in this file'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('84ab576271a543ea948ad6f08b651ebb')[0]),
					'flag': helper.set_entry_command_string('``'),

					'description': Markup('Go to the position before the last jump'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c64ea67df02d4d6da338f166d37ac079')[0]),
					'flag': helper.set_entry_command_string(':ju[mps]'),

					'description': Markup('List of jumps'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1cc45dcf3c7746c18a70120f6b666f50')[0]),
					'flag': helper.set_entry_command_string('Ctrl + i'),

					'description': Markup('Go to newer position in jump list'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c73108b15d934290865d8204fc17c6fe')[0]),
					'flag': helper.set_entry_command_string('Ctrl + o'),

					'description': Markup('Go to older position in jump list'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b808abc00c234a6d86b826b1ff664796')[0]),
					'flag': helper.set_entry_command_string(':changes'),

					'description': Markup('List of changes'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('513a24e9a2514173851f25940121a6b8')[0]),
					'flag': helper.set_entry_command_string('g,'),

					'description': Markup('Go to newer position in change list'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('3b978d8de8c749259c30f62f44169cc7')[0]),
					'flag': helper.set_entry_command_string('g;'),

					'description': Markup('Go to older position in change list'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('68f3c2a5331e482bb804c4c90f11065c')[0]),
					'flag': helper.set_entry_command_string('Ctrl + ]'),

					'description': Markup('Jump to the tag under cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Macros'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f4eeb79c5bf34dfcab2e5982bbcb52ac',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('15f9de38c06d42afb24dda717bf97c72')[0]),
					'flag': helper.set_entry_command_string('qa'),

					'description': Markup('Record macro a'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c743d2f0be6445ba91ddc859b2dff074')[0]),
					'flag': helper.set_entry_command_string('q'),

					'description': Markup('Stop recording macro'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('927e9f5f40124a828c669750e2d5f5a4')[0]),
					'flag': helper.set_entry_command_string('@a'),

					'description': Markup('Run macro a'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('db2003135fb645e0af86b8efa7d7bfa8')[0]),
					'flag': helper.set_entry_command_string('@@'),

					'description': Markup('Rerun last run macro'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Cut and paste'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'a90f28c75c7740ea981127e6d376a29c',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('4a6da67fae17400ab7714b7058ffd7f6')[0]),
					'flag': helper.set_entry_command_string('yy'),

					'description': Markup('Yank (copy) a line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d6aae05c26af4b6396afc45af626bf1d')[0]),
					'flag': helper.set_entry_command_string('2yy'),

					'description': Markup('Yank (copy) 2 lines'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bc766f7c853b478f983d0fa99b70c8bd')[0]),
					'flag': helper.set_entry_command_string('yw'),

					'description': Markup('Yank (copy) the characters of the word from the cursor position to the start of the next word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('da8c724dd26d4d349c0c895c9e6225f2')[0]),
					'flag': helper.set_entry_command_string('y$'),

					'description': Markup('Yank (copy) to end of line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e92f7423bdff4359a0ddfef510d6f6d2')[0]),
					'flag': helper.set_entry_command_string('p'),

					'description': Markup('Put (paste) the clipboard after cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('242e988d9aca4628bd42088cebf681f0')[0]),
					'flag': helper.set_entry_command_string('P'),

					'description': Markup('Put (paste) before cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cee72e71692a4890b7f42d237695698d')[0]),
					'flag': helper.set_entry_command_string('dd'),

					'description': Markup('Delete (cut) a line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4c0060bf5eb84f65a23337b041f12cea')[0]),
					'flag': helper.set_entry_command_string('2dd'),

					'description': Markup('Delete (cut) 2 lines'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0dceac4be0a3463190e08bccc03cd3f3')[0]),
					'flag': helper.set_entry_command_string('dw'),

					'description': Markup('Delete (cut) the characters of the word from the cursor position to the start of the next word'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4f4aa9ccb5d64cefb2db2d900664ebff')[0]),
					'flag': helper.set_entry_command_string('D'),

					'description': Markup('Delete (cut) to the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ddcb3138ecf446f58f11fe6be30e5222')[0]),
					'flag': helper.set_entry_command_string('d$'),

					'description': Markup('Delete (cut) to the end of the line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d346b69234e1476b8941bb80b289becf')[0]),
					'flag': helper.set_entry_command_string('x'),

					'description': Markup('Delete (cut) character'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Indent text'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0e5bbe44ac2d48539e2e6da548c86fcb',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e15731a0de9842da9a920ceab69bf645')[0]),
					'flag': helper.set_entry_command_string('>>'),

					'description': Markup('Indent (move right) line one shiftwidth'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bfc6b131f5374fa490aa0ad999b28e35')[0]),
					'flag': helper.set_entry_command_string('<<'),

					'description': Markup('De-indent (move left) line one shiftwidth'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('512d288066214d9e8e8559ba2cd44091')[0]),
					'flag': helper.set_entry_command_string('>%'),
					'description': Markup('Indent a block with () or {} (cursor on brace)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27ebbad8356443ec894b49695e7e439c')[0]),
					'flag': helper.set_entry_command_string('>ib'),

					'description': Markup('Indent inner block with ()'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('aedd0bfc39174962adf9ecab43db2e3c')[0]),
					'flag': helper.set_entry_command_string('>at'),

					'description': Markup('Indent a block with <> tags'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5479244a7394460883cd3430befa4d7e')[0]),
					'flag': helper.set_entry_command_string('3=='),

					'description': Markup('Re-indent 3 lines'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('74b52425b9d64f58b43a196e6e77d2ad')[0]),

					'flag': helper.set_entry_command_string('=%'),
					'description': Markup('Re-indent a block with () or {} (cursor on brace)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3bd9a9b6656d487cad5a86fe0323e929')[0]),

					'flag': helper.set_entry_command_string('=iB'),
					'description': Markup('Re-indent inner block with {}'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('79273140568a480181cf21b9e508fb18')[0]),
					'flag': helper.set_entry_command_string('gg=G'),

					'description': Markup('Re-indent entire buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('73931b87c654469a97a805ae593af1d5')[0]),
					'flag': helper.set_entry_command_string(']p'),

					'description': Markup('Paste and adjust indent to current line'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Exiting'),
		'subtitle': 'How to Exit Vim',
		'description': 'This section describes how to exit Vim',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '9a09c8d326c141aaafc3063ac8c5ae64',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e4cf635aa5d745bcbd4ffd0102e146e4')[0]),
					'flag': helper.set_entry_command_string(':w'),

					'description': Markup('Write (save) the file, but don\'t exit'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7f1ad63dc8eb4f49b3fbdd15a76cc9cb')[0]),
					'flag': helper.set_entry_command_string(':w !sudo tee %'),

					'description': Markup('Write out the current file using sudo'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c7ff2ddba6f44c8ea90d617107e37f50')[0]),
					'flag': Markup(helper.set_entry_command_string(':wq</kbd> or <kbd>:x</kbd> or <kbd>ZZ')),

					'description': Markup('Write (save) and quit'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('21364b20c7124bc5a462314952ea1daa')[0]),
					'flag': helper.set_entry_command_string(':q'),

					'description': Markup('Quit (fails if there are unsaved changes)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4d5c88567c4b4f63bb7f2075c12b5187')[0]),
					'flag': Markup(helper.set_entry_command_string(':q!</kbd> or <kbd>ZQ')),

					'description': Markup('Quit and throw away unsaved changes'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('53ad1d7219e7413990c1b96d2c4a93eb')[0]),
					'flag': helper.set_entry_command_string(':wqa'),

					'description': Markup('Write (save) and quit on all tabs'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Search and Replace'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '00b2a8f5a180491f8781c6a64a898c24',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('4853242fee8a41efbbf4dacd93d10e4c')[0]),
					'flag': helper.set_entry_command_string('/pattern'),

					'description': Markup('Search for pattern'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f788b890e78a420cace72583e0b759bf')[0]),
					'flag': helper.set_entry_command_string('?pattern'),

					'description': Markup('Search backward for pattern'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('36d51d280fc1452eab16ab90f6c5d174')[0]),
					'flag': helper.set_entry_command_string('\\vpattern'),

					'description': Markup('\'Very magic\' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4abd1f3628514062a9480787a4fc0043')[0]),
					'flag': helper.set_entry_command_string('n'),

					'description': Markup('Repeat search in same direction'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d51c9b9a907e4506a324abfb235181b6')[0]),
					'flag': helper.set_entry_command_string('N'),

					'description': Markup('Repeat search in opposite direction'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('15dfe5afef4c404e938a88e320e01947')[0]),
					'flag': helper.set_entry_command_string(':%s/old/new/g'),

					'description': Markup('Replace all old with new throughout file'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9af0a1af00e04340aa4333e05062b079')[0]),
					'flag': helper.set_entry_command_string(':%s/old/new/gc'),

					'description': Markup('Replace all old with new throughout file with confirmations'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('147c897b1afa4a51987bc1232731db38')[0]),
					'flag': helper.set_entry_command_string(':noh[lsearch]'),

					'description': Markup('Remove highlighting of search matches'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Search in Multiple Files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0097ad10a08643f885b32121af63bee1',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('465bebbe9a174a608523f1b4643b3119')[0]),
					'flag': helper.set_entry_command_string(':vim[grep] /pattern/ {`{file}`}'),

					'description': Markup('Search for pattern in multiple files'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e66af115d934402ca285868d69aa6e72')[0]),
					'flag': helper.set_entry_command_string(':cn[ext]'),

					'description': Markup('Jump to the next match'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9ead8c0087b043f08bdec26004b2e2c0')[0]),
					'flag': helper.set_entry_command_string(':cp[revious]'),

					'description': Markup('Jump to the previous match'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('147fbe0c31a9458e9f98825274f75d74')[0]),
					'flag': helper.set_entry_command_string(':cope[n]'),

					'description': Markup('Open a window containing the list of matches'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4ab16c6371b14b4da316be856cdada65')[0]),
					'flag': helper.set_entry_command_string(':ccl[ose]'),

					'description': Markup('Close the quickfix window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Tabs'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '39457a06f7e94bbaa1c7921ae5ddbc4f',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('526e8fc35b7c46da9cd232043be91380')[0]),
					'flag': Markup(helper.set_entry_command_string(':tabnew</kbd> or <kbd>:tabnew&nbsp;{page.words.file}')),

					'description': Markup('Open a file in a new tab'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5cec92bcac944ea0b7af61c37b3ca0be')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wT'),

					'description': Markup('Move the current split window into its own tab'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f32bc7eb69164be8a03ebe2c95089d6e')[0]),
					'flag': Markup(helper.set_entry_command_string('gt</kbd> or <kbd>:tabn[ext]')),

					'description': Markup('Move to the next tab'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bcb4d8bdb28a416a85833ac5d1c07667')[0]),
					'flag': Markup(helper.set_entry_command_string('gT</kbd> or <kbd>:tabp[revious]')),

					'description': Markup('Move to the previous tab'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('62aa8bea4f824b8189627a3e469f16bd')[0]),
					'flag': helper.set_entry_command_string('#gt'),

					'description': Markup('Move to tab number #'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('34c02c7fa3364e27ba43a39303ae6434')[0]),
					'flag': helper.set_entry_command_string(':tabm[ove] #'),

					'description': Markup('Move current tab to the #th position (indexed from 0)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5b84119f84f9458d9c4885a8525601d3')[0]),
					'flag': helper.set_entry_command_string(':tabc[lose]'),

					'description': Markup('Close the current tab and all its windows'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6b4d1bd05d11485d8802ed90323cb3f9')[0]),
					'flag': helper.set_entry_command_string(':tabo[nly]'),

					'description': Markup('Close all tabs except for the current one'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('24d1234b9ddc4c239549e0c614799da1')[0]),
					'flag': helper.set_entry_command_string(':tabdo'),

					'description': Markup('Command - run the command on all tabs (e.g. :tabdo q - closes all opened tabs)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Working with multiple files'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '8ce300b54abb42fe999e2bdd7a6fc4b0',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8e396d9d2f1943528caf15236dd191c9')[0]),
					'flag': helper.set_entry_command_string(':e[dit] file'),

					'description': Markup('Edit a file in a new buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4e7bec54de754a198095c7c9c3a481c4')[0]),
					'flag': helper.set_entry_command_string(':bn[ext]'),

					'description': Markup('Go to the next buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2d853b63160643b18f0205e944186e1c')[0]),
					'flag': helper.set_entry_command_string(':bp[revious]'),

					'description': Markup('Go to the previous buffer'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2580c96497bb406480a02dc38d21f313')[0]),
					'flag': helper.set_entry_command_string(':bd[elete]'),

					'description': Markup('Delete a buffer (close a file)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e6ba73d50c4b4febb12efe9b2ae65961')[0]),
					'flag': helper.set_entry_command_string(':b[uffer]#'),

					'description': Markup('Go to a buffer by index #'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('71609168401749e1931f67d4bfce09c4')[0]),
					'flag': helper.set_entry_command_string(':b[uffer] file'),

					'description': Markup('Go to a buffer by file'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a1537f6dad424c5cb292ba6131d0a60f')[0]),
					'flag': helper.set_entry_command_string(':ls or :buffers'),

					'description': Markup('List all open buffers'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4814b4d63c4e49038a4e8921d6be482c')[0]),
					'flag': helper.set_entry_command_string(':sp[lit] file'),

					'description': Markup('Open a file in a new buffer and split window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('47f3715b34d94f90b7c67366fc00f7fe')[0]),
					'flag': helper.set_entry_command_string(':vs[plit] file'),

					'description': Markup('Open a file in a new buffer and vertically split window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7ad00e8614364c03a296bbc081c4a6f2')[0]),
					'flag': helper.set_entry_command_string(':vert[ical] ba[ll]'),

					'description': Markup('Edit all buffers as vertical windows'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d0890ec271d347998a8afb158015e839')[0]),
					'flag': helper.set_entry_command_string(':tab ba[ll]'),

					'description': Markup('Edit all buffers as tabs'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6101f4d7f3d94609a06c155495fcfbd0')[0]),
					'flag': helper.set_entry_command_string('Ctrl + ws'),

					'description': Markup('Split window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('91ac2f91b0b642a9b0b8004e59aee796')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wv'),

					'description': Markup('Split window vertically'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2dc3de563b3c4a289576651cb2542b76')[0]),
					'flag': helper.set_entry_command_string('Ctrl + ww'),

					'description': Markup('Switch windows'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('87f1eca8870a412db5774a21f9432dfc')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wq'),

					'description': Markup('Quit a window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('36b78b8bbaa944ba8d3e9e38a9ef9c9d')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wx'),

					'description': Markup('Exchange current window with next one'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('07afb8db33b246a8bad1bfac35d0b908')[0]),
					'flag': helper.set_entry_command_string('Ctrl + w='),

					'description': Markup('Make all windows equal height & width'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d0503bbb7bfb4ab5a9edfad7fe37dbb9')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wh'),

					'description': Markup('Move cursor to the left window (vertical split)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('39c0dca34fbe4cd896407995871d5fc1')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wl'),

					'description': Markup('Move cursor to the right window (vertical split)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1f7c3b3f1de84a86b6ecce4448c05d7f')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wj'),

					'description': Markup('Move cursor to the window below (horizontal split)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('43ecb96f2df446b595c589930ead952c')[0]),
					'flag': helper.set_entry_command_string('Ctrl + wk'),

					'description': Markup('Move cursor to the window above (horizontal split)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading': helper.set_folder('Diff'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': Markup(helper.set_entry_folder('9ba4f5c075e643f19d1b7e2566752c75')[0]),
		'info': {
			'The commands for folding (e.g. za) operate on one level. To operate on all levels, use uppercase letters (e.g. zA).',
			'To view the differences of files, one can directly start Vim in diff mode by running vimdiff in a terminal. One can even set this as git difftool.',
		},
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('fdb3a182ba844f5ab80b4d0e0e3d2c5b')[0]),
					'flag': helper.set_entry_command_string('zf'),

					'description': Markup('Manually define a fold up to motion'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9ec8e0726bdb4eb28b31942b673d0c93')[0]),
					'flag': helper.set_entry_command_string('zd'),

					'description': Markup('Delete fold under the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('44ff164ed9ac4d4bb5276b858fce7958')[0]),
					'flag': helper.set_entry_command_string('za'),

					'description': Markup('Toggle fold under the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('61a37880e7c5431f8f1be1eeb5a5fa56')[0]),
					'flag': helper.set_entry_command_string('zo'),

					'description': Markup('Open fold under the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('731032abe3ce417d98728a787bfa835f')[0]),
					'flag': helper.set_entry_command_string('zc'),

					'description': Markup('Close fold under the cursor'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('368d80b30d524e5684fe2fe9f034d03f')[0]),
					'flag': helper.set_entry_command_string('zr'),

					'description': Markup('Reduce (open) all folds by one level'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5e5eacaf85641dbafe21cbabe83d2ee')[0]),
					'flag': helper.set_entry_command_string('zm'),

					'description': Markup('Fold more (close) all folds by one level'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7a5cd0b0e1f4407b986b1589cb3eb5f8')[0]),
					'flag': helper.set_entry_command_string('zi'),

					'description': Markup('Toggle folding functionality'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7e8555967e974115a6111c49cee9a86f')[0]),
					'flag': helper.set_entry_command_string(']c'),

					'description': Markup('Jump to start of next change'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8a0421c8063d4bac9978745c2750f714')[0]),
					'flag': helper.set_entry_command_string('[c'),

					'description': Markup('Jump to start of previous change'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('35705b76194842599a77c3e1f695e1e8')[0]),
					'flag': helper.set_entry_command_string('do or :diffg[et]'),

					'description': Markup('Obtain (get) difference (from other buffer)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a0070b66577640fdaba10bd29e6a0302')[0]),
					'flag': helper.set_entry_command_string('dp or :diffpu[t]'),

					'description': Markup('Put difference (to other buffer)'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ad61790f582a4c44a7a78260745f99df')[0]),
					'flag': helper.set_entry_command_string(':diffthis'),

					'description': Markup('Make current window part of diff'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5ef7cd869ec495dba54695d17b81e8e')[0]),
					'flag': helper.set_entry_command_string(':dif[fupdate]'),

					'description': Markup('Update differences'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('56e5e3dcd54944409cf0d0f26f1fec08')[0]),
					'flag': helper.set_entry_command_string(':diffo[ff]'),

					'description': Markup('Switch off diff mode for current window'),
					'video': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'uuid': helper.get_uuid(),

				},
			]
		}
	},

]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://github.com/hakluke/how-to-exit-vim',
			'title': 'How to Exit Vim',
			'description': Markup('The most complex ways of exiting Vim.. and some of the simplest; but that is no fun!'),
			'footer': 'Be warned: some of these methods may destroy your system.',
			'screencapture': ''
		},
		{
			'link': 'https://sanctum.geek.nz/arabesque/vim-koans/',
			'title': 'Vim Koans',
			'description': Markup('Carved into stone tabulas at a time when day was dark and matter was void; this wisdom will surely bring enlightenment upon humanity'),
			'screencapture': 'resources/graphic/link_screen_captures/sanctum_geek_nz.png',
		},
	)
]
affiliate_products = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'title': Markup('Vim cheatsheet stickers!'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/B00359YK5E/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00359YK5E&linkCode=as2&tag=cheatsheet0e-20&linkId=fa5b9f2e3651cdc9b22cb69b04b50ca8"><img style="max-height:150px; max-width: 150px;"  border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B00359YK5E&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=B00359YK5E" width="100px" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup('Stickers to put on your keyboard! Great tool for learning Vim'),
			'description': '',
		},
		{
			'title': Markup('Practical Vim'),
			'affiliate_link': Markup(
				'<a target="_blank"  href="https://www.amazon.com/gp/product/1680501275/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1680501275&linkCode=as2&tag=cheatsheet0e-20&linkId=60e2174b375aae9b613f4f5b9d4f5050"><img style="max-height:150px; max-width: 150px;" border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1680501275&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=cheatsheet0e-20" ></a><img src="//ir-na.amazon-adsystem.com/e/ir?t=cheatsheet0e-20&l=am2&o=1&a=1680501275" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />'),
			'footer': Markup(''),
			'description': '',
		}
	)
]
licensing = [
	Markup('This Vim cheatsheet is MIT licensed. <a href="https://github.com/rtorr/vim-cheat-sheet">See original work here.</a>')
]
