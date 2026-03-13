#!/bin/bash
false &
wait $! # falseプロセスの終了を待ち合わせる。falseコマンドのPIDは$!変数から得られる
echo "falseコマンドが終了しました: $?" # wait語にプロセスの戻り値は$?変数から得られる。