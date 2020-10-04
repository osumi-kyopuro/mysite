# mysite
「勤怠管理アプリ」取り扱い説明書
# 注意事項
- この「勤怠管理アプリ」は一つのコンピュータに複数人の方が勤怠管理をするためのものです。別コンピュータ間で勤怠管理できない仕様になっています。
- 「一般ユーザー」とはアカウントを持ち、ログイン、出勤ボタン、退勤ボタン、勤怠管理データ閲覧を許可されているユーザーです。
- 「管理ユーザー」とは一般ユーザーと同じ許可に加えて、ユーザー登録、ユーザー削除、勤怠管理データ登録、勤怠管理データ削除を許可されているユーザーです。
- これを見ている人が管理者ユーザーの場合は「注意事項」->「必要なもの」->「初期設定について」->「データ登録について」->「出退勤について」この順番で読み進めてください。
- これを見ている人が一般ユーザーの場合は「注意事項」->「出退勤について」この順番で読み進めてください。
- 「Page not found」が表示されることがありますがそのときはブラウザバックしてください。これは仕様です。
- 「初期設定」の「3」は管理ユーザーアカウント作成の説明です。
- 「初期設定」の「6」は一般ユーザーアカウント作成の説明です。

# 必要なもの
- python3.7
- django2.2
- git
- エディタ(推奨はVisual Studio Code)

# 初期設定について
1. アカウントログインボタンを押しユーザー名は「osumi」、パスワードは「(小文字アスタリスク)＊19991123Oy」を入力して管理サイトに入ります。
2. ユーザー追加ボタンを押す。
3. 自分のアカウント(ユーザー名、パスワード)を作成して「保存して編集を続ける」を押す。さらに「パーミッション」の「有効」と「スタッフ権限」と「スーパーユーザー権限」にチェックを入れて「保存」を押します。自分のアカウントの（ユーザー名、パスワード)は必ず忘れないようにしておいてください。
4. これであなたの管理ユーザーアカウントが作成されました。一度「osumi」アカウントからログアウトします。再度あなたの登録したアカウントでログインしてください。勤怠管理TOPページの上部にあなたのユーザー名が出力されていたらアカウントログイン出来てます。
5. それからユーザー変更ボタンを押しあなた以外のdefaultで入っていたユーザーをすべて削除してください。
6. それからあなた以外の一般ユーザーのアカウントを作成して「保存して編集を続ける」を押します。この一般ユーザーは何人でも構いません。さらに「パーミッション」の「有効」と「スタッフ権限」にチェックを入れて「保存」を押します。
7. それから「サイトを表示」を押します。そうすると勤怠管理TOPページに戻ることが出来ます。
8. 最後に「勤怠管理データ」->「データ消去メニューへ」->「データ全消去」を行ってください。これで初期設定は完了なので勤怠管理TOPページに戻りましょう。


# データ登録について
1. 「勤怠管理TOPページ」->「勤怠管理データ」->「データ登録フォームへ」までページ移動する。もし、データ登録する気がなく「データ登録フォーム」から「全体の勤怠管理データ(登録順)」ページに戻りたい場合はブラウザバックしてください。
2. 必須の「スタッフ情報」、「出勤予定時間」、「退勤予定時間」は必ず入力をしてください。
下の記入例を参考にしてください。
  - 出勤予定時間、退勤予定時間の記入例「2020-09-30 10:00:00」
3. 送信ボタンを押します。
4. 全データとの整合性が保てるものはデータを追加します。不整合なデータは追加できないようにしています。
5. 全体の勤怠管理データ(登録順)の一番下の列に追加されているか確認してください。
6(おまけ). 間違って登録してしまった場合は「データ消去メニューへ」->「最新登録データ消去」と遷移してみてください。おそらく「全体の勤怠管理データ(登録順)」の一番下の列がなくなっていることがわかります。

# 出退勤について
1. 「勤怠管理TOPページ」->「出勤」とページ遷移してください。
2. ここで「Page not found」が表示されている場合はブラウザバックしてください。そして「ちゃんと出勤予定時間の30分前よりあとか」、「前回のシフトの退勤ボタン押し忘れていないか」を「勤怠管理」->「勤怠管理データ」->「自分のデータ表示」と遷移して確認してください。
3. 出勤打刻を成功した場合は「(ユーザー名)さん！出勤！！」と「出勤打刻」が表示されます。
4. 退勤ボタンも同様です。
