# -*- coding: utf-8 -*-

import rltk

edit_distance_cost = {'insert': {'c':50}, 'insert_default':100, 'delete_default':100, 'substitute_default':100}

tk = rltk.init()
tk.load_edit_distance_table('A1', edit_distance_cost)
tk.load_df_corpus('B1', 'df_corpus_1.txt', file_type='text', mode='append')
tk.load_df_corpus('B2', 'jl_file_1.jsonl', file_type='json_lines', json_path='desc[*]', mode='append')

print tk.levenshtein_distance('a', 'abc')
print tk.levenshtein_distance('a', 'abc', name='A1')
print tk.tf_idf_similarity(['a', 'b', 'a'], ['a', 'c','d','f'], name='B1')
print tk.tf_idf_similarity(['abc'], ['abc', 'def'], name='B2')