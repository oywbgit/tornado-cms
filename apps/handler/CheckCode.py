#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'ouyangweibiao'

# from apps.handler.Ch
#
# class CheckCodeHandler(BaseHandler):
#     def get(self, *args, **kwargs):
#         import io
#         import check_code
#         mstream = io.BytesIO()
#         img,code = check_code.create_validate_code()
#         img.save(mstream,"GIF")
#         self.session['CheckCode'] =code
#         self.write(mstream.getvalue())