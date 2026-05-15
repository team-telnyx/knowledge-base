# Build interface for the Telnyx CI pipeline (infra-ci-gha-workflows/dockerImage.yml).
# `service` MUST match `names.service` in meta-dev.yml.
#
# `version` mirrors the format infra-ci-action-metadata generates
# (YYYY.MM.DD.HH.mm.shortsha). The two are computed independently — a
# minute-boundary race can in principle leave wiki/VERSION one minute ahead of
# the registry tag. The mismatch is cosmetic: wiki/VERSION is a provenance
# marker for consumers, not a content address.

service := knowledge-base-oci
tag := red
image := registry.internal.telnyx.com/jenkins/$(service):$(tag)
version := $(shell date -u +%Y.%m.%d.%H.%M).$(shell echo "$${GITHUB_SHA:-$$(git rev-parse HEAD 2>/dev/null || echo unknown)}" | cut -c1-7)

.PHONY: build test

build:
	docker build --no-cache --build-arg VERSION=$(version) -t $(image) .

test:
	@echo "no tests — image is a content-only build artifact"
