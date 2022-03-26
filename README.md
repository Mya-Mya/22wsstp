## 22 冬春の芝山寺子屋プロジェクト プログラミングブース

2022/03 に行われたプログラミングブースの成果物の雛形を管理・生成する。

## 生成されるサイトマップ

問題数が`N`個ある時、

`index.html` -> [ `{n}Q.html` <-> [ `{n}S{i}.html` for i in 1...3 ] for n in N ]->`fin.html`

## Get Started

5 つの問題の雛形を作ります。

```
> py build_empty_pages.py -n 5
```

`empty_pages/`に雛形の HTML ファイルが生成されます。質問文や選択肢を編集しましょう。

## `templates/`にあるものと Jinja2 変数

### headerbar.html

全ての画面の左上にある文字ロゴを表示するヘッダー画面。

### ogptags.html

OGP タグの雛形。

- `ogp_title` OGP タイトル
- `ogp_type` OGP タイプ

### index.html

最初の画面。

### Q.html

質問文画面の雛形。
`N`番目の問題の質問文画面は`f"{N}Q.html"`に改名する($N=1,...$)。

- `title` この画面のタイトル
- `S1_fn` 選択肢 1 のファイル名
- `S2_fn` 選択肢 2 のファイル名
- `S3_fn` 選択肢 3 のファイル名

### S.html

選択肢画面の雛形。
`N`番目の問題の`i`番目の選択肢画面は`f"{N}S{i}.html"`に改名する($N=1,..., i=1,2,3$)。

- `title` この画面のタイトル
- `Q_fn` 対応する質問文画面のファイル名
- `next_fn` この次の画面のファイル名
  - 最終問題だったら `"fin.html"`
  - それ以外だったら次の問題の質問文画面のファイル名

### fin.html

終了画面。
