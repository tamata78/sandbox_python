# _*_ coding: utf-8 _*_

# 複数行 改行あり
msg = repr(
    本日は晴天なり
    あかまきがみ
)

# 複数行 変数展開
msg = repr(
    本日は晴天なり
    あかまきがみ
    {add_str}
).format(add_str="追加文字列")

# 複数行 改行なし
msg1 = ('本日は晴天なり'
'あかまきがみ')

# f文字列（フォーマット済み文字列リテラル）
a = 123
b = 'abc'

print('{} and {}'.format(a, b)) # formatを使う書き方
print(f'{a} and {b}') # f文字列を使うと置換フィールドをそのまま指定可能
