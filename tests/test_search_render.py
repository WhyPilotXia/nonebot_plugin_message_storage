# python3
# -*- coding: utf-8 -*-

import base64

from nonebot_plugin_smart_message_storage.handlers.search import FONT_PATH, text_to_base64_image


def test_bundled_font_can_render_chinese_search_results():
    assert FONT_PATH.is_file()

    result = text_to_base64_image(["[2026-06-19 09:14:33] 测试用户(123): 中文消息"])

    assert result.startswith("base64://")
    assert base64.b64decode(result.removeprefix("base64://")).startswith(b"\x89PNG\r\n\x1a\n")
