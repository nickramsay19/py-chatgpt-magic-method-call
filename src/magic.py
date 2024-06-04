from __future__ import annotations
from typing import Any
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def _make_function_call_expr(f: str, *args, **kwargs) -> str:
    return f + '(' + ','.join([str(a) for a in args]) + ')'

sys.modules[__name__].__getattr__ = lambda f: lambda *args, **kwargs: _client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': 'square_root(9)'},
        {'role': 'assistant', 'content': '3.0'},
        {'role': 'user', 'content': 'sort([2,8,2,1)'},
        {'role': 'assistant', 'content': '[1,2,2,8]'},
        {'role': 'user', 'content': 'return_the_string_hi()'},
        {'role': 'assistant', 'content': '\'hi\''},
        {'role': 'user', 'content': 'yell(\'yo\')'},
        {'role': 'assistant', 'content': '\'YO!\''},
        {'role': 'user', 'content': 'raise_to_the_power_of_2(3)'},
        {'role': 'assistant', 'content': '9.0'},
        {'role': 'user', 'content': 'ping()'},
        {'role': 'assistant', 'content': '\'pong\''},
        {'role': 'user', 'content': 'concatenate_two_strings_together(\'a\', \'b\')'},
        {'role': 'assistant', 'content': '\'ab\''},
        {'role': 'user', 'content': 'give_me_a_random_number_please()'},
        {'role': 'assistant', 'content': '82'},
        {'role': 'user', 'content': 'is_5_a_prime_number()'},
        {'role': 'assistant', 'content': 'True'},
        {'role': 'user', 'content': 'the_int_8_interpreted_as_a_bool()'},
        {'role': 'assistant', 'content': 'True'},
        {'role': 'user', 'content': '2_plus_4_then_divided_by_3()'},
        {'role': 'assistant', 'content': '2.0'},
        {'role': 'user', 'content': 'does_rock_beat_scissors()'},
        {'role': 'assistant', 'content': 'True'},
        {'role': 'user', 'content': 'does_this_string_contain_two_vowels(\'howdy\')'},
        {'role': 'assistant', 'content': 'False'},
        {'role': 'user', 'content': _make_function_call_expr(f,*args)},
    ]
).choices[0].message.content

