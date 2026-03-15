#!/usr/bin/python3

import subprocess

# 適当な量のデータを作成してメモリを獲得する。
# メモリ容量が少ないシステムではプログラムがメモリ不足で失敗する可能性がある。
# その場合はsizeの値を小さくして再実行すること。
size = 100000000

print("メモリ獲得前のシステム全体のメモリ使用量を表示します。")
subprocess.run("free")

array = [0]*size

print("メモリ獲得後のシステム全体のメモリ空き容量を表示します。")
subprocess.run("free")