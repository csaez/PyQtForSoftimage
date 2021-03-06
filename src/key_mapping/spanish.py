#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import Qt

KEY_MAPPING = {
    # key: ( Qt::Key, ascii,  modifiers )

    8: (Qt.Key_Backspace,    '',     None),
    9: (Qt.Key_Tab,          '\t',   None),
    13: (Qt.Key_Enter,        '\n',   None),
    16: (Qt.Key_Shift,        '',     None),
    17: (Qt.Key_Control,      '',     None),
    18: (Qt.Key_Alt,          '',     None),
    19: (Qt.Key_Pause,        '',     None),
    20: (Qt.Key_CapsLock,     '',     None),
    27: (Qt.Key_Escape,       '',     None),
    32: (Qt.Key_Space,        ' ',    None),
    33: (Qt.Key_PageUp,       '',     None),
    34: (Qt.Key_PageDown,     '',     None),
    35: (Qt.Key_End,          '',     None),
    36: (Qt.Key_Home,         '',     None),
    37: (Qt.Key_Left,         '',     None),
    38: (Qt.Key_Up,           '',     None),
    39: (Qt.Key_Right,        '',     None),
    40: (Qt.Key_Down,         '',     None),
    44: (Qt.Key_SysReq,       '',     None),
    45: (Qt.Key_Insert,       '',     None),
    46: (Qt.Key_Delete,       '',     None),
    48: (Qt.Key_0,            '0',    None),
    49: (Qt.Key_1,            '1',    None),
    50: (Qt.Key_2,            '2',    None),
    51: (Qt.Key_3,            '3',    None),
    52: (Qt.Key_4,            '4',    None),
    53: (Qt.Key_5,            '5',    None),
    54: (Qt.Key_6,            '6',    None),
    55: (Qt.Key_7,            '7',    None),
    56: (Qt.Key_8,            '8',    None),
    57: (Qt.Key_9,            '9',    None),
    65: (Qt.Key_A,            'a',    None),
    66: (Qt.Key_B,            'b',    None),
    67: (Qt.Key_C,            'c',    None),
    68: (Qt.Key_D,            'd',    None),
    69: (Qt.Key_E,            'e',    None),
    70: (Qt.Key_F,            'f',    None),
    71: (Qt.Key_G,            'g',    None),
    72: (Qt.Key_H,            'h',    None),
    73: (Qt.Key_I,            'i',    None),
    74: (Qt.Key_J,            'j',    None),
    75: (Qt.Key_K,            'k',    None),
    76: (Qt.Key_L,            'l',    None),
    77: (Qt.Key_M,            'm',    None),
    78: (Qt.Key_N,            'n',    None),
    79: (Qt.Key_O,            'o',    None),
    80: (Qt.Key_P,            'p',    None),
    81: (Qt.Key_Q,            'q',    None),
    82: (Qt.Key_R,            'r',    None),
    83: (Qt.Key_S,            's',    None),
    84: (Qt.Key_T,            't',    None),
    85: (Qt.Key_U,            'u',    None),
    86: (Qt.Key_V,            'v',    None),
    87: (Qt.Key_W,            'w',    None),
    88: (Qt.Key_X,            'x',    None),
    89: (Qt.Key_Y,            'y',    None),
    90: (Qt.Key_Z,            'z',    None),
    93: (Qt.Key_Print,        '',     None),
    96: (Qt.Key_0,            '0',    Qt.KeypadModifier),
    97: (Qt.Key_1,            '1',    Qt.KeypadModifier),
    98: (Qt.Key_2,            '2',    Qt.KeypadModifier),
    99: (Qt.Key_3,            '3',    Qt.KeypadModifier),
    100: (Qt.Key_4,            '4',    Qt.KeypadModifier),
    101: (Qt.Key_5,            '5',    Qt.KeypadModifier),
    102: (Qt.Key_6,            '6',    Qt.KeypadModifier),
    103: (Qt.Key_7,            '7',    Qt.KeypadModifier),
    104: (Qt.Key_8,            '8',    Qt.KeypadModifier),
    105: (Qt.Key_9,            '9',    Qt.KeypadModifier),
    106: (Qt.Key_Asterisk,     '*',    Qt.KeypadModifier),
    107: (Qt.Key_Plus,         '+',    Qt.KeypadModifier),
    109: (Qt.Key_Minus,        '-',    Qt.KeypadModifier),
    110: (Qt.Key_Period,       '.',    Qt.KeypadModifier),
    111: (Qt.Key_Slash,        '/',    Qt.KeypadModifier),
    112: (Qt.Key_F1,           '',     None),
    113: (Qt.Key_F2,           '',     None),
    114: (Qt.Key_F3,           '',     None),
    115: (Qt.Key_F4,           '',     None),
    116: (Qt.Key_F5,           '',     None),
    117: (Qt.Key_F6,           '',     None),
    118: (Qt.Key_F7,           '',     None),
    119: (Qt.Key_F8,           '',     None),
    120: (Qt.Key_F9,           '',     None),
    121: (Qt.Key_F10,          '',     None),
    122: (Qt.Key_F11,          '',     None),
    113: (Qt.Key_F12,          '',     None),
    144: (Qt.Key_NumLock,      '',     None),
    145: (Qt.Key_ScrollLock,   '',     None),
    186: (Qt.Key_Semicolon,    u'`',   None),
    187: (Qt.Key_Equal,        '+',    None),
    188: (Qt.Key_Comma,        ',',    None),
    189: (Qt.Key_Minus,        '-',    None),
    190: (Qt.Key_Period,       '.',    None),
    191: (Qt.Key_Slash,        u'ç',   None),
    192: (Qt.Key_QuoteLeft,    u'ñ',   None),
    219: (Qt.Key_BracketLeft,  "'",    None),
    220: (Qt.Key_Backslash,    u'º',   None),
    221: (Qt.Key_BraceRight,   u'¡',   None),
    222: (Qt.Key_QuoteLeft,    u"´",   None),
    226: (Qt.Key_Less,         "<",    None),

    # Calculate the SHIFT key as 300 + key value
    348: (Qt.Key_ParenRight,   '=',    None),  # Shift+0
    349: (Qt.Key_Exclam,       '!',    None),  # Shift+1
    350: (Qt.Key_At,           '"',    None),  # Shift+2
    351: (Qt.Key_NumberSign,   u'·',   None),  # Shift+3
    352: (Qt.Key_Dollar,       '$',    None),  # Shift+4
    353: (Qt.Key_Percent,      '%',    None),  # Shift+5
    354: (Qt.Key_6,            '&',    None),  # Shift+6
    355: (Qt.Key_Ampersand,    '/',    None),  # Shift+7
    356: (Qt.Key_Asterisk,     '(',    None),  # Shift+8
    357: (Qt.Key_ParenLeft,    ')',    None),  # Shift+9

    365: (Qt.Key_A,            'A',    None),
    366: (Qt.Key_B,            'B',    None),
    367: (Qt.Key_C,            'C',    None),
    368: (Qt.Key_D,            'D',    None),
    369: (Qt.Key_E,            'E',    None),
    370: (Qt.Key_F,            'F',    None),
    371: (Qt.Key_G,            'G',    None),
    372: (Qt.Key_H,            'H',    None),
    373: (Qt.Key_I,            'I',    None),
    374: (Qt.Key_J,            'J',    None),
    375: (Qt.Key_K,            'K',    None),
    376: (Qt.Key_L,            'L',    None),
    377: (Qt.Key_M,            'M',    None),
    378: (Qt.Key_N,            'N',    None),
    379: (Qt.Key_O,            'O',    None),
    380: (Qt.Key_P,            'P',    None),
    381: (Qt.Key_Q,            'Q',    None),
    382: (Qt.Key_R,            'R',    None),
    383: (Qt.Key_S,            'S',    None),
    384: (Qt.Key_T,            'T',    None),
    385: (Qt.Key_U,            'U',    None),
    386: (Qt.Key_V,            'V',    None),
    387: (Qt.Key_W,            'W',    None),
    388: (Qt.Key_X,            'X',    None),
    389: (Qt.Key_Y,            'Y',    None),
    390: (Qt.Key_Z,            'Z',    None),

    486: (Qt.Key_Colon,        '^',    None),  # Shift+;
    487: (Qt.Key_Plus,         '*',    None),  # Shift++
    488: (Qt.Key_Less,         ';',    None),  # Shift+,
    489: (Qt.Key_Underscore,   '_',    None),  # Shift+-
    490: (Qt.Key_Greater,      ':',    None),  # Shift+>
    491: (Qt.Key_Question,     u'Ç',   None),  # Shift+?
    492: (Qt.Key_AsciiTilde,   u'Ñ',   None),  # Shift+`
    519: (Qt.Key_BraceLeft,    '?',    None),  # Shift+[
    520: (Qt.Key_Bar,          u'ª',   None),  # Shift+
    521: (Qt.Key_BraceRight,   u'¿',   None),  # Shift+]
    522: (Qt.Key_QuoteDbl,     u'¨',   None),  # Shift+'
    526: (Qt.Key_Less,         ">",    None),

    649: (Qt.Key_1,            '|',    None),  # AltGr+1
    650: (Qt.Key_2,            '@',    None),  # AltGr+2
    651: (Qt.Key_3,            '#',    None),  # AltGr+3
    654: (Qt.Key_6,            u'¬',   None),  # AltGr+6
    786: (Qt.Key_QuoteLeft,    '[',    None),  # AltGr+`
    787: (Qt.Key_Equal,        ']',    None),  # AltGr++
    791: (Qt.Key_Slash,        '}',    None),  # AltGr+ç
    820: (Qt.Key_Backslash,    '\\',   None),  # AltGr+º
    822: (Qt.Key_QuoteLeft,    "{",    None),  # AltGr+´
}
