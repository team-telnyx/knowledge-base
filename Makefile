service := knowledge-base-oci
tag := red
image := registry.internal.telnyx.com/jenkins/$(service):$(tag)
version := $(shell date -u +%Y.%m.%d.%H.%M).$(shell echo "$${GITHUB_SHA:-$$(git rev-parse HEAD 2>/dev/null || echo unknown)}" | cut -c1-7)

.PHONY: build test

build:
	docker build --no-cache --build-arg VERSION=$(version) -t $(image) .

test:
	@echo "no tests"
