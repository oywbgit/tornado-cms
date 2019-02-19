#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

import binascii

RECT_HEIGHT = 16
RECT_WIDTH = 16
BYTE_COUNT_PER_ROW = RECT_WIDTH / 8
BYTE_COUNT_PER_FONT = BYTE_COUNT_PER_ROW * RECT_HEIGHT

KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]


class FontRender(object):
    def __init__(self, font_file,
                 rect_height=RECT_HEIGHT, rect_width=RECT_WIDTH, byte_count_per_row=BYTE_COUNT_PER_ROW):
        self.font_file = font_file
        self.rect_height = rect_height
        self.rect_width = rect_width
        self.byte_count_per_row = byte_count_per_row

        self.__init_rect_list__()

    def __init_rect_list__(self):
        self.rect_list = [] * RECT_HEIGHT

        for i in range(RECT_HEIGHT):
            self.rect_list.append([] * RECT_WIDTH)

    def get_font_area_index(self, txt, encoding='utf-8'):
        if not isinstance(txt, unicode):
            txt = txt.decode(encoding)

        gb2312 = txt.encode('gb2312')
        hex_str = binascii.b2a_hex(gb2312)

        area = eval('0x' + hex_str[:2]) - 0xA0
        index = eval('0x' + hex_str[2:]) - 0xA0

        return area, index

    def get_font_rect(self, area, index):
        offset = (94 * (area - 1) + (index - 1)) * BYTE_COUNT_PER_FONT
        btxt = None

        with open(self.font_file, "rb") as f:
            f.seek(offset)
            btxt = f.read(BYTE_COUNT_PER_FONT)

        return btxt

    def convert_font_rect(self, font_rect, ft=1, ff=0):
        for k in range(len(font_rect) / self.byte_count_per_row):
            row_list = self.rect_list[k]
            for j in range(self.byte_count_per_row):
                for i in range(8):
                    asc = binascii.b2a_hex(font_rect[k * self.byte_count_per_row + j])
                    asc = eval('0x' + asc)
                    flag = asc & KEYS[i]
                    row_list.append(flag and ft or ff)

    def render_font_rect(self, rect_list=None):
        if not rect_list:
            rect_list = self.rect_list

        for row in rect_list:
            for i in row:
                if i:
                    print
                    '■',
                else:
                    print
                    '○',
            print

    def convert(self, text, ft=None, ff=None, encoding='utf-8'):
        if not isinstance(text, 'unicode'):
            text = text.decode(encoding)

        for t in text:
            area, index = self.get_font_area_index(t)
            font_rect = self.get_font_rect(area, index)

            self.convert_font_rect(font_rect, ft=ft, ff=ff)

    def get_rect_info(self):
        return self.rect_list


if '__main__' == __name__:
    text = u'同创伟业'
    fr = FontRender('./font/16x16/hzk16h')
    fr.convert(text, ft='/static/*', ff=0)
    # print fr.get_rect_info()
    fr.render_font_rect()
