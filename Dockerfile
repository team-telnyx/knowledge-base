# knowledge-base-oci — content-only OCI artifact carrying the compiled wiki.
#
# Final stage is `scratch` because this image is never executed: downstream
# consumers pull /wiki via `COPY --from=…`. Trivy has nothing to scan in the
# final layer.

FROM registry.internal.telnyx.com/docker/library/debian:trixie-slim AS builder
ARG VERSION=unknown
COPY wiki/ /out/wiki/
RUN echo "$VERSION" > /out/wiki/VERSION

FROM scratch
COPY --from=builder /out/wiki /wiki
