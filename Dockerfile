FROM registry.internal.telnyx.com/docker/library/debian:trixie-slim AS builder
ARG VERSION=unknown
COPY wiki/ /out/wiki/
RUN echo "$VERSION" > /out/wiki/VERSION

FROM scratch
COPY --from=builder /out/wiki /wiki
