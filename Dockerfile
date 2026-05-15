# knowledge-base-oci — build-time corpus artifact.
#
# Final stage is `scratch` because this image is never executed; knowledge-agent
# COPYs /wiki out of it at build time and discards the rest. Trivy has nothing
# to scan in the final layer.

FROM registry.internal.telnyx.com/docker/library/debian:trixie-slim AS builder
ARG VERSION=unknown
COPY wiki/ /out/wiki/
RUN echo "$VERSION" > /out/wiki/VERSION

FROM scratch
COPY --from=builder /out/wiki /wiki
