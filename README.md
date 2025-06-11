# Django CRUD アプリケーション

Django を使用した商品管理システムです。商品の作成、読み取り、更新、削除（CRUD）機能を提供するWebアプリケーションです。

## 機能

### 基本機能
- 📦 **商品管理**: 商品の一覧表示、詳細表示、新規作成、編集、削除
- 🏷️ **カテゴリ管理**: 商品をカテゴリ別に分類
- 🖼️ **画像アップロード**: 商品画像の登録・表示
- 📄 **ページネーション**: 商品一覧のページ分割表示
- 🔐 **認証システム**: ログイン/ログアウト機能
- ⚙️ **管理画面**: Django管理画面での商品・カテゴリ管理

### UI/UX
- 📱 **レスポンシブデザイン**: Bootstrap 5.3を使用
- 🎨 **直感的なUI**: わかりやすいナビゲーションとボタン配置
- 🔍 **検索・フィルタリング**: 管理画面での商品検索とカテゴリフィルタ

## 技術スタック

- **フレームワーク**: Django 4.2/5.2.1
- **データベース**: SQLite
- **フロントエンド**: Bootstrap 5.3
- **フォームスタイリング**: django-bootstrap-form
- **言語**: Python, HTML, CSS, JavaScript

## プロジェクト構成

```
learn_django/
├── myproject/
│   ├── manage.py
│   ├── myproject/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── crud/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── tests.py
│       ├── migrations/
│       └── templates/
│           ├── base.html
│           ├── top.html
│           ├── login.html
│           └── crud/
│               ├── product_list.html
│               ├── product_detail.html
│               ├── product_form.html
│               ├── product_update_form.html
│               └── product_confirm_delete.html
├── .gitignore
└── README.md
```

## データモデル

### Product（商品）
- `name`: 商品名（CharField, max_length=200）
- `price`: 価格（PositiveIntegerField）
- `description`: 商品説明（TextField, blank=True）
- `category`: カテゴリ（ForeignKey to Category）
- `img`: 商品画像（ImageField, blank=True）

### Category（カテゴリ）
- `name`: カテゴリ名（CharField, max_length=200）

## インストールと実行

### 必要条件
- Python 3.8以上
- pip

### セットアップ手順

1. **リポジトリのクローン**
   ```bash
   git clone <repository-url>
   cd learn_django
   ```

2. **仮想環境の作成と有効化**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **依存関係のインストール**
   ```bash
   pip install django
   pip install django-bootstrap-form
   pip install Pillow  # 画像処理用
   ```

4. **プロジェクトディレクトリに移動**
   ```bash
   cd myproject
   ```

5. **データベースマイグレーション**
   ```bash
   python manage.py migrate
   ```

6. **スーパーユーザーの作成（管理画面用）**
   ```bash
   python manage.py createsuperuser
   ```

7. **開発サーバーの起動**
   ```bash
   python manage.py runserver
   ```

8. **アプリケーションにアクセス**
   - メインアプリ: http://127.0.0.1:8000/
   - 管理画面: http://127.0.0.1:8000/admin/

## 使用方法

### 基本的な操作

1. **ログイン**
   - トップページの「ログイン」から認証

2. **商品管理**
   - 商品一覧: `/crud/`
   - 新規作成: 一覧ページの「新規作成」ボタン
   - 詳細表示: 商品行の「詳細」ボタン
   - 編集: 商品行の「編集」ボタン
   - 削除: 商品行の「削除」ボタン

3. **管理画面での操作**
   - `/admin/` にアクセス
   - スーパーユーザーでログイン
   - 商品とカテゴリの管理が可能

### ページ構成

- **トップページ** (`/`): ウェルカムページ
- **商品一覧** (`/crud/`): 全商品の一覧表示
- **商品詳細** (`/crud/<id>/`): 個別商品の詳細情報
- **新規作成** (`/crud/new/`): 新しい商品の登録
- **編集** (`/crud/edit/<id>/`): 既存商品の更新
- **削除** (`/crud/delete/<id>/`): 商品の削除確認
- **ログイン** (`/login/`): ユーザー認証

## 設定

### メディアファイル
- 画像ファイルは `media_local/` ディレクトリに保存
- `MEDIA_URL = '/media/'` で設定済み

### 認証設定
- ログイン必須: 商品関連の全ページ
- ログイン後リダイレクト: 商品一覧ページ
- ログアウト後リダイレクト: トップページ

### 言語・タイムゾーン
- 言語: 日本語 (`ja`)
- タイムゾーン: `Asia/Tokyo`

## 開発・カスタマイズ

### 新機能の追加
1. `models.py` でデータモデルを定義
2. マイグレーションの作成と適用
3. `views.py` でビューロジックを実装
4. `urls.py` でURL設定を追加
5. テンプレートファイルの作成

### スタイルのカスタマイズ
- Bootstrap 5.3のクラスを使用
- `base.html` でベーステンプレートを変更可能

## トラブルシューティング

### よくある問題

**画像が表示されない場合:**
- `Pillow` がインストールされているか確認
- `MEDIA_ROOT` と `MEDIA_URL` の設定を確認
- `urls.py` で静的ファイルの配信設定を確認

**ログインできない場合:**
- スーパーユーザーが作成されているか確認
- `python manage.py createsuperuser` で新規作成

**マイグレーションエラー:**
```bash
python manage.py makemigrations
python manage.py migrate
```

## ライセンス

このプロジェクトは学習目的で作成されています。

## 貢献

プルリクエストやイシューの報告を歓迎します。

---

**注意**: このアプリケーションは開発環境での使用を想定しています。本番環境で使用する場合は、セキュリティ設定の見直しが必要です。