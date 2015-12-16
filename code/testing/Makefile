test:
	python -m unittest discover

junit:
	py.test --junitxml junit.xml testBasic.py

coverage:
	coverage erase
	coverage run -m unittest discover
	coverage html

profile:
	rm -rf .profile
	python -m cProfile -o .profile Basic.py
	python -c "import pstats; pstats.Stats('.profile').sort_stats(2).reverse_order().print_stats(10)"


clean:
	rm -rf .profile .coverage htmlcov