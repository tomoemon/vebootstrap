echo テスト用 PyPI へ登録します
python setup.py register -r https://testpypi.python.org/pypi
echo 次に本番 PyPI へ登録します
pause
python setup.py register
echo 登録完了しました

