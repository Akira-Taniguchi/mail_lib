mail_lib
======================
メールに関連するライブラリを作成しました。
ご利用は自己責任でご自由にどうぞ

使い方
------
１．pipコマンドを実行し、モジュールをダウンロードしてください

    pip install mail_lib

２．クラスをインポートし、下記例の用に使用してください

    from mail_lib.mail_utils import send_mail
    send_mail(['hoge@mail.com', 'huga@mail.com'], 'title', 'message\nmessage2', 'no-reply@mail.com', '192.168.1.1' )


機能紹介
------
### ユーティリティ
#### メール関連
***
send_mail(to_addr_list, subject, message, from_addr, smtp_host, smtp_port=25, cc_addr_list=[], bcc_addr_list=[]):メールを送信します

| 名前 | 必須 | 説明 | デフォルト値 | 
|:-----------|:------------:|:-----------|:-----------| 
| to_addr_list | ◯ | 送信先メールアドレス | - | 
| subject | ◯ | 件名 | - |
| message | ◯ | メッセージ、改行コードで区切れば、メール内容も改行されます | - |
| from_addr | ◯ | 送信元メールアドレス | - |
| smtp_host | ◯ | smtpサーバドメイン | - |
| smtp_port | × | smtpサーバポート | 25 |
| cc_addr_list | × | CCメールアドレス | [] |
| bcc_addr_list | × | BCCメールアドレス | [] |
戻り値：なし
***
send_attach_file_mail(to_addr_list, subject, message, file_path, from_addr, smtp_host, smtp_port=25, cc_addr_list=[], bcc_addr_list=[]):ファイルを添付したメールを送信します

| 名前 | 必須 | 説明 | デフォルト値 | 
|:-----------|:------------:|:-----------|:-----------| 
| to_addr_list | ◯ | 送信先メールアドレス | - | 
| subject | ◯ | 件名 | - |
| message | ◯ | メッセージ、改行コードで区切れば、メール内容も改行されます | - |
| file_path | ◯ | 添付するファイルのパス | - |
| from_addr | ◯ | 送信元メールアドレス | - |
| smtp_host | ◯ | smtpサーバドメイン | - |
| smtp_port | × | smtpサーバポート | 25 |
| cc_addr_list | × | CCメールアドレス | [] |
| bcc_addr_list | × | BCCメールアドレス | [] |
戻り値：なし
***


関連情報
--------
1. [ググレカス(ブログ)](http://gugurekasu.blogspot.jp/)
2. [LinkedIn](https://jp.linkedin.com/in/akirataniguchi1)
 
ライセンス
----------
Distributed under the [MIT License][mit].
[MIT]: http://www.opensource.org/licenses/mit-license.php
