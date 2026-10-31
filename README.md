# network-topo

## 1. 環境構築手順（Windows | PowerShell）
1. 適当なディレクトリで以下のコマンドを実行する。
```bash
git clone https://github.com/shikao-web/network-topo
cd ./network-topo
```

2. 以下のコマンドで仮想環境を作成する
```bash
py -3.12 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\activate.ps1
```
3. 以下のコマンドを実行し、必要なライブラリをインストールする
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. hello.pyを実行して動作確認する


## 2. 環境構築手順（Ubuntu）
1. 適当なディレクトリで以下のコマンドを実行する。
```bash
git clone https://github.com/shikao-web/network-topo
cd ./network-topo
```

2. 以下のコマンドで仮想環境を作成する
```bash
python3.12 -m venv .venv
source ./.venv/bin/activate
```
3. 以下のコマンドを実行し、必要なライブラリをインストールする
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. hello.pyを実行して動作確認する


## 3. 実行手順
1. 環境構築まで終わった状態で`.venv`環境を用いて、プロジェクトルートから以下のコマンドを実行する。
```
python src/app.py
```
2. ターミナルで指定されたURLにアクセスする。
