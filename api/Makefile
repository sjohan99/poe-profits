.PHONY: run-local run-ninja test

run-local:
	cd poe_profit_calc && export POE_PROFIT_CALC_RUN_MODE=local && fastapi dev main.py

run-prod:
	cd poe_profit_calc && export POE_PROFIT_CALC_RUN_MODE=prod && export PYTHONOPTIMIZE=TRUE && fastapi dev main.py

test:
	poetry run pytest tests

test-create-snapshots:
	export POE_PROFIT_CALC_RUN_MODE=test && poetry run pytest snapshots --snapshot-update

test-snapshots:
	export POE_PROFIT_CALC_RUN_MODE=test && poetry run pytest -vv snapshots
