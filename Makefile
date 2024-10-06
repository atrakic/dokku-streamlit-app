MAKEFLAGS += --silent

BASEDIR=$(shell git rev-parse --show-toplevel)

.PHONY: all infra clean restore update backup test deploy

all:
	$(BASEDIR)/scripts/configure.sh
	$(BASEDIR)/scripts/deploy.sh

infra:
	pushd $(BASEDIR)/infra; make; popd

restore update backup test deploy:
	$(BASEDIR)/scripts/$@.sh

clean:
	$(BASEDIR)/scripts/clean.sh
	pushd $(BASEDIR)/infra; make clean; popd
