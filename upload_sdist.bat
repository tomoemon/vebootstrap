echo テスト用 PyPI へアップロードします
python setup.py sdist upload -r https://testpypi.python.org/pypi
echo 次に本番 PyPI へアップロードします
pause
python setup.py sdist upload
echo 本番へのアップロード完了しました
