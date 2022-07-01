# Bitcoind exporter
Tested with `bitcoind v0.21`

 * [metrics response example](docs/metrics.sample)
 * [docker-compose.yml](docker-compose.yml)
 * [grafana panel](staff/grafana/dashboards/bitcoind.json)

# Environment variables
 * `HOST` listen host, default:`localhost`
 * `PORT` listen port, default:`8064`
 * `BITCOIND` bitcoind url, default:`http://bitcoind:bitcoind@localhost:8335`
 * `COLLECTORS` enabled collectors, all by default

# Docker container
Docker container available at `ghcr.io/a1fred/bitcoind_exporter`.

`amd64` and `arm64` arch supported.


```
docker create -v "./staff/bitcoind.conf:/home/bitcoin/.bitcoind/bitcoind.conf:ro" --health-cmd="curl -s --fail --data-binary '{\"jsonrpc\":\"1.0\",\"id\":\"curltext\",\"method\":\"getblockchaininfo\",\"params\":[]}' -H 'content-type:text/plain;' http://bitcoind:bitcoind@localhost:8332/ || exit 1" --health-interval 10s --health-timeout 5s --health-retries 5 ruimarinho/bitcoin-core:0.19
```